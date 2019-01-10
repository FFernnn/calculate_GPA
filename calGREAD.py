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

def show(f):
    infor = open_file(f)
    t = 'Term'
    o = 'Order'
    s = 'Subject'
    c = 'Credit'
    g = 'Grade'
    
    select_term = (input('Select term [ex. 1] : '))
    print('                                     Your Subject                               ')
    print(t.ljust(10) + o.ljust(7) + s.ljust(45) + c.ljust(10) + g.ljust(5))
    print('--------------------------------------------------------------------------------')
        
    for i in range(len(infor)):
        if select_term == infor[i][0]:
            print((infor[i][0]).ljust(10) + (infor[i][1]).ljust(5) + (infor[i][2]).ljust(50) + (infor[i][3]).ljust(10) + (infor[i][4]).ljust(5))
    
    print('--------------------------------------------------------------------------------') 
    
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
        print('Select Mode: \n    1.Edit Mode \n    2.Show Object Mode \n    3.Calculate Grade Mode \n    4.Insert Mode \n     Exit : ^c')
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