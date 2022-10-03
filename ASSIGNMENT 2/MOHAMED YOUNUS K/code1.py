import time
import random
i=0
while(i<=2000):
    i=i+1
    time.sleep(5)
    temp=random.randint(0,30)
    humid=random.randint(1,100)
    if temp<=15:
       print("temperature is high alarm is on") 
    else:
        print("temperature is normal alarm is off")
    if humid<=15:
           print ("humidity is normal alarm is off") 
    else:
          print ("humidity is high alarm is on")
Footer
