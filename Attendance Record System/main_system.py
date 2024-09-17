import os
from organization_data import Organization
from admin_data import Admin
from manager_data import Manager
from employee_data import Employee

organization = Organization()
admin = Admin()
manager = Manager()
employee = Employee()


class MainSystem:
    def __init__(self):
        self.__employee_options = """Welcome Employee to the system.\n
1. Show all employees.
2. Show Attendance of all employees.
3. Show attendance of specific employee."""

    def authenticate(self, designation, username, password):
        if designation == "admin":
            admin.login_status(username=username, password=password)
        elif designation == "employee":
            return_value = organization.authenticate(uname=username, word=password)
            print(return_value)
            if return_value[0] == 1:
                manager.set_my_details(return_value[1])
                manager.show_options()
            elif return_value[0] == 0:
                employee.set_employee_details(return_value[1])
                employee.show_options()
            else:
                print("You have entered wrong credentials. Sorry Login Failed")

