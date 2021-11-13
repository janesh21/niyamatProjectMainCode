y1 =0
y2 =0
y3 =0

def bp_main ():
    lst = []
 

    n = int(input("Enter number of elements for Blood Pressure: "))
 
    for i in range(0, n):
          ele = int(input())
 
          lst.append(ele)

    sum_a = sum(lst)
    
    mean1 = (sum_a / n)
    print (mean1)

    y1 = (0.334)*(mean1 - 166.9)+20.25
    print (y1)


bp_main()

def cl_main ():
    lst = []
 

    n = int(input("Enter number of elements for Cholestrol: "))
 
    for i in range(0, n):
          ele = float(input())
 
          lst.append(ele)

    sum_a = sum(lst)
    
    mean2 = (sum_a / n)
    print (mean2)

    y2 = (0.8515)*(mean2 - 164.85)+32.25
    print (y2)


cl_main()

def sg_main ():
    lst = []
 

    n = int(input("Enter number of elements for A1C (Sugar): "))
 
    for i in range(0, n):
          ele = float(input())
 
          lst.append(ele)

    sum_a = sum(lst)
    
    mean = (sum_a / n)
    print (mean)

    y3 = (51.967)*(mean - 5.37)+108.85
    print (y3)


sg_main()

def final():
    y_final = y1+y2+y3
    
    if y_final <185.0:
        print("Patient has a low risk of heart failure and is within the normal range.")
    
    elif y_final>235.0:
        print("Patient has a high risk of heart failure and has extreme values.")

    else:
        print("Patient has a moderate risk of heart failure.")

final()
