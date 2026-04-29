from frappe.model.document import Document
import frappe
from frappe.utils import date_diff, getdate, nowdate

class ComplianceTask(Document):
    def validate(self):
        self.calculate_penalty()

    def calculate_penalty(self):
        """Calculates days overdue and estimated penalty."""
        if self.status not in ["Completed", "Waived"] and self.due_date:
            today = nowdate()
            if getdate(today) > getdate(self.due_date):
                self.days_overdue = date_diff(today, self.due_date)
                if self.penalty_per_day:
                    self.estimated_penalty = self.days_overdue * self.penalty_per_day
                self.status = "Overdue"
            else:
                self.days_overdue = 0
                self.estimated_penalty = 0
