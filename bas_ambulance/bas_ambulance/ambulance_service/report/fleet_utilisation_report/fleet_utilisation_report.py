import frappe

def execute(filters=None):
    columns = [
        {"label": "Ambulance", "fieldname": "name", "fieldtype": "Link", "options": "Ambulance Master", "width": 150},
        {"label": "Total Trips", "fieldname": "total_trips", "fieldtype": "Int", "width": 100},
        {"label": "Total KM", "fieldname": "total_km", "fieldtype": "Float", "width": 120},
        {"label": "Utilisation %", "fieldname": "utilisation", "fieldtype": "Percent", "width": 120},
        {"label": "Downtime (Hrs)", "fieldname": "total_downtime", "fieldtype": "Float", "width": 120}
    ]
    
    data = frappe.db.sql("""
        SELECT 
            a.name, 
            count(t.name) as total_trips, 
            sum(t.distance_covered_km) as total_km,
            (count(t.name) / 30.0) * 100 as utilisation,
            sum(m.downtime_hours) as total_downtime
        FROM 
            `tabAmbulance Master` a
        LEFT JOIN 
            `tabAmbulance Trip Sheet` t ON t.ambulance = a.name AND t.docstatus = 1
        LEFT JOIN 
            `tabAmbulance Maintenance Record` m ON m.ambulance = a.name AND m.docstatus = 1
        GROUP BY 
            a.name
    """, as_dict=True)
    
    return columns, data
