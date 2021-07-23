import tkinter
from tkinter import *
import os
import random


# Choose User type

def user_type():
    global user_type_screen, badmin, bstudent
    # root.destroy()
    user_type_screen = Tk()
    user_type_screen.config(background="#ffffff")
    user_type_screen.title("User Login")
    user_type_screen.geometry("400x250")
    Label(user_type_screen, text="Select User Type", bg="white", width="300", height="2", font=("Calibri", 13)).pack()
    Label(user_type_screen, text="", bg="white").pack()
    badmin = Button(user_type_screen, text="Admin", height="2", width="30", command=alogin).pack()
    Label(user_type_screen, text="", bg="white").pack()
    bstudent = Button(user_type_screen, text="Student", height="2", width="30", command=login).pack()


def login():
    # studentLogin

    #   def login_database():

    #   labelimage.destroy()
    #   labeltext.destroy()
    #   btnlogin.destroy()
    #   btnregister.destroy()
    #   login_window=root
    #   root.destroy()
    user_type_screen.destroy()
    global login_window
    login_window = Tk()
    login_window.title("LOGIN")
    login_window.geometry("400x250")
    login_window.config(background="#ffffff")

    L1 = Label(login_window, text="Username", bg="white", font="times 20")
    L1.grid(row=1, column=1)
    L2 = Label(login_window, text="Password", bg="white", font="times 20")
    L2.grid(row=3, column=1)

    global username_text
    global password_text
    global E1, E2
    username_text = StringVar()
    E1 = Entry(login_window, textvariable=username_text)
    E1.grid(row=1, column=2)
    password_text = StringVar()
    E2 = Entry(login_window, textvariable=password_text, show='*')
    E2.grid(row=3, column=2)
    B1 = Button(login_window, text="Login", width=20, command=login_verify)
    B1.grid(row=6, column=2)


def alogin():
    #   def login_database():
    #   labelimage.destroy()
    #   labeltext.destroy()
    #   btnlogin.destroy()
    #   btnregister.destroy()
    #   login_window=root
    #    root.destroy()
    user_type_screen.destroy()
    global login_window
    login_window = Tk()
    login_window.title("LOGIN")
    login_window.geometry("400x250")
    login_window.config(background="#ffffff")

    aL1 = Label(login_window, text="Username", bg="white", font="times 20")
    aL1.grid(row=1, column=1)
    aL2 = Label(login_window, text="Password", bg="white", font="times 20")
    aL2.grid(row=3, column=1)

    global ausername_text
    global apassword_text
    global aE1, aE2
    ausername_text = StringVar()
    aE1 = Entry(login_window, textvariable=ausername_text)
    aE1.grid(row=1, column=2)
    apassword_text = StringVar()
    aE2 = Entry(login_window, textvariable=apassword_text, show='*')
    aE2.grid(row=3, column=2)
    aB1 = Button(login_window, text="Login", width=20, command=alogin_verify)
    aB1.grid(row=5, column=2)
    # backbtn1 = Button(login_window, text="Back", width=20, command=user_type)
    # backbtn1.grid(row=7, column=2)


#  login_window.mainloop()

# Implementing event on login button

def login_verify():
    global username1
    username1 = E1.get()
    password1 = E2.get()
    E1.delete(0, END)
    E2.delete(0, END)

    # list_of_files = os.listdir() #selext statemtn
    # if username1 in list_of_files:
    #     file1=open(username1, "r")
    #     verify=file1.read().splitlines()
    #     if password1 in verify:
    #  lab=Label(login_window, text="Login Success", width="300", height="2", font=("Calibri", 13))
    #  lab.grid(row=7,column=2)
    #  bu=Button(login_window, text="OK", height="2", width="30", command=home)
    #  bu.grid(row=9,column=2)
    try:

        sql = "SELECT password from stdRegister where name='{}'".format(username1)
        executeSQL(sql)
        password11 = myCursor.fetchone()
        """print(password11[0])"""
        if (password1 == password11[0]):
            login_success()


        else:
            labe = Label(login_window, text="Invalid Password ")
            labe.grid(row=7, column=2)
        # but=Button(login_window, text="OK", command=delete_password_not_recognised)
        # but.grid(row=9,column=2)

    #            password_not_recognised()

    except Exception as e:
        print(e)
        la = Label(login_window, text="User Not Found. \n Please,try again!", fg="green", font=("calibri", 11))
        la.grid(row=7, column=2)

    #    user_not_found()


