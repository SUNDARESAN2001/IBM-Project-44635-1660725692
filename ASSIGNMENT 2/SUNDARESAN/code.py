import random
while(True):
    a=random.randint(30,99)
    b=random.randint(30,99)
    c=random.randint(37,99)
    d=random.randint(37,99)
    if(a>60):
        print("high humidity of:",a,"%","alarm is on")
    elif(b<99):
        print("Normal humidity of:",b,"%","alarm is off")
    if(c>70):
        print("high temperature of:",c,"%","alarm is on")
    elif(d<99):
        print("Normal temperature of:",d,"%","alarm is off")
        break
