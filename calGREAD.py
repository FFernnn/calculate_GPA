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
    print('                                     Your Grade                                 ')
    print(t.ljust(10) + o.ljust(7) + s.ljust(45) + c.ljust(10) + g.ljust(5))
    print('--------------------------------------------------------------------------------')
        
    for i in range(len(infor)):
        if select_term == infor[i][0]:
            print((infor[i][0]).ljust(10) + (infor[i][1]).ljust(5) + (infor[i][2]).ljust(50) + (infor[i][3]).ljust(10) + (infor[i][4]).ljust(5))
    print('--------------------------------------------------------------------------------') 
    print('GPA : ') 
    print('GPAX : ')   
    print('--------------------------------------------------------------------------------') 
    print('')
    print('')
        #else:
        #    print('Try again!!!')
        #    print('----------------------------------------------------------------------')


def main_cal():
    print('----------------------------CALCULATE GRADE-------------------------------------')
    while True:
        print('Select Mode: \n    1.Edit Mode \n    2.Show Grade Mode  \n    Exit : ^c')
        select_mode = (input('Your select: '))
        if select_mode == "1":
            print('-------EDIT MODE-------')
            edit("calculator_GPA.csv")
            print('')
        elif select_mode == '2':
            print('-------SHOW GRADE MODE-------')
            show("calculator_GPA.csv")
            print('')
main_cal()