def alogin_verify():
    global username1
    username1 = aE1.get()
    password1 = aE2.get()
    aE1.delete(0, END)
    aE2.delete(0, END)

    try:

        sql = "SELECT password from stdRegister where name='{}'".format(username1)
        executeSQL(sql)
        password11 = myCursor.fetchone()
        """print(password11[0])"""
        if (password1 == password11[0]):
            alogin_success()


        else:
            labe = Label(login_window, text="Invalid Password ")
            labe.grid(row=7, column=2)
        # but=Button(login_window, text="OK", command=delete_password_not_recognised)
        # but.grid(row=9,column=2)



    #            password_not_recognised()

    except:
        la = Label(login_window, text="User Not Found. \n Please,try again!", fg="green", font=("calibri", 11))
        la.grid(row=7, column=2)

    #    user_not_found()


# Designing popup for login success

def login_success():
    login_window.destroy()
    global login_success_screen
    login_success_screen = Tk()
    login_success_screen.title("logging in")
    login_success_screen.geometry("400x250")
    login_success_screen.config(background="#ffffff")
    Label(login_success_screen, text="Login Success", bg="white", width="300", height="2", font=("Calibri", 13)).pack()
    Label(login_success_screen, text="")
    Button(login_success_screen, text="OK", height="2", width="30", command=home).pack()


def alogin_success():
    login_window.destroy()
    global alogin_success_screen
    alogin_success_screen = Tk()
    alogin_success_screen.title("logging in")
    alogin_success_screen.geometry("400x250")
    alogin_success_screen.config(background="#ffffff")
    Label(alogin_success_screen, text="Login Success", bg="white", width="300", height="2", font=("Calibri", 13)).pack()
    Label(alogin_success_screen, text="")
    Button(alogin_success_screen, text="OK", height="2", width="30", command=ahome).pack()


# Designing popup for login invalid password

# def password_not_recognised():
#   global password_not_recog_screen
#   password_not_recog_screen = Toplevel(login_window)
#   password_not_recog_screen.title("Success")
#   password_not_recog_screen.geometry("150x100")
#   Label(password_not_recog_screen, text="Invalid Password ").pack()
#  Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()

# Designing popup for user not found

# def user_not_found():
#   global user_not_found_screen
#  user_not_found_screen = Toplevel(login_window)
# user_not_found_screen.title("Success")
# user_not_found_screen.geometry("350x250")
# Label(user_not_found_screen, text="User Not Found").pack()
# Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()


def register():
    # def register_database():

    # labelimage.destroy()
    # labeltext.destroy()
    # btnlogin.destroy()
    # btnregister.destroy()
    # register_window=root
    # root.destroy()
    global register_window
    register_window = Tk()
    register_window.title("REGISTRATION")
    register_window.geometry("400x250")
    register_window.config(background="#ffffff")

    l1 = Label(register_window, text="Username", font="times 20", bg="white")
    l1.grid(row=1, column=1)
    l2 = Label(register_window, text="Email", font="times 20", bg="white")
    l2.grid(row=3, column=1)
    l3 = Label(register_window, text="Password", font="times 20", bg="white")
    l3.grid(row=5, column=1)

    global username_text, Email_text, password_text
    global e1, e2, e3
    username_text = StringVar()
    e1 = Entry(register_window, textvariable=username_text)
    e1.grid(row=1, column=2)
    Email_text = StringVar()
    e2 = Entry(register_window, textvariable=Email_text)
    e2.grid(row=3, column=2)
    password_text = StringVar()
    e3 = Entry(register_window, textvariable=password_text, show='*')
    e3.grid(row=5, column=2)
    b1 = Button(register_window, text="Enter", width=20, command=register_user)
    b1.grid(row=8, column=2)
    # register_window.mainloop()


# Implementing event on register button
def register_user():
    username_info = e1.get()
    Email_info = e2.get()
    password_info = e3.get()
    # global file
    # file = open(username_info , "a+")
    # file.write(username_info + "\n")
    # file.write(Email_info + "\n")
    # file.write(password_info)
    # file.close()
    sqlStatement = "Insert into stdRegister values('{0}', '{1}', '{2}')".format(username_info, Email_info,
                                                                                password_info)
    a = executeSQL(sqlStatement)
    if (a == True):
        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)

        l = Label(register_window, text="Registration Success", fg="green", font=("calibri", 11))
        l.grid(row=10, column=2)
        # register_window.destroy()
        # root=tkinter


