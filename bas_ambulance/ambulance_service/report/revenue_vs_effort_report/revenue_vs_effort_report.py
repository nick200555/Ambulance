import frappe

def execute(filters=None):
    columns = [
        {"label": "Ambulance", "fieldname": "ambulance", "fieldtype": "Link", "options": "Ambulance Master", "width": 150},
        {"label": "Total Revenue", "fieldname": "revenue", "fieldtype": "Currency", "width": 150},
        {"label": "Km Covered", "fieldname": "total_km", "fieldtype": "Float", "width": 120},
        {"label": "Maintenance Cost", "fieldname": "maint_cost", "fieldtype": "Currency", "width": 150},
        {"label": "Profitability", "fieldname": "profit", "fieldtype": "Currency", "width": 150}
    ]
    
    data = frappe.db.sql("""
        SELECT 
            t.ambulance, 
            sum(b.net_amount) as revenue,
            sum(t.distance_covered_km) as total_km,
            (SELECT sum(total_cost) FROM `tabAmbulance Maintenance Record` WHERE ambulance = t.ambulance AND docstatus=1) as maint_cost,
            (sum(b.net_amount) - IFNULL((SELECT sum(total_cost) FROM `tabAmbulance Maintenance Record` WHERE ambulance = t.ambulance AND docstatus=1), 0)) as profit
        FROM 
            `tabAmbulance Trip Sheet` t
        JOIN 
            `tabAmbulance Bill` b ON b.trip_sheet = t.name AND b.docstatus = 1
        GROUP BY 
            t.ambulance
    """, as_dict=True)
    
    return columns, data
