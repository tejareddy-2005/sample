#Email Automation
#OTP Authentication
import random
import math
import smtplib#simple mail transfer protocol library

digits="0123456789"
OTP=""

for i in range(6):
    OTP+=digits[math.floor(random.random()*10)]
otp=OTP+"is your otp"
msg=otp
s=smtplib.SMTP("smtp.gmail.com",587)
s.starttls()
s.login("tejareddydusani0@gmail.com","zyky aove spah xmbk")
user="tejareddydusani0@gmail.com"
mailid=input("enter the mail which you want to send...")
s.sendmail(user,mailid,msg)

while True:
    a=input("Enter the otp")
    if a==OTP:
        print("otp is correct")
    else:
        print("incorrect otp")
