import frappe
from frappe import _
import math

def calculate_distance(lat1, lon1, lat2, lon2):
    """Haversine formula to calculate distance between two points on Earth."""
    if not (lat1 and lon1 and lat2 and lon2):
        return 0
    
    R = 6371 # Earth radius in km
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat / 2) * math.sin(dlat / 2) + \
        math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * \
        math.sin(dlon / 2) * math.sin(dlon / 2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return R * c

def calculate_eta(distance_km, avg_speed_kmh=40):
    """Rough ETA calculation based on distance and average city speed."""
    if distance_km <= 0:
        return 0
    return math.ceil((distance_km / avg_speed_kmh) * 60)

def on_trip_submit(doc, method=None):
    """Action on Ambulance Trip Sheet submission."""
    # Update Ambulance Status to Available
    if doc.ambulance:
        frappe.db.set_value("Ambulance Master", doc.ambulance, "operational_status", "Available")
        frappe.db.set_value("Ambulance Master", doc.ambulance, "last_service_date", doc.hospital_arrival_time)
    
    # Update Call Record Status
    if doc.patient_call_record:
        frappe.db.set_value("Patient Call Record", doc.patient_call_record, "call_status", "Completed")

def on_trip_cancel(doc, method=None):
    """Action on Ambulance Trip Sheet cancellation."""
    if doc.ambulance:
        frappe.db.set_value("Ambulance Master", doc.ambulance, "operational_status", "Available")

def update_ambulance_maintenance_status(doc, method=None):
    """When maintenance is submitted, update vehicle status."""
    if doc.maintenance_status == "Completed":
        frappe.db.set_value("Ambulance Master", doc.ambulance, "operational_status", "Available")
        frappe.db.set_value("Ambulance Master", doc.ambulance, "last_service_date", doc.completion_date)
    elif doc.maintenance_status == "In Progress":
        frappe.db.set_value("Ambulance Master", doc.ambulance, "operational_status", "Under Maintenance")

def get_billing_summary(trip_id):
    """Calculates billing components for a trip."""
    # Mock logic: Base Charge + Km Charge + Equipment Charge
    trip = frappe.get_doc("Ambulance Trip Sheet", trip_id)
    base_charge = 500
    km_charge = (trip.distance_covered or 0) * 20
    
    # Sum up procedures
    procedure_charge = sum([p.charge for p in trip.procedures_performed if hasattr(p, 'charge')])
    
    return {
        "base_charge": base_charge,
        "km_charge": km_charge,
        "procedure_charge": procedure_charge,
        "total": base_charge + km_charge + procedure_charge
    }
