import os
import pywhatkit
print('\t\t\t\tThe Menu Tools')
print('\t\t\t\t---------------')

s = '''Press 1 : To open notepad
Press 2 : To open Chrome
Press 3 : To open Vs Code
Press 4 : To Open whatsapp
press 5 : to send whatsapp message'''

print(s)

ch = input('Enter your choice: ')

if (('notepad' in ch) or ('editor' in ch ) and ( not ('dont' in ch))):
    os.system('notepad')
elif ('chrome' in ch) :
    os.system('')

elif (ch == '5'):
   num = input("Enter the mobile Number to send message with country code")
   mess = input("enter the message to send")
   pywhatkit.sendwhatmsg_instantly(num,  mess)

