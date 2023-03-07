from tkinter import *
import sqlite3
import tkinter.ttk as ttk
import tkinter.messagebox
import tkinter.messagebox as tkMessageBox


# DEVELOPED BY: RAGHEIL L. ATACADOR
# SECTION: BSIT - IT1R6


root = Tk()
root.title("DYNAMIC Solutions SCHOOL, INC.")
width = 1400
height = 500
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width / 2) - (width / 2)
y = (screen_height / 2) - (height / 2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(TRUE, TRUE)
root.config(bg="GRAY")

# ============================VARIABLES===================================
NUMBER = StringVar()
SNAME = StringVar()
GENDER = StringVar(root, "0")
COURSE = StringVar()
SUBJECT = StringVar()
PRELIM = StringVar()
MIDTERM = StringVar()
FINAL = StringVar()
AVERAGE = StringVar()
PEQUIVALENT = StringVar()
REMARKS = StringVar()

# ============================METHODS=====================================

def Database():
    conn = sqlite3.connect("masterfile.db")
    cursor = conn.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS `masterfile` (mem_id INTEGER NOT NULL  PRIMARY KEY AUTOINCREMENT, number TEXT, sname TEXT, gender TEXT, course TEXT, subject TEXT, prelim TEXT, midterm TEXT, final TEXT, average TEXT, pequivalent TEXT, remarks TEXT)")
    cursor.execute("SELECT * FROM `masterfile` ORDER BY `number` ASC")
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data))
    cursor.close()
    conn.close()

def Backtopdown():
    result = tkMessageBox.askquestion('Python - Save Record To Table', 'Are you sure you want to exit?', icon="warning")
    if result == 'yes':
        root.destroy()
        import pulldownmenugui2


# ========================= SOLUTION ==============================================

def GradeCal():
    IPM = PRELIM.get()
    IMT = MIDTERM.get()
    IFN = FINAL.get()

    if (IPM.isdigit()) and (IMT.isdigit()) and (IFN.isdigit()):
        AVRG = (int(IPM) + int(IMT) + int(IFN))/3
        avrg = str("{:,.2f}".format(float(AVRG)))
        AVERAGE.set(avrg)
    else:
        tkinter.messagebox.showinfo("WRONG DATA", "INVALID DATA")
        return AddNewWindow()

    if AVRG >= 96 and AVRG <= 100:
        grade = "1.00"
        remarks = "Excellent"
    elif AVRG >= 94:
        grade = "1.25"
        remarks = "Very Good"
    elif AVRG >= 92:
        grade = "1.50"
        remarks = "Very Good"
    elif AVRG >= 89:
        grade = "1.75"
        remarks = "Good"
    elif AVRG >= 87:
        grade = "2.00"
        remarks = "Good"
    elif AVRG >= 84:
        grade = "2.25"
        remarks = "Good"
    elif AVRG >= 82:
        grade = "2.50"
        remarks = "Fair"
    elif AVRG >= 79:
        grade = "2.75"
        remarks = "Fair"
    elif AVRG >= 75:
        grade = "3.00"
        remarks = "Passed"
    elif AVRG >= 60:
        grade = "5.00"
        remarks = "Failed"

    else:
        grade = "INVALID"
        remarks = "FA / WP / WF"

    PEQUIVALENT.set(grade)
    REMARKS.set(remarks)


# ================================================================================

# =============== DATA CLEAR =============================================
def ClearAll():
    NUMBER.set("")
    SNAME.set("")
    GENDER.set("")
    COURSE.set("")
    SUBJECT.set("")
    PRELIM.set("")
    MIDTERM.set("")
    FINAL.set("")
    AVERAGE.set("")
    PEQUIVALENT.set("")
    REMARKS.set("")
    root.clear()

