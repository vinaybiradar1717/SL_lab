# 5a. Write a temperature converter python program, which is menu driven. 
# Each such conversion logic should be defined in separate functions. 
# The program should call the respective function based on the user’s requirement. 
# The program should run as long as the user wishes so. 
# Provide an option to view the conversions stored as list of tuples with attributes -
# from unit value, to unit value sorted by the user’s choice (from-value or to-value).


def CTOF(c):
    return 32 + ((9/5)*c)
def FTOK(f):
    return 273.15 + (5/9)*(f-32)
def KTOC(k):
    return k-273.15

l = []
while True:
    ch = int(input("1.CTOF \n2.FTOK \n3.KTOC \n4.EXIT\n"))
    if ch==1:
        c = float(input("celcius: "))
        print("Farenheit:" +str(CTOF(c))+" Farenheit" )
        l.append(tuple((c,str(CTOF(c)))))

    if ch==2:
        f = float(input("farenheit: "))
        print("Kelvin:"+str(FTOK(f))+" K")
        l.append(tuple((f,str(FTOK(f)))))

    if ch==3:
        k=float(input("kelvin: "))
        print("Celcius: "+str(KTOC(k))+" degrees")
        l.append(tuple((k,str(KTOC(k)))))

    if ch==4:
        print(l)
        exit()

