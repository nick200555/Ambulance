from frappe.model.document import Document
import frappe
from frappe.utils import time_diff_in_seconds

class AmbulanceTripSheet(Document):
    def validate(self):
        self.calculate_times()
        self.calculate_distance()

    def calculate_times(self):
        """Calculates response time and total trip duration in minutes."""
        if self.departure_time and self.scene_arrival_time:
            diff = time_diff_in_seconds(self.scene_arrival_time, self.departure_time)
            self.response_time_min = round(diff / 60, 2)
        
        if self.departure_time and self.return_to_base_time:
            diff = time_diff_in_seconds(self.return_to_base_time, self.departure_time)
            self.total_trip_duration_min = round(diff / 60, 2)

    def calculate_distance(self):
        """Calculates distance covered based on odometer readings."""
        if self.odometer_start_km and self.odometer_end_km:
            if self.odometer_end_km >= self.odometer_start_km:
                self.distance_covered_km = self.odometer_end_km - self.odometer_start_km
            else:
                frappe.throw("Odometer End cannot be less than Odometer Start")
