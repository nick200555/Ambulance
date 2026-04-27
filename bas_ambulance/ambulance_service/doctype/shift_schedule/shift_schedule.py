from frappe.model.document import Document
import frappe

class ShiftSchedule(Document):
    def validate(self):
        self.actual_crew_count = len(self.crew_assignments or [])
