import re
# pattern = r"[a-z]+"
# print(re.match(pattern,"abc123abc")) #matches in a string. (Pattern,string)
# print(re.findall(pattern,"abc123abc")) #returns a list of all match
# print(re.search(pattern,"abc123abc")) #search and match same

# pattern = r"[0-9]+"
# print(re.split(pattern,"abc123abc")) #search and match same


# pattern = r'[0-9]+'
# print(re.findall(pattern,"My phtone number is 01942776654"))

# pattern = r'[0-9]{8}'
# print(re.match(pattern,'097846453'))

emails = ['example@mail.com','1234example@mail.com','siyam.hassan.main@gmail.com','siyamhassan.main@gmail.edu.com']
valid_email = []
pattern = r'^[a-z]+.?[a-z]+.?[a-z]+@[a-z]+.[a-z]+.?[a-z]+.?[a-z]+'

for email in emails:
    if re.findall(pattern,email):
        valid_email.append(email)
    
print(valid_email)