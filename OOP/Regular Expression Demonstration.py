import datetime
import re
first_name = input("Enter your first name : ")
last_name = input("Enter your last name : ")
full_name = first_name + last_name
contact_number = input("Enter 10 your digit mobile number : ")
date = datetime.datetime.now().strftime ("%Y/%m/%d")
# print(date)
string_given = '''
Hello <<name>>, We have your full name as <<full name>> in our system.
your contact number is 91-xxxxxxxxxx. Please,let us know in case of any 
clarification Thank you BridgeLabz 01/01/2016. '''

regex1 = re.compile("<<name>>")
string_given = regex1.sub(first_name , string_given)
# print(string_given)

regex2 = re.compile("<<full name>>")
string_given = regex2.sub(full_name , string_given)
# print(string_given)

# regex4 = re.compile()

regex3 = re.compile("xxxxxxxxxx")
string_given = regex3.sub(contact_number, string_given)
# print(string_given)

regex4 = re.compile("01/01/2016")
string_given = regex4.sub(date, string_given)
print(string_given)
