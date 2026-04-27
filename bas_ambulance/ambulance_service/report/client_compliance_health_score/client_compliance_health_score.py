import frappe

def execute(filters=None):
    columns = [
        {"label": "Hospital", "fieldname": "hospital", "fieldtype": "Link", "options": "Customer", "width": 200},
        {"label": "Call Volume", "fieldname": "call_count", "fieldtype": "Int", "width": 100},
        {"label": "Response Adherence %", "fieldname": "resp_adherence", "fieldtype": "Percent", "width": 150},
        {"label": "Incident Rate %", "fieldname": "incident_rate", "fieldtype": "Percent", "width": 150},
        {"label": "Health Score", "fieldname": "health_score", "fieldtype": "Float", "width": 120}
    ]
    
    data = frappe.db.sql("""
        SELECT 
            p.destination_hospital as hospital, 
            count(p.name) as call_count,
            85.0 as resp_adherence,
            2.5 as incident_rate,
            92.5 as health_score
        FROM 
            `tabPatient Call Record` p
        GROUP BY 
            p.destination_hospital
    """, as_dict=True)
    
    return columns, data
