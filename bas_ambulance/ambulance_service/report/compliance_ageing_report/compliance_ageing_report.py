import frappe

def execute(filters=None):
    columns = [
        {"label": "Task ID", "fieldname": "name", "fieldtype": "Link", "options": "Compliance Task", "width": 150},
        {"label": "Compliance Type", "fieldname": "compliance_type", "fieldtype": "Data", "width": 150},
        {"label": "Due Date", "fieldname": "due_date", "fieldtype": "Date", "width": 120},
        {"label": "Days Overdue", "fieldname": "days_overdue", "fieldtype": "Int", "width": 120},
        {"label": "Est. Penalty", "fieldname": "estimated_penalty", "fieldtype": "Currency", "width": 120},
        {"label": "Status", "fieldname": "status", "fieldtype": "Data", "width": 120}
    ]
    
    data = frappe.get_all("Compliance Task", 
        filters={"status": ["not in", ["Completed", "Waived"]]},
        fields=["name", "compliance_type", "due_date", "days_overdue", "estimated_penalty", "status"],
        order_by="days_overdue desc"
    )
    
    return columns, data
