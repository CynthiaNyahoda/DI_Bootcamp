# opening a file is only to open by default
f=open('secrets.text', 'a+')
# to write in the file
f.write("\nLife is good\n")
# to close the file
f.close()
# new line character = \n
# you can use this with "try" and "finally"
# "try" to write and "finally" to close

#  using faker, you can try loop and write something in a file
# from faker import faker
# fake = faker()
# with open ('output.txt', 'w') as f:
#     for i in range (10):
#         f.write(f'{fake.name()}\n')

# from line in open('output.txt'):
# print(line)

# WHEN USING JASON!!
# usually in objetcs,arrays,string and numbers

# HTTP!!!!!
# nullpod company
METHODS
# ? = is a parameter to a url
#  1. GET is the first method
# used to retrieve data and is requested from the url
# normally has length restriction , can be bookmarked and should never be passed through senstive data
#  2. POST is the second method
# you can create an API using flask
# used to send data
#  3. PUT is the third


# PYTHON API
# install a requests folder
# import it eg
import requests
response= requests.get("paste link")
print(response.text)
# using json
response=requests.get('string')
joke = response.jasom
print(type(joke))


# you can build a weather app