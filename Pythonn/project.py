import os
print('\t\t\t\tThe Menu Tools')
print('\t\t\t\t---------------')

s = '''Press 1 : To open notepad
Press 2 : To open Chrome
Press 3 : To open Vs Code
Press 4 : To Open whatsapp'''

print(s)

ch = input('Enter your choice: ')

if (('notepad' in ch) or ('editor' in ch ) and ( not ('dont' in ch))):
    os.system('notepad')
elif ('chrome' in ch) :
    os.system('')

else:
    print('idk')
