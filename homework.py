# Exercise #1
# Filter out all of the empty strings from the list below
# Output: ['Argentina', 'San Diego', 'Boston', 'New York']
places = [" ","Argentina", " ", "San Diego","","  ","","Boston","New York"]

my_filter_list = list(filter(lambda x: x.split(), places))
print(my_filter_list)


# Exercise #2
# Write an anonymous function that sorts this list by the last name...
# Hint: Use the ".sort()" method and access the key"
# Output: ['Victor aNisimov', 'Gary A.J. Bernstein', 'Joel Carter', 'Andrew P. Garfield', 'David hassELHOFF']
author = ["Joel Carter", "Victor aNisimov", "Andrew P. Garfield","David hassELHOFF","Gary A.J. Bernstein"]
author.sort(key=lambda name: name.split(" ")[-1].lower()) #sort()
print(author)

author = ["Joel Carter", "Victor aNisimov", "Andrew P. Garfield","David hassELHOFF","Gary A.J. Bernstein"]
new_author = sorted(author,key=lambda name: name.split(" ")[-1].lower()) #sorted()
print(new_author)


# Exercise #3
# Convert the list below from Celsius to Farhenheit, using the map function with a lambda...
# Output: [('Nashua', 89.6), ('Boston', 53.6), ('Los Angelos', 111.2), ('Miami', 84.2)]
# # F = (9/5)*C + 32
places = [('Nashua',32),("Boston",12),("Los Angelos",44),("Miami",29)]
output=list(map(lambda x: (x[0],(9/5)*x[1] + 32), places))
print(output)


# Exercise #4
# Write a recursion function to perform the fibonacci sequence up to the number passed in.
# Output for fib(5) => 
# Iteration 0: 1
# Iteration 1: 1
# Iteration 2: 2
# Iteration 3: 3
# Iteration 4: 5
# Iteration 5: 8
def fibonacci(n):
   if n <= 1:
       return 1
   return(fibonacci(n-1) + fibonacci(n-2))

def main(number):
    for i in range(number+1):
        print(f'Iteration {i}: {fibonacci(i)}')
           
main(5)