# ==========================================================================
# ============================== DATA SUBMISSION ============================
def SubmitData():
    if NUMBER.get() == "" or SNAME.get() == "" or GENDER.get() == "" or COURSE.get() == "" or SUBJECT.get() == "" or PRELIM.get() == "" or MIDTERM.get() == "" or FINAL.get() == "" or AVERAGE.get() == "" or PEQUIVALENT.get() == "" or REMARKS.get() == "":
        result = tkMessageBox.showwarning('', 'Please Input Something', icon="warning")
    else:
        tree.delete(*tree.get_children())
        conn = sqlite3.connect("masterfile.db")
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO `masterfile` (number, sname, gender, course, subject, prelim, midterm, final, average, pequivalent, remarks) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (str(NUMBER.get()), str(SNAME.get()), str(GENDER.get()), str(COURSE.get()), str(SUBJECT.get()), str(PRELIM.get()), str(MIDTERM.get()), str(FINAL.get()), str(AVERAGE.get()), str(PEQUIVALENT.get()), str(REMARKS.get())))
        conn.commit()
        cursor.execute("SELECT * FROM `masterfile` ORDER BY `number` ASC")
        fetch = cursor.fetchall()
        for data in fetch:
            tree.insert('', 'end', values=(data))
        cursor.close()
        conn.close()
        NUMBER.set("")
        SNAME.set("")
        GENDER.set("")
        COURSE.set("")
        SUBJECT.set("")
        PRELIM.set("")
        MIDTERM.set("")
        FINAL.set("")
        AVERAGE.set("")
        PEQUIVALENT.set("")
        REMARKS.set("")

# ==============================================================================
# ============================== UPDATE ========================================
def UpdateData():
    if NUMBER.get() == "" or SNAME.get() == "" or GENDER.get() == "" or COURSE.get() == "" or SUBJECT.get() == "" or PRELIM.get() == "" or MIDTERM.get() == "" or FINAL.get() == "" or AVERAGE.get() == "" or PEQUIVALENT.get() == "" or REMARKS.get() == "":
        result = tkMessageBox.showwarning('', 'Please Input Something', icon="warning")
    else:
        tree.delete(*tree.get_children())
        conn = sqlite3.connect("masterfile.db")
        cursor = conn.cursor()
        cursor.execute("UPDATE `masterfile` SET `number` = ?, `sname` = ?, `gender` =?, `course` = ?,  `subject` = ?, `prelim` = ?, `midterm` = ?, `final` = ?, `average` = ?, `pequivalent` = ?, `remarks` = ? WHERE `mem_id` = ?", (str(NUMBER.get()), str(SNAME.get()), str(GENDER.get()), str(COURSE.get()), str(SUBJECT.get()), str(PRELIM.get()), str(MIDTERM.get()), str(FINAL.get()), str(AVERAGE.get()), str(PEQUIVALENT.get()), str(REMARKS.get()), int(mem_id)))
        conn.commit()
        cursor.execute("SELECT * FROM `masterfile` ORDER BY `number` ASC")
        fetch = cursor.fetchall()
        for data in fetch:
            tree.insert('', 'end', values=(data))
        cursor.close()
        conn.close()
        NUMBER.set("")
        SNAME.set("")
        GENDER.set("")
        COURSE.set("")
        SUBJECT.set("")
        PRELIM.set("")
        MIDTERM.set("")
        FINAL.set("")
        AVERAGE.set("")
        PEQUIVALENT.set("")
        REMARKS.set("")