def executeSQL(sql):
    try:
        myCursor.execute(sql)
        conn.commit()
        return True
    except Exception as e:
        exceptionScreen(e)


import pymysql

conn = pymysql.connect(host="localhost", user="root", passwd="", db="studentDatabase")
myCursor = conn.cursor()


def exceptionScreen(msg):
    import tkinter as tk
    exceptionScreen1 = tk.Tk()
    exceptionLabel = tk.Label(exceptionScreen1, text=msg)
    exceptionLabel.pack()
    okButton = tk.Button(exceptionScreen1, text="OK", command=lambda: execptionScreen1.destroy())
    exceptionScreen1.mainloop()


def home():
    login_success_screen.destroy()
    global home_page
    home_page = Tk()
    home_page.title("Home Page")
    home_page.geometry("400x250")
    home_page.config(background="#ffffff")
    Label(home_page, text="Welcome!", bg="white", font=("Calibri", 13)).pack(pady=5)
    Label(home_page, text="Choose an Option", bg="white", font=("Calibri", 13)).pack(pady=5)
    Button(home_page, text="Take Exam", font=("Calibri", 13), height="2", width="30", command=take_exam).pack(pady=10)
    Button(home_page, text="Results", font=("Calibri", 13), height="2", width="30", command=result).pack(pady=10)


def result():
    home_page.destroy()
    result = Tk()
    result.title("Results")
    result.geometry("400x250")
    result.config(background="#ffffff")
    newList = []
    executeSQL("SELECT (id) from testDatabase where username='{}'".format(username1))
    length = myCursor.fetchall()
    print(length)
    for i in (length):
        executeSQL("SELECT username, score from testDatabase where id like({})".format(i[0]))
        newLabel = Label(result, text=myCursor.fetchone())

        newList.append(newLabel)
    for i in newList:
        i.pack()


def ahome():
    alogin_success_screen.destroy()
    global ahome_page

    ahome_page = Tk()
    ahome_page.title("Home Page")
    ahome_page.geometry("400x250")
    ahome_page.config(background="#ffffff")
    Label(ahome_page, text="Welcome!", bg="white", font=("Calibri", 13)).pack(pady=5)
    Button(ahome_page, text="Update Questions", height=2, width=30, font=("Calibri", 13),
           command=update_questions).pack(pady=10)
    Button(ahome_page, text="Results", height=2, width=30, font=("Calibri", 13), command=aresult).pack(pady=10)


def update_questions():
    ahome_page.destroy()
    global update_question
    update_question = Tk()
    update_question.title("Update Questions")
    update_question.geometry("400x250")
    update_question.config(background="#ffffff")
    Button(update_question, text="Add questions", command=add_questions).pack(pady=10)
    Button(update_question, text="Remove Questions", command=remove_questions).pack(pady=10)


def add_questions():
    global new_que
    new_que = "###"
    global add_question
    global e, o1, o2, o3, o4, a1
    add_question = Tk()
    add_question.title("Adding questions")
    add_question.geometry("600x500")
    add_question.config(background="#ffffff")
    Label(add_question, text="You can write the questions below to add in quiz!", bg="#ffffff",
          font=("Calibri", 16)).pack(pady=5)
    Label(add_question, text="Enter your question below: ").pack(pady=10)
    e = Entry(add_question)
    e.pack(pady=10)
    Label(add_question, text="enter your options below").pack(pady=10)
    o1 = Entry(add_question)
    o1.pack(pady=5)
    o2 = Entry(add_question)
    o2.pack(pady=5)
    o3 = Entry(add_question)
    o3.pack(pady=5)
    o4 = Entry(add_question)
    o4.pack(pady=10)
    Label(add_question, text="Enter answer option:").pack(pady=10)
    a1 = Entry(add_question)
    a1.pack(pady=10)
    Button(add_question, text="Add", command=added_successfully).pack(pady=10)
    # store e=question, o1..o4 iptions abd a1 correct option


def remove_questions():
    update_question.destroy()
    global remove_question
    remove_question = "###"
    remove_question = Tk()
    remove_question.geometry("500x350")
    remove_question.title("Remove Questions")
    remove_question.config(background="#ffffff")
    Label(remove_question, text="Choose the question from below", bg="#ffffff", font=("Calibri", 16)).grid(row=0,
                                                                                                           column=0)
    r = 2
    c = 2
    yes = IntVar()
    for i in range(len(questions)):
        Label(remove_question, text=questions[i]).grid(row=r, column=0)
        r += 1
    for j in range(len(questions)):
        Checkbutton(remove_question, variable="yes" + str(j), onvalue=1, offvalue=0).grid(row=c,
                                                                                          column=1)  # use radioButton

        c += 1
    # Button(remove_question, text="Confirm", command=removed_successfully).grid(row=11, column=0)


