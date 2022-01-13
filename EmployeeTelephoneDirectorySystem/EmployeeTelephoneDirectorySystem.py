import csv
from tkinter import *
from Employee import *
global current_employee
global array_employees
array_employees =[]
def load_employee_file_into_array():
    print('loading employee file')
