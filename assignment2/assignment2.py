# Task 2: Read a CSV File
import csv
import traceback

def read_employees():
    employees_data = {"fields": [], "rows": []}

    try:
        with open('../csv/employees.csv', 'r') as file:
            reader = csv.reader(file)
            employees_data["fields"] = next(reader)
            employees_data["rows"] = []
            while True:
                try:
                    row=next(reader)
                    employees_data['rows'].append(row)
                except StopIteration:
                    break
        return employees_data
                
    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = list()
        for trace in trace_back:
            stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
        print(f"Exception type: {type(e).__name__}")
        message = str(e)
        if message:
            print(f"Exception message: {message}")
        print(f"Stack trace: {stack_trace}")


employees = read_employees()

# Task 3 : Find the Column Index
def column_index(column_name):
    return employees["fields"].index(column_name)
employee_id_column = column_index("employee_id")

# Task 4 : Find the Employee First Name
def first_name(row_number):
    index = column_index("first_name")
    return employees["rows"][row_number][index]

# Task 5 : Find the EMployee: a Function in a Function
def employee_find(employee_id):
    def employee_match(row):
        return int(row[employee_id_column]) == employee_id
    
    matches = list(filter(employee_match, employees["rows"]))
    return matches

# Task 6 : Find the Employee with Lambda
def employee_find_2(employee_id):
   matches = list(filter(lambda row : int(row[employee_id_column]) == employee_id , employees["rows"]))
   return matches

# Task 7 : Sort the Rows by last_name Using a Lambda
def sort_by_last_name():
    last_name_index = column_index("last_name")
    employees['rows'].sort(key=lambda row: row[last_name_index])
    return employees["rows"]

# Task 8 : Create a dict for an Employee
def employee_dict(row):
    employee_data = {}
    for i, field in enumerate(employees["fields"]):
        if field != "employee_id":
            employee_data[field] = row[i]
    return employee_data

# Task 9 : A dict of dicts, for All Employees
def all_employees_dict():
    result = {}
    for row in employees["rows"]:
        employee_id = row[column_index("employee_id")]
        result[employee_id] = employee_dict(row)
    return result

# Task 10 : Use the os Module
import os

def get_this_value():
    return os.getenv('THISVALUE')

# Task 11 :  Creating Your Own Module
import custom_module

def set_that_secret(new_secret):
    custom_module.set_secret(new_secret)

# Task 12 : Create minutes_set
def read_minutes_file(filepath):
    minutes_data = {"fields": [], "rows": []}
    try:
         with open(filepath, 'r') as file:
            reader = csv.reader(file)
            minutes_data["fields"] = next(reader)
            minutes_data["rows"] = []
            while True:
                try:
                    row=next(reader)
                    minutes_data['rows'].append(tuple(row))
                except StopIteration:
                    break
    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = list()
        for trace in trace_back:
            stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
        print(f"Exception type: {type(e).__name__}")
        message = str(e)
        if message:
            print(f"Exception message: {message}")
        print(f"Stack trace: {stack_trace}")
    return minutes_data

def read_minutes():
    minutes1 = read_minutes_file('../csv/minutes1.csv')
    minutes2 = read_minutes_file('../csv/minutes2.csv')
    return minutes1, minutes2

minutes1, minutes2 = read_minutes()

# Task 13 : Create minutes_set
def create_minutes_set():
    set1 = set(minutes1["rows"])
    set2 = set(minutes2["rows"])
    combine_sets = set1.union(set2)
    return combine_sets

minutes_set = create_minutes_set()

# Task 14 : Convert to datetime
from datetime import datetime

def create_minutes_list():
    minutes_list_all = list(minutes_set)
    converted = list(map(lambda j: (j[0], datetime.strptime(j[1], "%B %d, %Y")), minutes_list_all))
    return converted

minutes_list = create_minutes_list()

# Task 15 : Write Out Sorted List
def write_sorted_list():
    sorted_minutes = sorted(minutes_list, key= lambda j: j[1])
    converted_list = list(map(lambda j: (j[0], j[1].strftime("%B %d, %Y")), sorted_minutes))

    try: 
        with open('minutes.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer. writerow(minutes1["fields"])
            writer. writerows(converted_list)
    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = list()
        for trace in trace_back:
            stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
        print(f"Exception type: {type(e).__name__}")
        message = str(e)
        if message:
            print(f"Exception message: {message}")
        print(f"Stack trace: {stack_trace}")

    return converted_list
sorted_minutes_list = write_sorted_list()
