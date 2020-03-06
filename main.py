#1. Create a say_hello() function; that prints hello five times
#2. Creat a function with one argument first_name and print it with default last name
# ==============================================================

#1. Create a say_hello() function; that prints hello five times
def say_hello():
  counter = 1
  while counter < 6:
    print(str(counter) + " Hello!")
    counter += 1

say_hello()
print('--------------******--------------\n')

#2. Creat a function with one argument first_name and print it with default last name
def print_name(first_name):
  print(first_name + " Singh")

print_name("Ajit")
print_name("Babbu")
print_name("Kuku")
print('--------------******--------------\n')
