import csv
from tkinter import *
from Employee import *
global current_employee
global array_employees
employee_list = []
def load_employee_file_into_array():
    
    with open('employee.csv', newline='') as csvfile:
        employee_reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in employee_reader:
            new_employee = Employee(row[0],row[1], row[2], row[3])
            employee_list.append(new_employee)

def sort_by_forename():
    print('Sorting by forename')

def sort_by_surname():
    print('Sorting by surname')

def find_by_name():
    surname = txt_surname.get()

    found = False
    end_of_list = False
    employee_in_list = 0

    while (not found and not end_of_list):
        print(employee_in_list)
        if employee_list[employee_in_list].get_employee_surname() == surname:
            found = True
        elif employee_in_list == len(employee_list)-1:
            end_of_list = True
        else:
            employee_in_list += 1

    lst_results.insert(1,"Working")


def backup():
    print('Backing up')

def recover():
    print('Recovering')

load_employee_file_into_array()

form =Tk()
form.title('Employee Telephone Directory System')

lbl_surname = Label(form, text= 'Surname')
txt_surname = Entry(form,width=15)
lbl_surname.grid()
txt_surname.grid()


lbl_results = Label(form,text= 'Phone number')
lst_results = Listbox(form,height=7)
lbl_results.grid()
lst_results.grid()

btn_find_by_name = Button(form,text='Search', command=find_by_name)
btn_find_by_name.grid()

btn_sort_by_surname = Button(form,text='Sort Surname', command=sort_by_surname)
btn_sort_by_surname.grid()

btn_sort_by_forename = Button(form,text='Sort Forename', command=sort_by_forename)
btn_sort_by_forename.grid()

btn_backup = Button(form,text='Backup', command=backup)
btn_backup.grid()

btn_recover = Button(form,text='Recover', command=recover)
btn_recover.grid()



form.mainloop()

