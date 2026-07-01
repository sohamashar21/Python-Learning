# Variables in python

first_name = 'Soham'
last_name = 'Ashar'
country = 'India'
city = 'Ahmedabad'
age = 19
is_married = False
skills = ['HTML','CSS','JS','React','Python']
person_info = {
  'first_name': 'Soham',
  'last_name': 'Ashar',
  'country':'India',
  'city': 'Ahmedabad'
}

# Printing the values Stored in variables
print('First name: ',first_name)
print('First name length: ',len(first_name))
print('Last name: ', last_name)
print('Last name length: ', len(last_name))
print('Country: ',country)
print('City: ',city)
print('Age: ',age)
print('Married: ',is_married)
print('Skills: ',skills)
print('Person information: ',person_info)


# Declaring multiple variables in one line

first_name,last_name,country,age,is_married = 'Soham','Ashar','India',19,False

print(first_name, last_name, country, age, is_married)
print('First name:', first_name)
print('Last name: ', last_name)
print('Country: ', country)
print('Age: ', age)
print('Married: ', is_married)