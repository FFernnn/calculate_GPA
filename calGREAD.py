import csv

def transform_grade(intput_grade):
    grade = {'A': 4,
             'B+': 3.5,
             'B': 3,
             'C+': 2.5,
             'C': 2,
             'D+': 1.5,
             'D': 1,
             'F': 0}
    return grade[intput_grade]

def open_file(f):
    subject = []
    with open(f,newline='') as csvfile:
        reader = csv.reader(csvfile)
        for i in reader:
            subject.append(i)
    return subject

def edit(f):
    show(f)
    infor = open_file(f)
    t = 'Term'
    o = 'Subject No.'
    s = 'Subject'
    c = 'Credit'
    g = 'Grade'

    print('                                     Edit Mode                                  ')
    select_edit_mode = (input('Select mode: \n    1.Edit Subject \n    2.Add new subject\n Ans: '))

    #edit mode
    if select_edit_mode == "1":
        select_order = (input('Select subject no. [ex. 1] : '))
        #change subject
        change_subject = (input("Press you change subject : "))
        change_credit = (input("Press you change credit : "))
        change_grade = str(input("Press you change grade : "))
        for i in range(len(infor)):
            if select_order == infor[i][1]:
                infor[i][2] = change_subject
                infor[i][3] = change_credit
                infor[i][4] = change_grade
    #add new subject
    elif select_edit_mode == "2":
        num_to_add = int(input("How many subjects do you want to add? \n   Ans: "))
        for i in range (num_to_add):
            new_term = input("Term: ")
            new_order = input("Subject No.: ")
            new_subject = input("Subject: ")
            new_credit = input("Credit: ")
            new_grade = input("Grade: ")
            infor.append([new_term,new_order,new_subject,new_credit,new_grade])
    #calculate new GPA
    average_credit = 0
    average_grade = 0
    for i in range(len(infor)):
        average_credit += float(infor[i][3])
        average_grade += (float(infor[i][3]) * float(transform_grade(infor[i][4])))
    GPA = average_grade / average_credit
    print('NEW GPA: {0:.2f}'.format(GPA))
    choice_save = input('Do you want to save change? [y/n] : ')
    if choice_save == "Y" or "y":
        save(infor)
    elif choice_save == "N" or "n":
        edit(f)
    else:
        print('Try again!!!')
    return

def save(infor):
    file_name = input('File name:')
    with open(file_name, 'w', newline="") as csvfile:
        fieldnames = ['Term', 'Subject No.', 'Subject', 'Credit', 'Grade']
        file = csv.DictWriter(csvfile, fieldnames= fieldnames)
        file.writeheader()
        for i in range(len(infor)):
            file.writerow({'Term': infor[i][0], 'Subject No.': infor[i][1], 'Subject' : infor[i][2], 'Credit': infor[i][3], 'Grade': infor[i][4]})
    print("Save newfile success!!!")
    return


def show(f):
    infor = open_file(f)
    t = 'Term'
    o = 'Subject No.'
    s = 'Subject'
    c = 'Credit'
    g = 'Grade'
    
    print('                                     Your Subject                               ')
    select_term = (input('Select term [ex. 1] : '))
    print(t.ljust(5) + o.ljust(15) + s.ljust(40) + c.ljust(10) + g.ljust(5))
    print('--------------------------------------------------------------------------------')
        
    for i in range(len(infor)):
        if select_term == infor[i][0]:
            print((infor[i][0]).ljust(10) + (infor[i][1]).ljust(7) + (infor[i][2]).ljust(45) + (infor[i][3]).ljust(10) + (infor[i][4]).ljust(5))
    
    print('--------------------------------------------------------------------------------') 
    return

def cal_graed(f):
    infor = open_file(f)

    t_credit = 0
    t_grade = 0
    average_credit = 0
    average_grade = 0
    
    print('                                     Your Grade                                 ')
    select_term = (input('Select term [ex. 1] : '))
    #calculate gpa and calculate gpax
    for i in range(len(infor)):
        t_credit += float(infor[i][3])
        t_grade += (float(infor[i][3]) * float(transform_grade(infor[i][4])))
        if select_term == infor[i][0]:
            average_credit += float(infor[i][3])
            average_grade += (float(infor[i][3]) * float(transform_grade(infor[i][4])))

    GPA = average_grade / average_credit
    GPAX = t_grade / t_credit
    print('GPA : {0:.2f}'.format(GPA)) 
    print('GPAX : {0:.2f}'.format(GPAX))   
    print('--------------------------------------------------------------------------------') 
    print('')
    print('')


def main_cal():
    print('----------------------------CALCULATE GRADE-------------------------------------')
    while True:
        print('Select Mode: \n    1.Edit Mode \n    2.Show Object Mode \n    3.Calculate Grade Mode \n    Exit : ^c')
        select_mode = (input('Your select: '))
        if select_mode == "1":
            print('-------EDIT MODE-------')
            edit("calculator_GPA.csv")
            print('')
        elif select_mode == '2':
            print('-------SHOW OBJECT MODE-------')
            show("calculator_GPA.csv")
            print('')
        elif select_mode == '3':
            print('-------SHOW GRADE MODE-------')
            cal_graed("calculator_GPA.csv")
            print('')
main_cal()