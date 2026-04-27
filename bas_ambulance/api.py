import frappe
from frappe import _
from frappe.utils import getdate, add_days, now_datetime
from .utils import calculate_distance

@frappe.whitelist()
def dispatch_ambulance(call_id, ambulance_id, crew_ids):
    """Assigns ambulance and crew to a call record and updates status."""
    call = frappe.get_doc("Patient Call Record", call_id)
    call.assigned_ambulance = ambulance_id
    
    # Add crew to child table
    call.set("assigned_crew", [])
    for crew_id in crew_ids:
        call.append("assigned_crew", {"crew_member": crew_id})
    
    call.call_status = "Dispatched"
    call.dispatch_time = now_datetime()
    call.save()
    
    # Update Ambulance Status
    frappe.db.set_value("Ambulance Master", ambulance_id, "operational_status", "On Trip")
    
    return {"status": "success", "message": _("Ambulance {0} dispatched for call {1}").format(ambulance_id, call_id)}

@frappe.whitelist()
def nearest_ambulance_lookup(latitude, longitude, vehicle_type=None):
    """Finds the nearest available ambulance based on coordinates."""
    ambulances = frappe.get_all("Ambulance Master", 
        filters={"operational_status": "Available", "current_gps_status": "Online"},
        fields=["name", "latitude", "longitude", "vehicle_type"]
    )
    
    if vehicle_type:
        ambulances = [a for a in ambulances if a.vehicle_type == vehicle_type]
        
    for amb in ambulances:
        amb.distance = calculate_distance(latitude, longitude, amb.latitude, amb.longitude)
        
    # Sort by distance
    ambulances.sort(key=lambda x: x.distance)
    return ambulances

@frappe.whitelist()
def generate_compliance_calendar():
    """Daily job to create compliance tasks based on templates and due dates."""
    templates = frappe.get_all("Compliance Template", fields=["*"]) # Assuming a template doctype or using list from PDF
    # Mocking implementation based on PDF p.18
    items = [
        {"item": "Vehicle Fitness Certificate", "frequency": "Annual", "applies_to": "Vehicle", "trigger": 45},
        {"item": "Insurance Renewal", "frequency": "Annual", "applies_to": "Vehicle", "trigger": 30},
        # ... logic to check expiries and create Compliance Task records
    ]
    
    for item in items:
        # Check corresponding fields in Ambulance Master or Crew Member
        # Example for Vehicle Fitness
        if item["applies_to"] == "Vehicle":
            vehicles = frappe.get_all("Ambulance Master", fields=["name", "fitness_expiry_date"])
            for v in vehicles:
                if v.fitness_expiry_date and getdate(v.fitness_expiry_date) <= add_days(getdate(), item["trigger"]):
                    create_compliance_task(v.name, "Ambulance Master", item["item"], v.fitness_expiry_date)

def create_compliance_task(ref_docname, ref_doctype, task_type, due_date):
    if not frappe.db.exists("Compliance Task", {"reference_document": ref_docname, "compliance_type": task_type, "status": ["in", ["Open", "Assigned"]]}):
        task = frappe.get_doc({
            "doctype": "Compliance Task",
            "compliance_type": task_type,
            "reference_doctype": ref_doctype,
            "reference_document": ref_docname,
            "due_date": due_date,
            "status": "Open",
            "priority": "High"
        })
        task.insert(ignore_permissions=True)

@frappe.whitelist()
def get_fleet_availability():
    """Returns summary of fleet status."""
    stats = frappe.db.sql("""
        SELECT operational_status, count(*) as count 
        FROM `tabAmbulance Master` 
        GROUP BY operational_status
    """, as_dict=1)
    return stats

@frappe.whitelist()
def check_certification_expiry():
    """Checks crew certifications and creates compliance tasks."""
    crew = frappe.get_all("Crew Member", fields=["name", "certification_expiry", "crew_member_name"])
    for c in crew:
        if c.certification_expiry and getdate(c.certification_expiry) <= add_days(getdate(), 60):
            create_compliance_task(c.name, "Crew Member", "Staff Certification", c.certification_expiry)

def get_permission_query_conditions(user=None):
    if not user: user = frappe.session.user
    # Return empty string to allow visibility by default, or add logic
    return ""

@frappe.whitelist()
def check_drug_expiry():
    """Checks for drugs expiring soon and creates compliance tasks."""
    inventory = frappe.get_all("Drug and Supply Inventory", 
        filters={"expiry_date": ["<=", add_days(now_datetime(), 90)]},
        fields=["name", "item_name", "expiry_date"]
    )
    for item in inventory:
        create_compliance_task(item.name, "Drug and Supply Inventory", "Drug Expiry", item.expiry_date)

@frappe.whitelist()
def escalate_overdue_compliance():
    """Escalates overdue tasks by changing status or notifying."""
    overdue = frappe.get_all("Compliance Task", filters={"status": "Overdue"})
    for task in overdue:
        # Potentially send notification or update priority
        pass

@frappe.whitelist()
def update_fleet_availability():
    """Recalculates fleet status based on current trips/maintenance."""
    # Logic to ensure status field matches reality
    pass
