import csv
from tkinter import *
from Employee import *
global current_employee
global array_employees
array_employees =[]
def load_employee_file_into_array():
    print('loading employee file')

def find_by_name():
    print('Finding employee')

def sort_by_forename():
    print('Sorting by forename')

def sort_by_surname():
    print('Sorting by surname')

def backup():
    print('Backing up')

def recover():
    print('Recovering')

form =Tk()
form.title('Employee Telephone Directory System')

lbl_surname = Label(form, text= 'Student Number')
txt_surname = Entry(form,width=15)
lbl_surname.grid()
txt_surname.grid()


lbl_results = Label(form,text= 'Results')
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

