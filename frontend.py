from tkinter import *
import backend as bk
from tkinter.messagebox import *


def get_selected_row(event):
    global selected_row
    index = item_list.curselection()[0]
    selected_row = item_list.get(index)
    e_date.delete(0, END)
    e_date.insert(END, selected_row[1])
    e_earning.delete(0, END)
    e_earning.insert(END, selected_row[2])
    e_exe.delete(0, END)
    e_exe.insert(END, selected_row[3])
    e_std.delete(0, END)
    e_std.insert(END, selected_row[4])
    e_dit.delete(0, END)
    e_dit.insert(END, selected_row[5])
    e_pyt.delete(0, END)
    e_pyt.insert(END, selected_row[6])


def delete_command():
    message = bk.delete(selected_row[0])
    showinfo('Delete', message)
    e_date.delete(0, END)

    e_earning.delete(0, END)

    e_exe.delete(0, END)

    e_std.delete(0, END)

    e_dit.delete(0, END)

    e_pyt.delete(0, END)

    view_command()


def view_command():
    item_list.delete(0, END)
    for row in bk.view():
        item_list.insert(END, row)


def add_command():
    msg = bk.insert(date_text.get(), earning_text.get(), exe_text.get(), std_text.get(), dit_text.get(), pyt_text.get())
    showinfo('Add', msg)
    view_command()


def search_command():
    item_list.delete(0, END)
    for row in bk.search(date_text.get(), earning_text.get(), exe_text.get(), std_text.get(), dit_text.get(),
                         pyt_text.get()):
        item_list.insert(END, row)


win = Tk()
win.title("My Routine DataBase")

l1 = Label(win, text='Date')
l1.grid(row=0, column=0)
l2 = Label(win, text='Earnings')
l2.grid(row=1, column=0)
l3 = Label(win, text='Exercise')
l3.grid(row=2, column=0)
l4 = Label(win, text='Study')
l4.grid(row=3, column=0)
l5 = Label(win, text='Diet')
l5.grid(row=4, column=0)
l6 = Label(win, text='Python')
l6.grid(row=5, column=0)

item_list = Listbox(win, height=15, width=40)
item_list.grid(row=0, column=2, rowspan=10, columnspan=6)
item_list.bind('<<ListboxSelect>>', get_selected_row)

sb = Scrollbar(win)
sb.grid(row=0, column=8)

date_text = StringVar()
e_date = Entry(win, textvariable=date_text)
e_date.grid(row=0, column=1)

earning_text = StringVar()
e_earning = Entry(win, textvariable=earning_text)
e_earning.grid(row=1, column=1)

exe_text = StringVar()
e_exe = Entry(win, textvariable=exe_text)
e_exe.grid(row=2, column=1)

std_text = StringVar()
e_std = Entry(win, textvariable=std_text)
e_std.grid(row=3, column=1)

dit_text = StringVar()
e_dit = Entry(win, textvariable=dit_text)
e_dit.grid(row=4, column=1)

pyt_text = StringVar()
e_pyt = Entry(win, textvariable=pyt_text)
e_pyt.grid(row=5, column=1)

btn_add = Button(win, text='Add', command=add_command, width=12)
btn_add.grid(row=10, column=0, pady=5)

btn_search = Button(win, text='Search', command=search_command, width=12)
btn_search.grid(row=10, column=1, pady=5)

btn_delete = Button(win, text='Delete', command=delete_command, width=12)
btn_delete.grid(row=10, column=2, pady=5)

btn_view = Button(win, text='View', command=view_command, width=12)
btn_view.grid(row=10, column=3, pady=5)

win.mainloop()
