from . import __version__ as app_version

app_name = "bas_ambulance"
app_title = "BAS Ambulance Service"
app_publisher = "BAS"
app_description = "Ambulance Service Management Module for ERPNext"
app_email = "info@bas.com"                     # ✅ Fixed: plain string
app_license = "Proprietary"
app_icon = "ambulance"                         # optional
app_color = "#e74c3c"                          # optional

# Fixtures
fixtures = [
    {"doctype": "Role", "filters": [["name", "in", ["Fleet Manager", "Dispatch Officer", "Billing Executive", "Compliance Officer", "Call Centre Agent", "Paramedic"]]]},
    "Custom Field",
    "Property Setter",
    "Workflow",
    "Workflow State",
    # "Workflow Action",  # ✅ Removed: deprecated/runtime doctype in Frappe v14+
    "Print Format",
    "Notification"
]

# Scheduler Events
scheduler_events = {
    "daily": [
        "bas_ambulance.api.generate_compliance_calendar",
        "bas_ambulance.api.check_certification_expiry",
        "bas_ambulance.api.check_drug_expiry",
        "bas_ambulance.api.escalate_overdue_compliance"
    ],
    "hourly": [
        "bas_ambulance.api.update_fleet_availability"
    ]
}

# Document Events
doc_events = {
    "Ambulance Trip Sheet": {
        "on_submit": "bas_ambulance.utils.on_trip_submit",
        "on_cancel": "bas_ambulance.utils.on_trip_cancel"
    },
    "Ambulance Maintenance Record": {
        "on_submit": "bas_ambulance.utils.update_ambulance_maintenance_status"
    }
}

# Permissions
permission_query_conditions = {
    "Ambulance Master": "bas_ambulance.api.get_permission_query_conditions",
}