temp = []


def added_successfully():
    questions.append(e.get())
    temp.append(o1.get())
    temp.append(o2.get())
    temp.append(o3.get())
    temp.append(o4.get())
    answers.append(temp)
    executeSQL(
        "INSERT INTO questions(adminID, correctOption, optionA, optionB,optionC, optionD, question) values('{0}','{1}','{2}', '{3}','{4}','{5}','{6}')".format(
            username1, a1.get(), o1.get(), o2.get(), o3.get(), o4.get(), e.get()))

    right_answers.append(a1.get())
    temp.clear()
    Label(add_question, text="Question Added Succesfully").pack(pady=10)


#    global addquestion
# Entry(add_questions,text="Add Questions",width=50,height=5)


def aresult():
    ahome_page.destroy()
    aresult = Tk()
    aresult.title("Results")
    aresult.geometry("400x250")
    aresult.config(background="#ffffff")
    Label(aresult, text="Welcome ", bg="#ffffff", font=("Calibri", 16)).grid(row=0, column=0)
    # l1 = Label(aresult, bg="#ffffff", font=("Calibri", 16)).grid(row=1, column=0)
    executeSQL("SELECT max(id) from testDatabase")
    maxx = myCursor.fetchone()
    maxx = maxx[0]
    for i in range(maxx, maxx - 10, -1):
        executeSQL("SELECT username, score, timestamp from testDatabase where id={}".format(i))
        Label(aresult, text=myCursor.fetchone()).grid()
    # l1.configure(text=ausername_text.get())
    # l1.configure()


# show score+username of student
questions = [
    "this is question 1?",
    "this is question 2?",
    "this is question 3?",
    "this is question 4?",
    "this is question 5?",
    "this is question 6?",
    "this is question 7?",
    "this is question 8?",
    "this is question 9?",
    "this is question 10?",
]

answers = [
    ["1", "2", "3", "4"],
    ["1", "2", "3", "4"],
    ["1", "2", "3", "4"],
    ["1", "2", "3", "4"],
    ["1", "2", "3", "4"],
    ["1", "2", "3", "4"],
    ["1", "2", "3", "4"],
    ["1", "2", "3", "4"],
    ["1", "2", "3", "4"],
    ["1", "2", "3", "4"],
]

right_answers = [1, 1, 1, 1, 3, 1, 0, 1, 3, 3]

user_answer = []

indexes = []


def gen1():
    sql = "Select max(questionID) from questions"
    executeSQL(sql)
    # global max
    max = myCursor.fetchone()
    sql = "Select min(questionID) from questions"
    executeSQL(sql)
    min = myCursor.fetchone()
    if (int(max[0]) > 20):
        max = 20
    global listOfQuestion
    global listOfAnswers
    listOfQuestion = []
    listOfAnswers = []
    for i in range(int(min[0]), int(max[0])):
        executeSQL("SELECT question from questions where questionID like({})".format(i))
        listOfQuestion.append(myCursor.fetchone())
        executeSQL("Select correctOption from questions where questionId={}".format(i))
        listOfAnswers.append(myCursor.fetchone())
    print(listOfQuestion, " ", listOfAnswers)


def gen():  # generator #random questions from the database
    gen1()
    global indexes
    while (len(indexes) < 5):
        x = random.randint(0, 9)
        if x in indexes:
            continue
        else:
            indexes.append(x)
    # questionList=['q1',...]
    # ansList=['a'...]


def showresult(score):
    showresult = Tk()
    showresult.geometry("450x200")
    showresult.title("Result")
    showresult.config(background="#ffffff")
    labelscore = Label(showresult, font=("consolas", 16), bg="white")
    labelscore.pack(pady=50)
    labelresulttext = Label(showresult, font=("consolas", 20), bg="#ffffff")
    labelresulttext.pack(pady=5)
    y = "Your score is "
    executeSQL("SELECT max(id) from testDatabase")
    global max
    max = myCursor.fetchone()
    max += 1
    executeSQL("INSERT into testDatabase(username, score, id) values('{0}','{1}',{2})".format(username1, score, max))
    if (score >= 20):
        labelscore.configure(text=(y + str(score)))
        labelscore.configure()
        labelresulttext.configure(text="You are excellent!!")
        labelresulttext.configure()
    elif (score >= 10 and score < 20):
        labelscore.configure(text=(y + str(score)))
        labelresulttext.configure(text="You can do better!!")
    else:
        labelscore.configure(text=(y + str(score)))
        labelresulttext.configure(text="You should work hard!!")