# =================================================================================================
def OnSelected(event):
    global mem_id, UpdateWindow
    curItem = tree.focus()
    contents = (tree.item(curItem))
    selecteditem = contents['values']
    mem_id = selecteditem[0]
    NUMBER.set("")
    SNAME.set("")
    GENDER.set("")
    COURSE.set("")
    SUBJECT.set("")
    PRELIM.set("")
    MIDTERM.set("")
    FINAL.set("")
    AVERAGE.set("")
    PEQUIVALENT.set("")
    REMARKS.set("")
    NUMBER.set(selecteditem[1])
    SNAME.set(selecteditem[2])
    GENDER.set(selecteditem[3])
    COURSE.set(selecteditem[4])
    SUBJECT.set(selecteditem[5])
    PRELIM.set(selecteditem[6])
    MIDTERM.set(selecteditem[7])
    FINAL.set(selecteditem[8])
    AVERAGE.set(selecteditem[9])
    PEQUIVALENT.set(selecteditem[10])
    REMARKS.set(selecteditem[11])

    UpdateWindow = Toplevel()
    UpdateWindow.title("updaaate Solutions School, INC.")
    width = 400
    height = 600
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = ((screen_width / 2) + 450) - (width / 2)
    y = ((screen_height / 2) + 20) - (height / 2)
    UpdateWindow.resizable(TRUE, TRUE)
    UpdateWindow.config(bg="white")
    UpdateWindow.geometry("%dx%d+%d+%d" % (width, height, x, y))
    if 'NewWindow' in globals():
        NewWindow.destroy()
# ========================================================================

    # ===================FRAMES==============================
    FormTitle = Frame(UpdateWindow)
    FormTitle.pack(side=TOP)
    ContactForm = Frame(UpdateWindow)
    ContactForm.pack(side=TOP, pady=10)

    # ===================LABELS==============================
    lbl_title = Label(FormTitle, text="Updating Grade", font=('arial', 16), bg="YELLOWGREEN", width=300)
    lbl_title.pack(fill=X)
    lbl_number = Label(ContactForm, text="Student's No.", font=('arial', 14), bd=5)
    lbl_number.grid(row=0, sticky=W)
    lbl_sname = Label(ContactForm, text="Student's Name", font=('arial', 14), bd=5)
    lbl_sname.grid(row=1, sticky=W)
    lbl_gender = Label(ContactForm, text="Gender", font=('arial', 14), bd=5)
    lbl_gender.grid(row=2, sticky=W)
    lbl_course = Label(ContactForm, text="Course", font=('arial', 14), bd=5)
    lbl_course.grid(row=3, sticky=W)
    lbl_subject = Label(ContactForm, text="Subject", font=('arial', 14), bd=5)
    lbl_subject.grid(row=4, sticky=W)
    lbl_prelim = Label(ContactForm, text="Prelim Grade", font=('arial', 14), bd=5)
    lbl_prelim.grid(row=5, sticky=W)
    lbl_midterm = Label(ContactForm, text="Midterm Grade", font=('arial', 14), bd=5)
    lbl_midterm.grid(row=6, sticky=W)
    lbl_final = Label(ContactForm, text="Final Grade", font=('arial', 14), bd=5)
    lbl_final.grid(row=7, sticky=W)
    lbl_gwa = Label(ContactForm, text="GWA", font=('arial', 14), bd=5)
    lbl_gwa.grid(row=8, sticky=W)
    lbl_pequivalent = Label(ContactForm, text="Points Equivalent", font=('arial', 14), bd=5)
    lbl_pequivalent.grid(row=9, sticky=W)
    lbl_remarks = Label(ContactForm, text="Remarks", font=('arial', 14), bd=5)
    lbl_remarks.grid(row=10, sticky=W)

 #===========================================================================================================
    # ===================ENTRY===============================
    number = Entry(ContactForm, textvariable=NUMBER, font=('arial', 14))
    number.grid(row=0, column=1)
    sname = Entry(ContactForm, textvariable=SNAME, font=('arial', 14))
    sname.grid(row=1, column=1)
    gender_radio1 = Radiobutton(ContactForm, text="Male", variable=GENDER, value="Male")
    gender_radio1.place(x=155, y=74)
    gender_radio2 = Radiobutton(ContactForm, text="Female", variable=GENDER, value="Female")
    gender_radio2.place(x=231, y=74)
    course = ttk.Combobox(ContactForm, textvariable=COURSE, width=33)
    course['values'] = (
    'B.S. Information Technology', 'B.S. Civil Engineering', 'B.S. Electrical Engineering', 'B.S. Education',
    'B.S. Architecture')
    course.current(0)
    course.grid(row=3, column=1)
    subject = Entry(ContactForm, textvariable=SUBJECT, font=('arial', 14))
    subject.grid(row=4, column=1)
    prelim = Entry(ContactForm, textvariable=PRELIM, font=('arial', 14))
    prelim.grid(row=5, column=1)
    midterm = Entry(ContactForm, textvariable=MIDTERM, font=('arial', 14))
    midterm.grid(row=6, column=1)
    final = Entry(ContactForm, textvariable=FINAL, font=('arial', 14))
    final.grid(row=7, column=1)
    average = Entry(ContactForm, textvariable=AVERAGE, font=('arial', 14))
    average.grid(row=8, column=1)
    pequivalent = Entry(ContactForm, textvariable=PEQUIVALENT, font=('arial', 14))
    pequivalent.grid(row=9, column=1)
    remarks = Entry(ContactForm, textvariable=REMARKS, font=('arial', 14))
    remarks.grid(row=10, column=1)


