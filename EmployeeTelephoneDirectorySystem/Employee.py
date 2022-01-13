class Employee(object):
    """Create an object to hold employee details """

    def __init__(self,employee_forename,employee_surname,extention_number,mobile_number):
        self.employee_forename = employee_forename
        self.employee_surname = employee_surname
        self.extention_number = extention_number
        self.mobile_number = mobile_number
        
    def get_employee_forename(self):
        return self.employee_forename

    def get_employee_surname(self):
        return self.employee_surname

    def get_extention_number(self):
        return self.extention_number

    def get_mobile_number(self):
        return self.mobile_number

    