def calc():
    global indexes, user_answers, right_answers
    x = 0
    score = 0
    for i in range(len(user_answer)):
        print(listOfAnswers[i])

        try:
            if (listOfAnswers[i][0] == 'a'):
                listOfAnswers[i] = 1
            elif (listOfAnswers[i][0] == 'b'):
                listOfAnswers[i] = 2
            elif (listOfAnswers[i][0] == 'c'):
                listOfAnswers[i] = 3
            else:
                listOfAnswers[i] = 4
        except:
            print("HI")
        # print(listOfAnswers[i], user_answer[x], listOfAnswers[i])
        if user_answer[i] == listOfAnswers[i]:
            score = score + 5
        x += 1
    print(score)
    showresult(score)
    # store the result in the database, username, score


ques = 1


def selected(r):
    global radiovar, user_answer
    global lblquestion, r1, r2, r3, r4
    global ques
    x = radiovar.get()
    # a,b,c,d=r1.get(),r2.get(),r3.get(),r4.get()
    # print(a,b,c,d)
    print(r)
    user_answer.append(r)
    # radiovar.set(-1)
    if ques < 2:
        lblquestion.config(text=listOfQuestion[ques])  # takes random questions// use database
        executeSQL("Select optionA, optionB, optionC, optionD from questions where question like('{}')".format(
            listOfQuestion[ques][0]))
        optionList = myCursor.fetchone()
        r1['text'] = optionList[0]
        r2['text'] = optionList[1]
        r3['text'] = optionList[2]
        r4['text'] = optionList[3]
        ques += 1
    else:
        calc()


def take_exam():
    home_page.destroy()
    gen()
    take_exam = Tk()
    take_exam.title("Home Page")
    take_exam.geometry("600x500")
    take_exam.config(background="#ffffff")
    global lblquestion, r1, r2, r3, r4
    ques = 0
    lblquestion = Label(take_exam, text=listOfQuestion[ques], font=("Consolas", 16), width=500, justify="center",
                        wraplength=400, background="#ffffff")
    lblquestion.pack()  # (pady=(50, 30))
    executeSQL("Select optionA, optionB, optionC, optionD from questions where question like('{}')".format(
        listOfQuestion[ques][0]))
    optionList = myCursor.fetchone()

    global radiovar
    radiovar = IntVar()
    radiovar.set(-1)

    r1 = Radiobutton(take_exam, text=optionList[0], font=("Times", 12), background="#ffffff", value=0,
                     variable=radiovar, command=lambda: selected(1))
    r1.pack(pady=5)

    r2 = Radiobutton(take_exam, text=optionList[1], font=("Times", 12), background="#ffffff", value=1,
                     variable=radiovar, command=lambda: selected(2))
    r2.pack(pady=5)

    r3 = Radiobutton(take_exam, text=optionList[2], font=("Times", 12), background="#ffffff", value=2,
                     variable=radiovar, command=lambda: selected(3))
    r3.pack(pady=5)

    r4 = Radiobutton(take_exam, text=optionList[3], font=("Times", 12), background="#ffffff", value=3,
                     variable=radiovar, command=lambda: selected(4))
    r4.pack(pady=5)


root = tkinter.Tk()
root.title("MULTIPLE CHOICE QUESTIONS")
root.geometry("600x500")
root.config(background="#ffffff")

'''img1 = PhotoImage(file="C:/Users/Deepak/Downloads/MCQ.png")

labelimage = Label(
    root,
    image = img1,
    background = "#ffffff",
)
labelimage.pack(pady=(40,0))'''

labeltext = Label(
    root,
    text="MULTIPLE CHOICE QUESTIONS",
    font=("Comic sans MS", 24, "bold"),
    background="#ffffff",
)
labeltext.pack(pady=(0, 50))

btnlogin = Button(root, text="Login", height="2", width="30", command=user_type)
btnlogin.pack()
Label(text="", background="#ffffff").pack()
btnregister = Button(root, text="Register", height="2", width="30", command=register)
btnregister.pack()

root.mainloop()