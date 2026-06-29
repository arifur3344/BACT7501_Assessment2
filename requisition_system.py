# Counter to generate unique Requisition ID 
requisition_counter = 0

class Requisition:
    def __init__(self, date, staff_id, staff_name):
        global requisition_counter
        # Variables inside the class
        self.date = date
        self.staff_id = staff_id
        self.staff_name = staff_name
        
        # Unique ID assignme  nt
        requisition_counter = requisition_counter + 1
        self.requisition_id = requisition_counter + 10000
        
        self.list_of_items = []
        self.total = 0
        self.status = "Pending"
        self.approval_reference = "Not available"