# ========================================================================
    # ==================BUTTONS==============================
    btn_addcon = Button(ContactForm, text="Calculate", width=50, command=lambda: GradeCal())
    btn_addcon.grid(row=11, columnspan=2, pady=10)
    btn_updatecon = Button(ContactForm, text="Update", width=50, command=lambda: UpdateData())
    btn_updatecon.grid(row=12, columnspan=2, pady=10)
    btn_addcon = Button(ContactForm, text="Clear Data", width=50, command=ClearAll)
    btn_addcon.grid(row=13, columnspan=2, pady=10)

# ===========================================================================
# ============================ DELETING A DATA ===================================
def DeleteData():
    if not tree.selection():
        result = tkMessageBox.showwarning('', 'Please Select Something First!', icon="warning")
    else:
        result = tkMessageBox.askquestion('', 'Are you sure you want to delete this record?', icon="warning")
        if result == 'yes':
            curItem = tree.focus()
            contents = (tree.item(curItem))
            selecteditem = contents['values']
            tree.delete(curItem)
            conn = sqlite3.connect("masterfile.db")
            cursor = conn.cursor()
            cursor.execute("DELETE FROM `masterfile` WHERE `mem_id` = %d" % selecteditem[0])
            conn.commit()
            cursor.close()
            conn.close()

# ===========================================================================================
# =========================== ADD NEW ==================================================
def AddNewWindow():
    global NewWindow
    NUMBER.set("")
    SNAME.set("")
    GENDER.set("")
    COURSE.set("")
    SUBJECT.set("")
    PRELIM.set("")
    MIDTERM.set("")
    FINAL.set("")
    AVERAGE.set("")
    PEQUIVALENT.set("")
    REMARKS.set("")
    NewWindow = Toplevel()
    NewWindow.title("addd Solutions INC. Lists")
    width = 420
    height = 600
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = ((screen_width / 2) - 455) - (width / 2)
    y = ((screen_height / 2) + 20) - (height / 2)
    NewWindow.resizable(TRUE, TRUE)
    NewWindow.config(bg="white")
    NewWindow.geometry("%dx%d+%d+%d" % (width, height, x, y))
    if 'UpdateWindow' in globals():
        UpdateWindow.destroy()

    # ===================FRAMES==============================
    FormTitle = Frame(NewWindow)
    FormTitle.pack(side=TOP)
    ContactForm = Frame(NewWindow)
    ContactForm.pack(side=TOP, pady=10)

