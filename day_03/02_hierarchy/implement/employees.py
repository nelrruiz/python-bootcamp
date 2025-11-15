class Employee:
    """Class representation for employee data"""

    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.tasks = []
        print(f"Employee {self.name} created with ID {self.id}")

    def add_work(self, task):
        print(f"Added work {task} to {self.name}")
        self.tasks.append(task)

    def __repr__(self):
        return ""
class Recruiter(Employee):
    def recruit(self):
        # return Employee.add_work() + " " + f"Identified a shortlist."
        self.add_work("done recruiting - Identified a shortlist")
    
    # def offer(self):
    #     return super().add_work() + " " + f"Sent an offer to applicant"

class Developer(Employee):
    def code(self):
        # return Employee.add_work() + " " + f"MTP'd a code."
        self.add_work("MTP'd a code.")

class Manager(Employee):
    def manage(self):
        # return Employee.add_work() + " " + f"Checked in with an employee."
        self.add_work("Checked in with an employee.")

employee = Recruiter("JP", 123)

employee.recruit()

print(employee)