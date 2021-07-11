#File = open ("C:\Users\stuar\Desktop\DevOps Training\1\File\myfile.txt", mode='w')


Ylist = ['x','+','-','/']
while True:
    xvalue = int(input('What is your X numeric value ?'))
    #if xvalue.isdigit():
     #   print (xvalue) 
    #else:
    #    print ("X is not a number")
     #   break
    yvalue = input('What is your Y operator value?')
    if yvalue in Ylist:
        print (yvalue)
    else:
        print ("Y's not in the list") 
        break   
    zvalue = int(input('What is your Z numeric value ?'))
    #if zvalue.isdigit():
    #    print(zvalue) 
    #else:
    #    print ("Z is not a number")
    #    break 
    if yvalue == 'x':
        sumss = xvalue*zvalue
        print(sumss)
        print(xvalue*yvalue)
    elif yvalue == '+':
        sumss = xvalue+zvalue
        print(sumss)
        print(xvalue+zvalue)
    elif yvalue == '-':
        sumss = xvalue-zvalue
        print(sumss)
        print(xvalue-zvalue)
    elif yvalue == '/':
        sumss=xvalue/zvalue
        print(sumss)
        print(xvalue/zvalue)
    break