#=========================================================================================================
# ===================LABELS==============================
    lbl_title = Label(FormTitle, text="Adding Student Grade", font=('arial', 16), bg="YELLOWGREEN", width=300)
    lbl_title.pack(fill=X)
    lbl_number = Label(ContactForm, text="Student's No.", font=('arial', 14), bd=5)
    lbl_number.grid(row=0, sticky=W)
    lbl_sname = Label(ContactForm, text="Student's Name", font=('arial', 14), bd=5)
    lbl_sname.grid(row=1, sticky=W)
    lbl_gender = Label(ContactForm, text="Gender", font=('arial', 14), bd=5)
    lbl_gender.grid(row=2, sticky=W)
    lbl_course = Label(ContactForm, text="Course", font=('arial', 14), bd=5)
    lbl_course.grid(row=3, sticky=W)
    lbl_subject = Label(ContactForm, text="Subject", font=('arial', 14), bd=5)
    lbl_subject.grid(row=4, sticky=W)
    lbl_prelim = Label(ContactForm, text="Prelim Grade", font=('arial', 14), bd=5)
    lbl_prelim.grid(row=5, sticky=W)
    lbl_midterm = Label(ContactForm, text="Midterm Grade", font=('arial', 14), bd=5)
    lbl_midterm.grid(row=6, sticky=W)
    lbl_final = Label(ContactForm, text="Final Grade", font=('arial', 14), bd=5)
    lbl_final.grid(row=7, sticky=W)
    lbl_gwa = Label(ContactForm, text="GWA", font=('arial', 14), bd=5)
    lbl_gwa.grid(row=8, sticky=W)
    lbl_pequivalent = Label(ContactForm, text="Points Equivalent", font=('arial', 14), bd=5)
    lbl_pequivalent.grid(row=9, sticky=W)
    lbl_remarks = Label(ContactForm, text="Remarks", font=('arial', 14), bd=5)
    lbl_remarks.grid(row=10, sticky=W)
# ==============================================================================
# ===================ENTRY===============================
    number = Entry(ContactForm, textvariable=NUMBER, font=('arial', 14))
    number.grid(row=0, column=1)
    sname = Entry(ContactForm, textvariable=SNAME, font=('arial', 14))
    sname.grid(row=1, column=1)
    gender_radio1 = Radiobutton(ContactForm, text="Male", variable=GENDER, value="Male")
    gender_radio1.place(x=155, y=74)
    gender_radio2 = Radiobutton(ContactForm, text="Female", variable=GENDER, value="Female")
    gender_radio2.place(x=231, y=74)
    course = ttk.Combobox(ContactForm, textvariable=COURSE, width=33)
    course['values'] = ('B.S. Information Technology', 'B.S. Civil Engineering', 'B.S. Electrical Engineering', 'B.S. Education', 'B.S. Architecture')
    course.current(0)
    course.grid(row=3, column=1)
    subject = Entry(ContactForm, textvariable=SUBJECT, font=('arial', 14))
    subject.grid(row=4, column=1)
    prelim = Entry(ContactForm, textvariable=PRELIM, font=('arial', 14))
    prelim.grid(row=5, column=1)
    midterm = Entry(ContactForm, textvariable=MIDTERM, font=('arial', 14))
    midterm.grid(row=6, column=1)
    final = Entry(ContactForm, textvariable=FINAL, font=('arial', 14))
    final.grid(row=7, column=1)
    average = Entry(ContactForm, textvariable=AVERAGE, font=('arial', 14))
    average.grid(row=8, column=1)
    pequivalent = Entry(ContactForm, textvariable=PEQUIVALENT, font=('arial', 14))
    pequivalent.grid(row=9, column=1)
    remarks = Entry(ContactForm, textvariable=REMARKS, font=('arial', 14))
    remarks.grid(row=10, column=1)
# ==============================================================================
    # ==================BUTTONS==============================
    btn_addcon = Button(ContactForm, text="Calculate", width=50, command=lambda: GradeCal())
    btn_addcon.grid(row=11, columnspan=2, pady=10)
    btn_addcon = Button(ContactForm, text="Save", width=50, command=SubmitData)
    btn_addcon.grid(row=12, columnspan=2, pady=10)
    btn_addcon = Button(ContactForm, text="Clear Data", width=50, command=ClearAll)
    btn_addcon.grid(row=13, columnspan=2, pady=10)

