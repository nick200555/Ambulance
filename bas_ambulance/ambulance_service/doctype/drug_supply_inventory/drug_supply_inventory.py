from frappe.model.document import Document
import frappe
from frappe.utils import getdate, nowdate

class DrugSupplyInventory(Document):
    def validate(self):
        self.update_stock_status()

    def update_stock_status(self):
        """Updates stock status based on quantity and expiry."""
        if self.expiry_date and getdate(self.expiry_date) < getdate(nowdate()):
            self.stock_status = "Expired"
        elif self.quantity_in_stock <= 0:
            self.stock_status = "Out of Stock"
        elif self.quantity_in_stock <= (self.minimum_stock_level or 0):
            self.stock_status = "Low Stock"
        else:
            self.stock_status = "Adequate"
