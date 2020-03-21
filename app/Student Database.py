
from tkinter import*
import tkinter.messagebox
import Student_Database_Backend


class Student:

    def __init__(self, root):
        self.root = root
        self.root.title("Student Database Management System")
        self.root.geometry("1350x750+0+0")
        self.root.config(bg="royal blue")

        std_id = StringVar()
        std_name = StringVar()
        std_surname = StringVar()
        std_dob = StringVar()
        std_age = StringVar()
        std_gender = StringVar()
        std_address = StringVar()
        std_mobile = StringVar()

        # ================================ Function ==================================

        def iExit():
            iExit = tkinter.messagebox.askyesno("Students Database Management Systems", "Confirm if you want to exit")
            if iExit:
                root.destroy()
                return

        def clear_data():
            self.txtStd_Id.delete(0, END)
            self.txtStd_fn.delete(0, END)
            self.txtStd_sna.delete(0, END)
            self.txtStd_dob.delete(0, END)
            self.txtStd_age.delete(0, END)
            self.txtStd_gender.delete(0, END)
            self.txtStd_adr.delete(0, END)
            self.txtStd_mobile.delete(0, END)

        def add_data():
            if len(std_id.get()) != 0:
                Student_Database_Backend.add_std_rec(std_id.get(), std_name.get(), std_surname.get(),\
                std_dob.get(), std_age.get(), std_gender.get(), std_address.get(), std_mobile.get())

                student_list.delete(0, END)
                student_list.insert(END, (std_id.get(), std_name.get(), std_surname.get(),\
                std_dob.get(), std_age.get(), std_gender.get(), std_address.get(), std_mobile.get()))

        def display_data():
            student_list.delete(0, END)
            for row in Student_Database_Backend.view_data():
                student_list.insert(END, row, str(""))

        def student_rec(event):
            global sd
            search_std = student_list.curselection()[0]
            sd = student_list.get(search_std)

            self.txtStd_Id.delete(0, END)
            self.txtStd_Id.insert(END, sd[1])
            self.txtStd_fn.delete(0, END)
            self.txtStd_fn.insert(END, sd[2])
            self.txtStd_sna.delete(0, END)
            self.txtStd_sna.insert(END, sd[3])
            self.txtStd_dob.delete(0, END)
            self.txtStd_dob.insert(END, sd[4])
            self.txtStd_age.delete(0, END)
            self.txtStd_age.insert(END, sd[5])
            self.txtStd_gender.delete(0, END)
            self.txtStd_gender.insert(END, sd[6])
            self.txtStd_adr.delete(0, END)
            self.txtStd_adr.insert(END, sd[7])
            self.txtStd_mobile.delete(0, END)
            self.txtStd_mobile.insert(END, sd[8])

        def delete_data():
            if len(std_id.get()) != 0:
                Student_Database_Backend.delete_rec(sd[0])
                clear_data()
                display_data()

        def search_data():
            student_list.delete(0, END)
            for row in Student_Database_Backend.search_data(std_id.get(), std_name.get(), std_surname.get(),\
                std_dob.get(), std_age.get(), std_gender.get(), std_address.get(), std_mobile.get()):
                student_list.insert(END, row, str(""))

        def update_data():
            if len(std_id.get()) != 0:
                Student_Database_Backend.delete_rec(sd[0])
            if len(std_id.get()) != 0:
                Student_Database_Backend.add_std_rec(std_id.get(), std_name.get(), std_surname.get(),\
                std_dob.get(), std_age.get(), std_gender.get(), std_address.get(), std_mobile.get())
                student_list.delete(0, END)
                student_list.insert(END, (std_id.get(), std_name.get(), std_surname.get(),\
                std_dob.get(), std_age.get(), std_gender.get(), std_address.get(), std_mobile.get()))
        # ================================ Frames ======================================

        main_frame = Frame(self.root, bg="royal blue")
        main_frame.grid()

        tit_frame = Frame(main_frame, bd=2, padx=200, pady=20, bg="limegreen", relief=RIDGE)
        tit_frame.pack(side=TOP)

        self.lblTit = Label(tit_frame, font=('arial', 30, 'bold'), text="Student Database Management Systems", bg="limegreen")
        self.lblTit.grid()

        button_frame = Frame(main_frame, bd=2, width=1350, height=70, padx=18, pady=10, bg="dodgerblue", relief=RIDGE)
        button_frame.pack(side=BOTTOM)

        data_frame = Frame(main_frame, bd=1, width=1300, height=400, padx=20, pady=20, bg="Gray", relief=RIDGE)
        data_frame.pack(side=BOTTOM)

        data_frame_left = LabelFrame(data_frame, bd=1, width=1000, height=600, padx=20, bg="orange", relief=RIDGE,
                                     font=('arial', 20, 'bold'), text="Student Info\n")
        data_frame_left.pack(side=LEFT)

        data_frame_right = LabelFrame(data_frame, bd=1, width=450, height=300, padx=31, pady=3, bg="tomato", relief=RIDGE,
                                      font=('arial', 20, 'bold'), text="Student Info\n")
        data_frame_right.pack(side=RIGHT)

        # ================================ Labels and Entry Widget ======================================
        # Student ID label
        self.lblStd_Id = Label(data_frame_left, font=('arial', 20, 'bold'), text="Student ID:", padx=2, pady=2, bg="orange")
        self.lblStd_Id .grid(row=0, column=0, sticky=W)
        self.txtStd_Id = Entry(data_frame_left, font=('arial', 20, 'bold'), textvariable=std_id, width=39, bg="silver")
        self.txtStd_Id.grid(row=0, column=1)

        # First name label
        self.lblStd_fn = Label(data_frame_left, font=('arial', 20, 'bold'), text="Firstname:", padx=2, pady=2,  bg="orange")
        self.lblStd_fn.grid(row=1, column=0, sticky=W)
        self.txtStd_fn = Entry(data_frame_left, font=('arial', 20, 'bold'), textvariable=std_name, width=39, bg="silver")
        self.txtStd_fn.grid(row=1, column=1)

        # Surname label
        self.lblStd_sna = Label(data_frame_left, font=('arial', 20, 'bold'), text="Surname:", padx=2, pady=2, bg="orange")
        self.lblStd_sna.grid(row=2, column=0, sticky=W)
        self.txtStd_sna = Entry(data_frame_left, font=('arial', 20, 'bold'), textvariable=std_surname, width=39, bg="silver")
        self.txtStd_sna.grid(row=2, column=1)

        # Date of birth label
        self.lblStd_dob = Label(data_frame_left, font=('arial', 20, 'bold'), text="Date of Birth:", padx=2, pady=2, bg="orange")
        self.lblStd_dob.grid(row=3, column=0, sticky=W)
        self.txtStd_dob = Entry(data_frame_left, font=('arial', 20, 'bold'), textvariable=std_dob, width=39, bg="silver")
        self.txtStd_dob.grid(row=3, column=1)

        # Age label
        self.lblStd_age = Label(data_frame_left, font=('arial', 20, 'bold'), text="Age:", padx=2, pady=2, bg="orange")
        self.lblStd_age.grid(row=4, column=0, sticky=W)
        self.txtStd_age = Entry(data_frame_left, font=('arial', 20, 'bold'), textvariable=std_age, width=39, bg="silver")
        self.txtStd_age.grid(row=4, column=1)

        # Gender label
        self.lblStd_gender = Label(data_frame_left, font=('arial', 20, 'bold'), text="Gender:", padx=2, pady=2, bg="orange")
        self.lblStd_gender.grid(row=5, column=0, sticky=W,)
        self.txtStd_gender = Entry(data_frame_left, font=('arial', 20, 'bold'), textvariable=std_gender, width=39, bg="silver")
        self.txtStd_gender.grid(row=5, column=1)

        # Address label
        self.lblStd_adr = Label(data_frame_left, font=('arial', 20, 'bold'), text="Address:", padx=2, pady=2, bg="orange")
        self.lblStd_adr.grid(row=6, column=0, sticky=W)
        self.txtStd_adr = Entry(data_frame_left, font=('arial', 20, 'bold'), textvariable=std_address, width=39, bg="silver")
        self.txtStd_adr.grid(row=6, column=1)

        # Mobile label
        self.lblStd_mobile = Label(data_frame_left, font=('arial', 20, 'bold'), text="Mobile No.:", padx=2, pady=2, bg="orange")
        self.lblStd_mobile.grid(row=7, column=0, sticky=W)
        self.txtStd_mobile = Entry(data_frame_left, font=('arial', 20, 'bold'), textvariable=std_mobile, width=39, bg="silver")
        self.txtStd_mobile.grid(row=7, column=1)

        # =================== ListBox & ScrollBar Widget ========================

        scrollbar = Scrollbar(data_frame_right)
        scrollbar.grid(row=0, column=1, sticky='ns')

        student_list = Listbox(data_frame_right, width=41, height=16, font=('arial', 12, 'bold'), yscrollcommand=scrollbar.set, bg="silver" )
        student_list.bind('<<ListboxSelect>>', student_rec)
        student_list.grid(row=0, column=0, padx=8)
        scrollbar.config(command=student_list.yview)

        # ================= Button Widget =============================

        self.btn_add_data = Button(button_frame, text='Add New', font=('arial', 20, 'bold'), height=1, width=10, bd=4, bg="deepskyblue", command=add_data)
        self.btn_add_data.grid(row=0, column=0)

        self.btn_display_data = Button(button_frame, text='Display', font=('arial', 20, 'bold'), height=1, width=10, bd=4, bg="deepskyblue", command=display_data)
        self.btn_display_data.grid(row=0, column=1)

        self.btn_clear_data = Button(button_frame, text='Clear', font=('arial', 20, 'bold'), height=1, width=10, bd=4, bg="deepskyblue", command=clear_data)
        self.btn_clear_data.grid(row=0, column=2)

        self.btn_delete_data = Button(button_frame, text='Delete', font=('arial', 20, 'bold'), height=1, width=10, bd=4, bg="deepskyblue", command=delete_data)
        self.btn_delete_data.grid(row=0, column=3)

        self.btn_search_data = Button(button_frame, text='Search', font=('arial', 20, 'bold'), height=1, width=10, bd=4, bg="deepskyblue", command=search_data)
        self.btn_search_data.grid(row=0, column=4)

        self.btn_update_data = Button(button_frame, text='Update', font=('arial', 20, 'bold'), height=1, width=10, bd=4, bg="deepskyblue", command=update_data)
        self.btn_update_data.grid(row=0, column=5)

        self.btn_exit = Button(button_frame, text='Exit', font=('arial', 20, 'bold'), height=1, width=10, bd=4, bg="deepskyblue", command=iExit)
        self.btn_exit.grid(row=0, column=6)


if __name__ == '__main__':
    root = Tk()
    application = Student(root)
    root.mainloop()