#===================================================================================
# ============================FRAMES======================================
Top = Frame(root, width=500, bd=1, relief=SOLID)
Top.pack(side=TOP)
Mid = Frame(root, width=500,  bg="GRAY")
Mid.pack(side=TOP)

Centerleft = Frame(root, width=500,  bg="GRAY")
Centerleft.place(x=200, y=41)
Centerright = Frame(root, width=500,  bg="GRAY")
Centerright.place(x=700, y=41)
MidLeft = Frame(Mid, width=100)
MidLeft.pack(side=LEFT, pady=10)
MidLeftPadding = Frame(Mid, width=370, bg="GRAY")
MidLeftPadding.pack(side=LEFT)
MidRight = Frame(Mid, width=100)
MidRight.pack(side=RIGHT, pady=10)
TableMargin = Frame(root, width=500)
TableMargin.pack(side=TOP)
# ============================LABELS======================================
lbl_title = Label(Top, text="DYNAMIC LINK SCHOOL, INC.", font=('Gothic', 18), width=400)
lbl_title.pack(fill=X)

# ============================BUTTONS=====================================
btn_add = Button(Centerleft, text="+ ADD NEW", bg="lightblue", command=AddNewWindow)
btn_add.pack()
btn_edit = Button(MidLeft, text="UPDATE", bg="lightblue", command= lambda: OnSelected(Event))
btn_edit.pack()
btn_delete = Button(Centerright, text="DELETE", bg="lightblue", command=DeleteData)
btn_delete.pack()
btn_exit = Button(MidRight, text="EXIT", bg="RED", command=Backtopdown)
btn_exit.pack()

# ============================TABLES======================================
scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
tree = ttk.Treeview(TableMargin, columns=("mem_id", "number", "sname", "gender", "course", "subject", "prelim", "midterm", "final", "average", "pequivalent", "remarks"),
                    height=400, selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
scrollbary.config(command=tree.yview)
scrollbary.pack(side=RIGHT, fill=Y)
scrollbarx.config(command=tree.xview)
scrollbarx.pack(side=BOTTOM, fill=X)
tree.heading('mem_id', text="Member ID", anchor=W)
tree.heading('number', text="Student No.", anchor=W)
tree.heading('sname', text="Student Name", anchor=W)
tree.heading('gender', text="Gender", anchor=W)
tree.heading('course', text="Course", anchor=W)
tree.heading('subject', text="Subject", anchor=W)
tree.heading('prelim', text="Prelim", anchor=W)
tree.heading('midterm', text="Midterm", anchor=W)
tree.heading('final', text="Final", anchor=W)
tree.heading('average', text="GWA", anchor=W)
tree.heading('pequivalent', text="Points Equivalent", anchor=W)
tree.heading('remarks', text="Remarks", anchor=W)
tree.column('#0', stretch=NO, minwidth=0, width=0)
tree.column('#1', stretch=NO, minwidth=0, width=0)
tree.column('#2', stretch=NO, minwidth=0, width=100)
tree.column('#3', stretch=NO, minwidth=0, width=110)
tree.column('#4', stretch=NO, minwidth=0, width=120)
tree.column('#5', stretch=NO, minwidth=0, width=180)
tree.column('#6', stretch=NO, minwidth=0, width=120)
tree.column('#7', stretch=NO, minwidth=0, width=110)
tree.column('#8', stretch=NO, minwidth=0, width=80)
tree.column('#9', stretch=NO, minwidth=0, width=80)
tree.column('#10', stretch=NO, minwidth=0, width=110)
tree.pack()
tree.bind('<Double-Button-1>', OnSelected)

# ============================INITIALIZATION==============================
Database()
if __name__ == '__main__':

    mainloop()