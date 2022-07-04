import sys
import time
import datetime
import statistics

sys.path.append("C:\Magazyn\Code\workbench\week_7\secure-erp-python-sjafernik")
from model.hr import hr
from view import terminal as view

TODAY = datetime.date.today()


def list_employees():
    emp_list = []
    with open(hr.DATAFILE) as f:
        emp_raw = f.read().splitlines()
    for line in emp_raw:
        emp_list.append(line.split(";"))
    view.print_table(hr.HEADERS, emp_list)


def add_employee():
    new_emp = view.get_inputs(["Name", "Birthdate (yyyy-mm-dd)", "Department", "Clearance"])
    new_emp.insert(0, hr.util.generate_id())
    new_emp_str = ";".join(new_emp)

    with open(hr.DATAFILE) as f:
        emp_lines = f.read().splitlines()

    emp_lines_updated = []
    for item in emp_lines:
        emp_lines_updated.append(item)
    emp_lines_updated.append(new_emp_str)

    with open(hr.DATAFILE, "w") as f:
        for item in emp_lines_updated:
            f.write(item + "\n")
    
    print(f"{new_emp[1]} added")


def update_employee():
    list_employees()
    emp_to_delete = view.get_input("which employee would you to modify? (enter the ID)")
    new_emp = view.get_inputs(["Name", "Birthdate (yyyy-mm-dd)", "Department", "Clearance"])
    new_emp.insert(0, hr.util.generate_id())
    new_emp_str = ";".join(new_emp)

    with open(hr.DATAFILE) as f:
        emp_lines = f.read().splitlines()

    emp_lines_updated = []
    for item in emp_lines:
        if item.split(";")[0] != emp_to_delete:
            emp_lines_updated.append(item)
    emp_lines_updated.append(new_emp_str)

    with open(hr.DATAFILE, "w") as f:
        for item in emp_lines_updated:
            f.write(item + "\n")
    
    print(f"{new_emp[1]} modified")


def delete_employee(): #NOT FINISHED
    list_employees()
    emp_to_delete = view.get_input("which employee would you to delete? (enter the ID)")

    with open(hr.DATAFILE) as f:
        emp_lines = f.read().splitlines()

    emp_lines_updated = []
    for item in emp_lines:
        if item.split(";")[0] != emp_to_delete:
            emp_lines_updated.append(item)

    with open(hr.DATAFILE, "w") as f:
        for item in emp_lines_updated:
            f.write(item + "\n")
    
    print(f"{emp_to_delete} deleted")


def get_oldest_and_youngest():
    oldest = []
    youngest = []
    result = [[], []]
    temp = []

    with open(hr.DATAFILE) as f:
        emp_lines = f.read().splitlines()
    for index, item in enumerate(emp_lines):
        if oldest == []:
            oldest.append(item)
        elif time.strptime(item.split(";")[2], "%Y-%m-%d") == time.strptime(oldest[0].split(";")[2], "%Y-%m-%d"):
            oldest.append(item)
        elif time.strptime(item.split(";")[2], "%Y-%m-%d") < time.strptime(oldest[0].split(";")[2], "%Y-%m-%d"):
            oldest = []
            oldest.append(item)
    for employee in oldest:
        for item in employee.split(";"):
            temp.append(item)
        result.append(temp)
        temp = []

    for index, item in enumerate(emp_lines):
        if youngest == []:
            youngest.append(item)
        elif time.strptime(item.split(";")[2], "%Y-%m-%d") == time.strptime(youngest[0].split(";")[2], "%Y-%m-%d"):
            youngest.append(item)
        elif time.strptime(item.split(";")[2], "%Y-%m-%d") > time.strptime(youngest[0].split(";")[2], "%Y-%m-%d"):
            youngest = []
            youngest.append(item)
    for employee in youngest:
        for item in employee.split(";"):
            temp.append(item)
        result.append(temp)
        temp = []

    view.print_table(hr.HEADERS, result)


def get_average_age():
    age = []
    with open(hr.DATAFILE) as f:
        emp_lines = f.read().splitlines()
    for item in emp_lines:
        age.append(datetime.date.today().year - datetime.datetime.strptime(item.split(";")[2], "%Y-%m-%d").year)
    view.print_general_results(statistics.mean(age), "Average age")


def next_birthdays():
    result = []
    temp_line = []

    with open(hr.DATAFILE) as f:
        emp_lines = f.read().splitlines()
    for item in emp_lines:
        birthdate_str = str(datetime.datetime.strptime(item.split(";")[2], "%Y-%m-%d").date())
        birthday = datetime.datetime.strptime(str(TODAY)[0:5] + birthdate_str[5:10], "%Y-%m-%d").date()
        days_to_birthday = (birthday - TODAY).days
        if  0 <= days_to_birthday < 15:
            for item_listed in item.split(";"):
                temp_line.append(item_listed)
            result.append(temp_line)
            temp_line = []
    view.print_table(hr.HEADERS, result)


def count_employees_with_clearance():
    level = view.get_input("Choose minimal clearance level: ")
    result = []
    temp = []
    with open(hr.DATAFILE) as f:
        emp_lines = f.read().splitlines()
    for item in emp_lines:
        if int(item.split(";")[4]) >= int(level):
            for item_listed in item.split(";"):
                temp.append(item_listed)
            result.append(temp)
            temp = []

    view.print_table(hr.HEADERS, result)


def count_employees_per_department():
    department = view.get_input("Choose department: ")
    result = 0
    with open(hr.DATAFILE) as f:
        emp_lines = f.read().splitlines()
    for item in emp_lines:
        if item.split(";")[3].lower() == department.lower():
            result += 1
    view.print_general_results(result, f"Number of employees in {department}: ")


def run_operation(option):
    if option == 1:
        list_employees()
    elif option == 2:
        add_employee()
    elif option == 3:
        update_employee()
    elif option == 4:
        delete_employee()
    elif option == 5:
        get_oldest_and_youngest()
    elif option == 6:
        get_average_age()
    elif option == 7:
        next_birthdays()
    elif option == 8:
        count_employees_with_clearance()
    elif option == 9:
        count_employees_per_department()
    elif option == 0:
        return
    else:
        raise KeyError("There is no such option.")


def display_menu():
    options = ["Back to main menu",
               "List employees",
               "Add new employee",
               "Update employee",
               "Remove employee",
               "Oldest and youngest employees",
               "Employees average age",
               "Employees with birthdays in the next two weeks",
               "Employees with clearance level",
               "Employee numbers by department"]
    view.print_menu("Human resources", options)


def menu():
    operation = None
    while operation != '0':
        display_menu()
        try:
            operation = view.get_input("Select an operation")
            run_operation(int(operation))
        except KeyError as err:
            view.print_error_message(err)
