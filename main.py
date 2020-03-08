#1. Create a say_hello() function; that prints hello five times
#2. Create a function with one argument first_name and print it with default last name
#3. Create a funciton with default parameter and print its values
#4. add Doc Strings to add info to each function ==============================================================

#1. Create a say_hello() function; that prints hello five times

def say_hello():
  '''Prints "Hello" 5 times'''
  counter = 1
  while counter < 6:
    print(str(counter) + " Hello!")
    counter += 1

say_hello()
print('--------------******--------------\n')

#2. Create a function with one argument first_name and print it with default last name
def print_name(first_name):
  '''Prints first name and last name'''
  print(first_name + " Singh")

print_name("Ajit")
print_name("Babbu")
print_name("Kuku")
print('--------------******--------------\n')


#3. Create a funciton with default parameter and print its values
def print_country(country = 'USA'):
  '''Prints country name'''
  print('I am from ' + country)

print_country('Mexico')
print_country()
print_country('India')
print('--------------******--------------\n')

