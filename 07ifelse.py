age=int(input("enter the age"))
if (age<18):
    print("not elgible for vote")
else:
    print("elgible for vote")

 
 
score=int(input("enter the score"))
if (score>=80 and score<=100):
    print("Grade A")
elif (score>=60 and score<80):
    print("Grade B")
elif (score>=33 and score<60):
    print("Pass")
else:
    print("fail")


import time
timestamp=time.strftime('%H:%M:%S')
print(timestamp)