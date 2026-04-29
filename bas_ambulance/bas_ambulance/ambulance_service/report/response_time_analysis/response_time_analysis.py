import frappe

def execute(filters=None):
    columns = get_columns()
    data = get_data(filters)
    return columns, data

def get_columns():
    return [
        {"label": "Trip ID", "fieldname": "name", "fieldtype": "Link", "options": "Ambulance Trip Sheet", "width": 120},
        {"label": "Station", "fieldname": "home_station", "fieldtype": "Link", "options": "Ambulance Station", "width": 120},
        {"label": "Ambulance", "fieldname": "ambulance", "fieldtype": "Link", "options": "Ambulance Master", "width": 120},
        {"label": "Emergency Type", "fieldname": "nature_of_emergency", "fieldtype": "Data", "width": 120},
        {"label": "Priority", "fieldname": "triage_priority", "fieldtype": "Data", "width": 100},
        {"label": "Response Time (min)", "fieldname": "response_time_min", "fieldtype": "Float", "width": 120}
    ]

def get_data(filters):
    query = """
        SELECT 
            t.name, 
            a.home_base_station as home_station, 
            t.ambulance, 
            p.nature_of_emergency, 
            p.triage_priority, 
            t.response_time_min
        FROM 
            `tabAmbulance Trip Sheet` t
        LEFT JOIN 
            `tabAmbulance Master` a ON t.ambulance = a.name
        LEFT JOIN 
            `tabPatient Call Record` p ON t.patient_call_record = p.name
        WHERE 
            t.docstatus = 1
    """
    
    if filters.get("from_date") and filters.get("to_date"):
        query += " AND t.departure_time BETWEEN '{0}' AND '{1}'".format(filters.get("from_date"), filters.get("to_date"))
        
    return frappe.db.sql(query, as_dict=True)
