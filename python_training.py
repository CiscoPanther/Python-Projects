#Control flow code challenge
# Write your movie_review function here:
def movie_review(rating):
  if (rating <=5):
    return "Avoid at all costs!"
  elif (rating >= 5) and (rating < 9):
    return "This one was fun."
  else:
    return "Outstanding!"
# Uncomment these function calls to test your movie_review function:
print(movie_review(9))
# should print "Outstanding!"
print(movie_review(4))
# should print "Avoid at all costs!"
print(movie_review(6))
# should print "This one was fun."


# Write your twice_as_large function here:
def twice_as_large(num1, num2):
  if (num1 > num2*2 ):
    return True
  else:
    return False
# Uncomment these function calls to test your twice_as_large function:
print(twice_as_large(10, 5))
# should print False
print(twice_as_large(11, 5))
# should print True


# Write your large_power function here:
def large_power(base, exponent):
  if (base**exponent > 5000):
    return True
  else:
    return False
# Uncomment these function calls to test your large_power function:
print(large_power(2, 13))
# should print True
print(large_power(2, 12))
# should print False


# Write your divisible_by_ten function here:
def divisible_by_ten(num):
 # if num % 10 == 0:
  if num % 10 is 0:
    return True
  else:
    return False
# Uncomment these function calls to test your divisible_by_ten function:
print(divisible_by_ten(20))
# should print True
print(divisible_by_ten(25))
# should print False

# Write your max_num function here:
def max_num(num1, num2, num3):
  if (num1 > num2) and (num1 > num3):
    return num1
  elif (num2 > num1) and (num1 > num3):
    return num2
  elif (num3 > num1) and (num3 > num2):
    return num3
  else:
    return "It's a tie!"

# Uncomment these function calls to test your max_num function:
print(max_num(-10, 0, 10))
# should print 10
print(max_num(-10, 5, -30))
# should print 5
print(max_num(-5, -10, -10))
# should print -5
print(max_num(2, 3, 3))
# should print "It's a tie!"

# Write your over_budget function here:
def over_budget(budget, food_bill, electricity_bill, internet_bill, rent):
  monthly_expenses = (food_bill + electricity_bill + internet_bill + rent)
  if (budget < monthly_expenses):
    return True
  else:
    return False
# Uncomment these function calls to test your over_budget function:
print(over_budget(100, 20, 30, 10, 40))
# should print False
print(over_budget(80, 20, 30, 10, 30))
# should print True

# Write your always_false function here:
def always_false(num):
  if num > 0 and num < 0:
    return True
  else:
    return False
# Uncomment these function calls to test your always_false function:
print(always_false(0))
# should print False
print(always_false(-1))
# should print False
print(always_false(1))
# should print False

# Write your not_sum_to_ten function here:
def not_sum_to_ten(num1, num2):
  if num1 + num2 != 10:
    return True
  else:
    return False
# Uncomment these function calls to test your not_sum_to_ten function:
print(not_sum_to_ten(9, -1))
# should print True
print(not_sum_to_ten(9, 1))
# should print False
print(not_sum_to_ten(5,5))
# should print False

# Write your same_name function here:
def same_name(your_name, my_name):
  if your_name == my_name:
    return True
  else:
    return False
# Uncomment these function calls to test your same_name function:
print(same_name("Colby", "Colby"))
# should print True
print(same_name("Tina", "Amber"))
# should print False


#List in lists
heights = [['Jenny', 61], ['Alexus', 70], ['Sam', 67], ['Grace', 64]]
heights.append(['Vik', 68])

ages = [['Aaron', 15], ['Dhruti', 16]]

names = ['Jenny', 'Alexus', 'Sam', 'Grace']
dogs_names = ['Elphonse', 'Dr. Doggy DDS', 'Carter', 'Ralph']
#zip merges two lists by pairing the values with each other..
names_and_dogs_names = zip(names, dogs_names)
list_names_and_dogs_names = list(names_and_dogs_names)
print(list_names_and_dogs_names)

orders = ['daisies', 'periwinkle']
print(orders)
orders.append('tulips')
orders.append('roses')
print(orders)


orders = ['daisy', 'buttercup', 'snapdragon', 'gardenia', 'lily']
# Create new orders here:
new_orders = orders + ['lilac', 'iris']

broken_prices = [5, 3, 4, 5, 4] + [4]

list1 = range(0, 9)
range1 = range(0, 8)
print(list(range1))
print(list(list1))

list1 = range(5, 15, 3)
list2 = range(0, 40, 5)
print(list(list1))
print(list(list2))

first_names = ['Ainsley', 'Ben', 'Chani', 'Depak']
age = []
age.append(42)
all_ages = age + [32, 41, 29]
name_and_age = zip(first_names, all_ages)
ids = range(0, 4)


last_semester_gradebook = [("politics", 80), ("latin", 96), ("dance", 97), ("architecture", 65)]
subjects = ['physics', 'calculus', 'poetry', 'history']
grades = [98, 97, 85, 88]
subjects.append("Computer Science")
grades.append(100)
grade_book = list(zip(subjects, grades))
grade_book.append(("visual arts", 93))
print(grade_book)
full_gradebook = list(zip(grade_book, last_semester_gradebook ))
print(full_gradebook)

employees = ['Michael', 'Dwight', 'Jim', 'Pam', 'Ryan', 'Andy', 'Robert']
index4 = employees[4]
print(index4)
print(len(employees))
print(employees[6])

shopping_list = ['eggs', 'butter', 'milk', 'cucumbers', 'juice', 'cereal']
print(len(shopping_list))
last_element = shopping_list[-1]
element5 = shopping_list[5]
print(element5)
print(last_element)

suitcase = ['shirt', 'shirt', 'pants', 'pants', 'pajamas', 'books']

beginning = suitcase[0:4]
#Creating a selection from a list is called slicing.

print(beginning)
middle = suitcase[2:4]
print(middle)

suitcase = ['shirt', 'shirt', 'pants', 'pants', 'pajamas', 'books']
start = suitcase[:3]
end = suitcase[-2:]

votes = ['Jake', 'Jake', 'Laurie', 'Laurie', 'Laurie', 'Jake', 'Jake', 'Jake', 'Laurie', 'Cassie', 'Cassie', 'Jake', 'Jake', 'Cassie', 'Laurie', 'Cassie', 'Jake', 'Jake', 'Cassie', 'Laurie']

jake_votes = votes.count("Jake")
print(jake_votes)
cassie_votes = votes.count("Cassie")
print(cassie_votes)
laurie_votes = votes.count("Laurie")
print(laurie_votes)

if (jake_votes > cassie_votes) and (jake_votes > laurie_votes):
  print("Jakes is the new President")
elif (cassie_votes > jake_votes) and (cassie_votes > laurie_votes):
  print("Cassie is the new President")

elif (laurie_votes > jake_votes) and (laurie_votes > cassie_votes):
  print("Cassie is the new President")
else:
  print("There would be a vote recount")

  ### Exercise 1 & 2 ###
addresses = ['221 B Baker St.', '42 Wallaby Way', '12 Grimmauld Place', '742 Evergreen Terrace', '1600 Pennsylvania Ave', '10 Downing St.']

# Sort addresses here:
addresses.sort()
print(addresses)

### Exercise 3 ###
names = ['Ron', 'Hermione', 'Harry', 'Albus', 'Sirius']
names.sort()

### Exercise 4 ###
cities = ['London', 'Paris', 'Rome', 'Los Angeles', 'New York']
#Below code returns none, sorted list cant be = to a variable
sorted_cities = cities.sort()
print(sorted_cities)

inventory = ['twin bed', 'twin bed', 'headboard', 'queen bed', 'king bed', 'dresser', 'dresser', 'table', 'table', 'nightstand', 'nightstand', 'king bed', 'king bed', 'twin bed', 'twin bed', 'sheets', 'sheets', 'pillow', 'pillow']

inventory_len = len(inventory)
first = inventory[0]
last = inventory[-1]
inventory_2_6 = inventory[2:6]
first_3 = inventory[:3]
twin_beds = inventory.count("twin bed")
inventory.sort()
sorted_inventory = sorted(inventory)
print(sorted_inventory)
#Lists slice
toppings = ['pepperoni', 'pineapple', 'cheese', 'sausage', 'olives', 'anchovies', 'mushrooms']
prices = [2,6,1,3,2,7,2]
num_pizzas = len(toppings)
print("We sell " + str(num_pizzas) +" different kinds of pizza!")
pizzas = list(zip(prices, toppings))
print(pizzas)
print("\n")
pizzas.sort()
print(pizzas)
print("\n")
sorted_pizza_list = sorted(pizzas)
print(sorted_pizza_list)

cheapest_pizza = pizzas[0]
print("\n")
print(cheapest_pizza)
priciest_pizza = pizzas[-1]
print("\n")
print(priciest_pizza)
three_cheapest = pizzas[:3]
print("\n")
print(three_cheapest)
num_two_dollars_slices = prices.count(2)
print("\n")
print(num_two_dollars_slices)


def data_retrieve():
  global first_name
  first_name = input('Enter your first name: ')
  global last_name
  last_name = input('Enter your last name: ')
  global Age
  age = input('Enter your age: ')
  global dest
  dest = input('Enter your destination: ')


def data_processing():
  result = "Name: " + first_name[0][1] + "." + last_name + "." + age + "\nDestination: " + dest
  return result


def ticket_print():
  data_retrieve()
  print(data_processing())


ticket_print()


def create_spreadsheet(title = "Applications", row_count = 10):
  print("Creating a spreadsheet called " + title + ", with " + str(row_count) + " rows")

# Call create_spreadsheet() below with the required arguments:
create_spreadsheet()

def calculate_age(current_year, birth_year):
  age = current_year - birth_year
  return age

my_age = calculate_age(2049, 1993)
dads_age = calculate_age(2049,1953)

print("I am " + str(my_age) + " old and my dad is " + str(dads_age) + " years old")




def get_boundaries(target, margin):
  low_limit = target - margin
  high_limit = target + margin
  return low_limit, high_limit

low, high = get_boundaries(100, 20)
print("Low limit: "+str(low)+", high limit: "+str(high))




current_year = 2048
def calculate_age(birth_year):
  age = current_year - birth_year
  return age


print(calculate_age(1970))


def repeat_stuff(stuff, num_repeats = 10):
  return stuff*num_repeats


a = repeat_stuff("Row ", 3)
b = "Your Boat. "
lyrics = a + b

song = repeat_stuff(lyrics)

print(song)


# Write your dog_years function here:
def dog_years(name, age):
  age = age * 7
  return name + ", you are " +str(age) + " years old in dog years"
# Uncomment these function calls to test your dog_years function:
print(dog_years("Lola", 16))
# should print "Lola, you are 112 years old in dog years"
print(dog_years("Baby", 0))
# should print "Baby, you are 0 years old in dog years"


#Write your function here
def double_index(lst, index):
  if index < len(lst):
  	lst[index] = lst[index] * 2
  return lst

print(double_index([3, 8, -10, 12], 2))

def remove_middle(lst, start, end):
  return lst[:start] + lst[end+1:]

print(remove_middle([4, 8, 15, 16, 23, 42], 1, 3))

def more_than_n(lst, item, n):
  b = lst.count(item)
  if b > n:
    return True
  else:
    return False

print(more_than_n([2, 4, 6, 2, 3, 2, 1, 2], 2, 3))
def more_frequent_item(lst, item1, item2):
  b = lst.count(item1)
  c = lst.count(item2)
  if b > c:
    return item1
  elif c > b:
    return item2
  elif b == c:
    return item1
print(more_frequent_item([2, 3, 3, 2, 3, 2, 3, 2, 3], 2, 3))

def middle_element(lst):
  if len(lst) % 2 == 0:
    sum = lst[int(len(lst)/2)] + lst[int(len(lst)/2) - 1]
    return sum / 2
  else:
    return lst[int(len(lst)/2)]

print(middle_element([5, 2, -10, -4, 4, 5]))

def append_sum(lst):
  lst.append(lst[-1] + lst[-2])
  lst.append(lst[-1] + lst[-2])
  lst.append(lst[-1] + lst[-2])
  return lst

print(append_sum([1, 1, 2]))

def larger_list(lst1, lst2):
  if len(lst1) >= len(lst2):
    return lst1[-1]
  else:
    return lst2[-1]
print(larger_list([4, 10, 2, 5], [-10, 2, 5, 10]))

def combine_sort(lst1, lst2):
  a = lst1 + lst2
  a.sort()
  return a
print(combine_sort([4, 10, 2, 5], [-10, 2, 5, 10]))

def append_size(lst):
  lst.append(len(lst))
  return lst
print(append_size([23, 42, 108]))

def every_three_nums(start):
  start = list(range(start, 101, 3))
  return start
print(every_three_nums(91))

promise = "I will not chew gum in class"
for i in range(5):
  print(promise)

students_period_A = ["Alex", "Briana", "Cheri", "Daniele"]
students_period_B = ["Dora", "Minerva", "Alexa", "Obie"]

for student in students_period_A:
  students_period_B.append(student)
  print(student)

dog_breeds_available_for_adoption = ['french_bulldog', 'dalmation', 'shihtzu', 'poodle', 'collie']
dog_breed_I_want = 'dalmation'
for breeds in dog_breeds_available_for_adoption:
  print(breeds)
  if breeds == 'dalmation':
     break

print("They have the dog I want!")

ages = [12, 38, 34, 26, 21, 19, 67, 41, 17]
for i in ages:
  if i < 21:
    continue
  print(i)

all_students = ["Alex", "Briana", "Cheri", "Daniele", "Dora", "Minerva", "Alexa", "Obie", "Arius", "Loki"]
students_in_poetry = []

while len(students_in_poetry) < 6:
  student = all_students.pop()
  students_in_poetry.append(student)

print(students_in_poetry)

sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]

scoops_sold = 0
for sales in sales_data:
  for location in sales_data:
    print(location)

sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]

scoops_sold = 0

for location in sales_data:
  print(location)
  for element in location:
    scoops_sold += element

print(scoops_sold)

words = ["@coolguy35", "#nofilter", "@kewldawg54", "reply", "timestamp", "@matchamom", "follow", "#updog"]
usernames = []

for word in words:
  if word[0] == '@':
    usernames.append(word)
print(usernames)

usernames = [word for word in words if word[0] == '@']
print(usernames)

heights = [161, 164, 156, 144, 158, 170, 163, 163, 157]
can_ride_coaster = []

for height in heights:
  if height > 161:
    can_ride_coaster.append(height)

print(can_ride_coaster)

my_upvotes = [192, 34, 22, 175, 75, 101, 97]
updated_upvotes = [vote_value + 100 for vote_value in my_upvotes]

celsius = [0, 10, 15, 32, -5, 27, 3]

fahrenheit = [temp*(9/5) + 32 for temp in celsius]

print(fahrenheit)

single_digits = range(10)
squares = []

for item in single_digits:
  print(item)
  squares.append(item**2)

cubes = [item**3 for item in single_digits]
print(cubes)
print(squares)

#Barber shop Loop Project
hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

total_price = 0
for i in prices:
  total_price += i
average_price = total_price/len(prices)
print("The Average Haircut Price is " + str(average_price))
new_prices = [item - 5 for item in prices]
print(new_prices)
total_revenue = 0
for i in range(len(hairstyles)):
  cash = prices[i] * last_week[i]
  total_revenue+=cash
print(total_revenue)
average_daily_revenue = total_revenue/7
print(average_daily_revenue)
cuts_under_30 = [hairstyles[i] for i in range(len(hairstyles)) if prices[i] < 30]
print(cuts_under_30)

my_list = [5, 10, -2, 8, 20]
new_list = [i for i in my_list if i > 5]
print(new_list)

numbers = [1, 1, 2, 3]

#When the loop reaches 2 it stops without printing 2
for number in numbers:
  if number % 2 == 0:
    break
  print(number)

numbers = [2, 4, 6, 8]
for number in numbers:
  print("hello!")

#When the loop reaches the element 2, it passes to the next number before printing it.
numbers = [1, 1, 2, 3]
for number in numbers:
  if number % 2 == 0:
    continue
print(number)

def odd_nums(lst):
    for item in lst:
        if item % 2 == 1:
            print(item)

def even_numbers(lst):
    for item in lst:
        if item % 2 == 0:
            print(item)

even_numbers([1, 3, 4, 2,6, 5, 8, 100, 101])
odd_nums([1, 3, 4, 2,6, 5, 8, 100, 101])

def divisible_by_ten(nums):
  count = 0
  for number in nums:
    if (number % 10 == 0):
      count += 1
  return count

print(divisible_by_ten([20, 25, 30, 35, 40]))


def add_greetings(names):
  greeting = []
  for name in names:
  	greeting.append("Hello, "+ name)
  return greeting


print(add_greetings(["Owen", "Max", "Sophie"]))

def delete_starting_evens(lst):
  while (len(lst) > 0 and lst[0] % 2 == 0):
    lst = lst[1:]
  return lst

print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
print(delete_starting_evens([4, 8, 10]))

def odd_indices(lst):
  new_lst = []
  for index in range(1, len(lst), 2):
    new_lst.append(lst[index])
  return new_lst
print(odd_indices([4, 3, 7, 10, 11, -2]))


def exponents(bases, powers):
  new_lst = []
  for base in bases:
    for power in powers:
      new_lst.append(base ** power)
  return new_lst
print(exponents([2, 3, 4], [1, 2, 3]))

def larger_sum(lst1, lst2):
  sum1 = 0
  sum2 = 0
  for number in lst1:
    sum1 += number
  for number in lst2:
    sum2 += number
  if sum1 >= sum2:
    return lst1
  else:
    return lst2
print(larger_sum([1, 9, 5], [2, 3, 7]))

def over_nine_thousand(lst):
  sum1 = 0
  for i in lst:
    sum1 += i
    if sum1 > 9000:
      break
  return sum1

print(over_nine_thousand([8000, 900, 120, 5000]))

def max_num(nums):
  maximum = nums[0]
  for number in nums:
    if number > maximum:
      maximum = number
  return maximum
print(max_num([50, -10, 0, 75, 20]))

def same_values(lst1, lst2):
  new_lst = []
  for index in range(len(lst1)):
    if lst1[index] == lst2[index]:
      new_lst.append(index)
  return new_lst
print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))


#Write your function here
def reversed_list(lst1, lst2):
  for index in range(len(lst1)):
    if lst1[index] != lst2[len(lst2) - 1 - index]:
      return False
  return True
#Uncomment the lines below when your function is done
print(reversed_list([1, 2, 3], [3, 2, 1]))
print(reversed_list([1, 5, 3], [3, 2, 1]))

first_name = "Julie"
last_name = "Blevins"
def account_generator(first_name, last_name):
  account_name = first_name[:3] + last_name[:3]
  return account_name
new_account = account_generator(first_name, last_name)

print(new_account)

first_name = "Reiko"
last_name = "Matsuki"
def password_generator(first_name, last_name):
  f = len(first_name)
  l = len(last_name)
  return  first_name[f-3:] + last_name[l-3:]

temp_password = password_generator(first_name, last_name)
print(temp_password)

company_motto = "Copeland's Corporate Company helps you capably cope with the constant cacophony of daily life"
second_to_last = company_motto[-2]
final_word = company_motto[-4:]
first_name = "Bob"
last_name = "Daily"
#first_name[0] = "R"
new_name = first_name[1:]
#print(new_name)
fixed_first_name = "R"+ new_name
print(fixed_first_name)

password = "theycallme\"crazy\"91"
print(password)

def get_length(word):
  counter = 0
  for letter in word:
    counter += 1
  return counter

def letter_check(word, letter):
  for character in word:
    if character == letter:
      return True
  return False

def contains(big_string, little_string):
  if little_string in big_string:
    return True
  else:
    return False

def contains(big_string, little_string):
  return little_string in big_string

def common_letters(string_one, string_two):
  common = []
  for letter in string_one:
    if (letter in string_two) and not (letter in common):
      common.append(letter)
  return common

def username_generator(first_name, last_name):
  f = first_name[:3]
  l = last_name[:4]
  if len(first_name) < len(f):
    return first_name
  if len(last_name) < len(l):
    return last_name
  username = f + l
  return username
def username_generator(first_name, last_name):
    if len(first_name) < 3:
        user_name = first_name
    else:
        user_name = first_name[0:3]
    if len(last_name) < 4:
        user_name += last_name
    else:
        user_name += last_name[0:4]
    return user_name

def password_generator(user_name):
    password = ""
    for i in range(0, len(user_name)):
        password += user_name[i-1]
    return password

poem_title = "spring storm"
poem_author = "William Carlos Williams"
poem_title_fixed = poem_title.title()
print(poem_title)
print(poem_title_fixed)
poem_author_fixed = poem_author.upper()
print(poem_author)
print(poem_author_fixed)

line_one = "The sky has given over"
line_one_words =line_one.split()
print(line_one_words)

authors = "Audre Lorde,Gabriela Mistral,Jean Toomer,An Qi,Walt Whitman,Shel Silverstein,Carmen Boullosa,Kamala Suraiyya,Langston Hughes,Adrienne Rich,Nikki Giovanni"

author_names = authors.split(',')

print(author_names)

author_last_names = []
for name in author_names:
  author_last_names.append(name.split()[-1])

print(author_last_names)
#spring_storm_lines = spring_storm_text.split("\n")

reapers_line_one_words = ["Black", "reapers", "with", "the", "sound", "of", "steel", "on", "stones"]
#The below join method joins the list with a space in between each entry
reapers_line_one = ' '.join(reapers_line_one_words)
print(reapers_line_one)

winter_trees_lines = ['All the complicated details', 'of the attiring and', 'the disattiring are completed!', 'A liquid moon', 'moves gently among', 'the long branches.', 'Thus having prepared their buds', 'against a sure winter', 'the wise trees', 'stand sleeping in the cold.']
winter_trees_full = "\n".join(winter_trees_lines)
print(winter_trees_full)

love_maybe_lines = ['Always    ', '     in the middle of our bloodiest battles  ', 'you lay down your arms', '           like flowering mines    ','\n' ,'   to conquer me home.    ']


love_maybe_lines_stripped = []

for line in love_maybe_lines:
  love_maybe_lines_stripped.append(line.strip())

love_maybe_full = '\n'.join(love_maybe_lines_stripped)

print(love_maybe_full)

toomer_bio = \
"""
Nathan Pinchback Tomer, who adopted the name Jean Tomer early in his literary career, was born in Washington, D.C. in 1894. Jean is the son of Nathan Tomer was a mixed-race freedman, born into slavery in 1839 in Chatham County, North Carolina. Jean Tomer is most well known for his first book Cane, which vividly portrays the life of African-Americans in southern farmlands.
"""

toomer_bio_fixed = toomer_bio.replace("Tomer", "Toomer")
print(toomer_bio_fixed)

god_wills_it_line_one = "The very earth will disown you"
disown_placement = god_wills_it_line_one.find("disown")
print(disown_placement)

def favorite_song_statement(song, artist):
  return "My favorite song is {} by {}.".format(song, artist)


def poem_title_card(poet, title):
  return "The poem \"{}\" is written by {}.".format(title, poet)
a = poem_title_card("Walt Whitman", "I Hear America Singing")
print(a)

def favorite_song_statement(song, artist):
    return "My favorite song is {song} by {artist}.".format(song=song, artist=artist)

def poem_description(publishing_date, author, title, original_work):
  poem_desc = "The poem {title} by {author} was originally published in {original_work} in {publishing_date}.".format(publishing_date=publishing_date, author=author, title=title, original_work=original_work)
  return poem_desc
my_beard_description = poem_description(author = "Shel Silverstein",
title = "My Beard",
original_work = "Where the Sidewalk Ends",
publishing_date = "1974")
print(my_beard_description)

highlighted_poems = "Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, Dreamwood:Adrienne Rich:1987"
print(highlighted_poems)
highlighted_poems_list = highlighted_poems.split(",")
print("\n")
print(highlighted_poems_list)
highlighted_poems_stripped = []
for spaces in highlighted_poems_list:
  highlighted_poems_stripped.append(spaces.strip(" "))
  print("\n")
print(highlighted_poems_stripped)

highlighted_poems_details = []
for item in highlighted_poems_stripped:
  highlighted_poems_details.append(item.split(":"))
print("\n")
print(highlighted_poems_details)
print("\n")
titles = []
poets = []
dates = []
for item in highlighted_poems_details:
  titles.append(item[0])
  poets.append(item[1])
  dates.append(item[2])

print(titles)
print("\n")
print(poets)
print("\n")
print(dates)
print("\n")

'''
def final_word(title, poets, dates):
  for item in titles:
  	for item in poets:
     	for item in dates:
 	return "The poem {} was published by {} in {}".format(titles, poets, dates)
 '''
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
def unique_english_letters(word):
  uniques = 0
  for letter in letters:
    if letter in word:
      uniques += 1
  return uniques
print(unique_english_letters("mississippi"))
print(unique_english_letters("Apple"))
def count_char_x(word, x):
  x_count = 0
  for i in word:
    if i == x:
      x_count += 1
  return x_count
print(count_char_x("mississippi", "s"))
print(count_char_x("mississippi", "m"))

def count_multi_char_x(word, x):
  splits = word.split(x)
  return(len(splits)-1)
print(count_multi_char_x("mississippi", "iss"))
print(count_multi_char_x("apple", "pp"))

def substring_between_letters(word, start, end):
  a = word.find(start)
  b = word.find(end)
  for i in word:
    if a == -1 or b == -1:
      return word
  return word[a+1:b]
print(substring_between_letters("apple", "p", "e"))
# should print "pl"
print(substring_between_letters("apple", "p", "c"))
# should print "apple"

def x_length_words(word, x):
  sentence_list = word.split()
  for i in sentence_list:
    if len(str(i)) < x:
      return False
  return True
print(x_length_words("i like apples", 2))
# should print False
print(x_length_words("he likes apples", 2))
# should print True

def check_for_name(sentence, name):
  return name.lower() in sentence.lower()

print(check_for_name("My name is Jamie", "Jamie"))

def every_other_letter(word):
  every_other = ""
  for i in range(0, len(word), 2):
    every_other += word[i]
  return every_other
print(every_other_letter("Codecademy"))
# should print Cdcdm
print(every_other_letter("Hello world!"))
# should print Hlowrd
print(every_other_letter(""))

def make_spoonerism(word1, word2):
  return word2[0]+word1[1:]+" "+word1[0]+word2[1:]

print(make_spoonerism("Codecademy", "Learn"))
# should print Lodecademy Cearn
print(make_spoonerism("Hello", "world!"))
# should print wello Horld!
print(make_spoonerism("a", "b"))
# should print b a


def add_exclamation(word):
  while len(word) < 20:
    word += "!"
  return word

print(add_exclamation("Codecademy"))
# should print Codecademy!!!!!!!!!!
print(add_exclamation("Codecademy is the best place to learn"))
# should print Codecademy is the best place to learn

from datetime import datetime
current_time = datetime.now()
print(current_time)


import random
random_list = [random.randint(1,300) for i in range(101)]
randomer_number = random.choice(random_list)
print(randomer_number)

#import codecademylib3_seaborn
#from matplotlib import pyplot as plt
#import random
#numbers_a = range(1, 13)
#numbers_b = range(12)
#plt.plot(numbers_a, numbers_b)
#plt.show()


#This function is used to handle functions that deals with money and floats
#It prints out the appropriate number in two decimal places.
from decimal import Decimal
two_decimal_points = Decimal('0.2') + Decimal('0.69')
print(two_decimal_points)
four_decimal_points = Decimal('0.53') + Decimal('0.65')
print(four_decimal_points)

animals_in_zoo = {}
animals_in_zoo["zebras"] = 8
animals_in_zoo["monkeys"] = 12
animals_in_zoo["dinosaurs"] = 0
print(animals_in_zoo)

user_ids = {"teraCoder": 9018293, "proProgrammer": 119238}
user_ids.update({"theLooper": 138475, "stringQueen": 85739})
print(user_ids)

oscar_winners = {"Best Picture": "La La Land", "Best Actor": "Casey Affleck", "Best Actress": "Emma Stone", "Animated Feature": "Zootopia"}
oscar_winners["Supporting Actress"] = "Viola Davis"
oscar_winners["Best Picture"] = "Moonlight"

drinks = ["espresso", "chai", "decaf", "drip"]
caffeine = [64, 40, 0, 120]
zipped_drinks = zip(drinks, caffeine)
drinks_to_caffeine = {drinks: caffeine for drinks, caffeine in zipped_drinks}
print(drinks_to_caffeine)

songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]
playcounts = [78, 29, 44, 21, 89, 5]
zipped_play_list = zip(songs, playcounts)
plays = {songs: playcounts for songs, playcounts in zipped_play_list}
print(plays)
plays["Purple Haze"] = 1
plays["Respect"] = 94
library = {}
library["The Best Songs"] = plays
library["Sunday Feelings"] = {}
print(library)

zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"], "fire": ["Aries", "Leo", "Sagittarius"], "earth": ["Taurus", "Virgo", "Capricorn"], "air":["Gemini", "Libra", "Aquarius"]}
print(zodiac_elements["earth"])
print(zodiac_elements["fire"])

zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"], "fire": ["Aries", "Leo", "Sagittarius"], "earth": ["Taurus", "Virgo", "Capricorn"], "air":["Gemini", "Libra", "Aquarius"]}
zodiac_elements["energy"] = "Not a Zodiac element"
print(zodiac_elements["energy"])

caffeine_level = {"espresso": 64, "chai": 40, "decaf": 0, "drip": 120, "matcha": 30}
try:
  print(caffeine_level["cass"])
except KeyError:
  print("Unknown Caffeine level")

user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}
tc_id = user_ids.get("teraCoder", 100000)
print(tc_id)
stack_id = user_ids.get("superStackSmash", 100000)
print(stack_id)

available_items = {"health potion": 10, "cake of the cure": 5, "green elixir": 20, "strength sandwich": 25, "stamina grains": 15, "power stew": 30}
health_points = 20

health_points += available_items.pop("stamina grains", 0)
health_points += available_items.pop("power stew", 0)
health_points += available_items.pop("mystic bread", 0)

print(available_items)
print(health_points)

user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}
num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}

users = user_ids.keys()
lessons = num_exercises.keys()
print(users)
print(lessons)

num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}
total_exercises = 0
for i in num_exercises.values():
  total_exercises += i
print(total_exercises)

pct_women_in_occupation = {"CEO": 28, "Engineering Manager": 9, "Pharmacist": 58, "Physician": 40, "Lawyer": 37, "Aerospace Engineer": 9}
for position, percentage in pct_women_in_occupation.items():
  print("Women make up "+ str(pct_women_in_occupation) +" percent of "+ position)

pct_women_in_occupation = {"CEO": 28, "Engineering Manager": 9, "Pharmacist": 58, "Physician": 40, "Lawyer": 37, "Aerospace Engineer": 9}
for position, percentage in pct_women_in_occupation.items():
  print("Women make up "+ str(percentage) +" percent of "+ position+"s.")

tarot = { 1:	"The Magician", 2:	"The High Priestess", 3:	"The Empress", 4:	"The Emperor", 5:	"The Hierophant", 6:	"The Lovers", 7:	"The Chariot", 8:	"Strength", 9:	"The Hermit", 10:	"Wheel of Fortune", 11:	"Justice", 12:	"The Hanged Man", 13:	"Death", 14:	"Temperance", 15:	"The Devil", 16:	"The Tower", 17:	"The Star", 18:	"The Moon", 19:	"The Sun", 20:	"Judgement", 21:	"The World", 22: "The Fool"}
spread = {}
spread["past"] = tarot.pop(20)
spread["present"] = tarot.pop(17)
spread["future"] = tarot.pop(10)
for key, value in spread.items():
  print("Your "+key+" is the "+value+" card. ")


def sum_values(my_dictionary):
  values_sum = 0
  for value in my_dictionary.values():
    values_sum += value
  return values_sum

print(sum_values({"milk":5, "eggs":2, "flour": 3}))
print(sum_values({10:1, 100:2, 1000:3}))

def sum_even_keys(my_dictionary):
  total = 0
  for key in my_dictionary.keys():
    if key%2 == 0:
      total += my_dictionary[key]
  return total
print(sum_even_keys({1:5, 2:2, 3:3}))
# should print 2
print(sum_even_keys({10:1, 100:2, 1000:3}))
# should print 6

def add_ten(my_dictionary):
  for key in my_dictionary.keys():
    my_dictionary[key] += 10
  return my_dictionary
print(add_ten({1:5, 2:2, 3:3}))
# should print {1:15, 2:12, 3:13}
print(add_ten({10:1, 100:2, 1000:3}))
# should print {10:11, 100:12, 1000:13}

def values_that_are_keys(my_dictionary):
  new_list = []
  for value in my_dictionary.values():
    if value in my_dictionary.keys():
      new_list.append(value)
  return new_list
print(values_that_are_keys({1:100, 2:1, 3:4, 4:10}))
# should print [1, 4]
print(values_that_are_keys({"a":"apple", "b":"a", "c":100}))
# should print ["a"]

# Write your max_key function here:
def max_key(my_dictionary):
  largest_key = float("-inf")
  largest_value = float("-inf")
  for key, value in my_dictionary.items():
    if value > largest_value:
      largest_value = value
      largest_key = key
  return largest_key
print(max_key({1:100, 2:1, 3:4, 4:10}))

def word_length_dictionary(words):
  word_lengths = {}
  for word in words:
    word_lengths[word] = len(word)
  return word_lengths

print(word_length_dictionary(["apple", "dog", "cat"]))
# should print {"apple":5, "dog": 3, "cat":3}
print(word_length_dictionary(["a", ""]))
# should print {"a": 1, "": 0}

def frequency_dictionary(words):
  freqs = {}
  for word in words:
    if word not in freqs:
    	freqs[word] = 0
    freqs[word] += 1
  return freqs

# Uncomment these function calls to test your  function:
print(frequency_dictionary(["apple", "apple", "cat", 1]))
# should print {"apple":2, "cat":1, 1:1}
print(frequency_dictionary([0,0,0,0,0]))
# should print {0:5}
def unique_values(my_dictionary):
  seen_values = []
  for value in my_dictionary.values():
    if value not in seen_values:
      seen_values.append(value)
  return len(seen_values)
print(unique_values({0:3, 1:1, 4:1, 5:3}))
# should print 2
print(unique_values({0:3, 1:3, 4:3, 5:3}))
# should print 1

def count_first_letter(names):
  letters = {}
  for key in names:
    first_letter = key[0]
    if first_letter not in letters:
      letters[first_letter] = 0
    letters[first_letter] += len(names[key])
  return letters

# Uncomment these function calls to test your  function:
print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Lannister": ["Jaime", "Cersei", "Tywin"]}))
# should print {"S": 4, "L": 3}
print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Sannister": ["Jaime", "Cersei", "Tywin"]}))
# should print {"S": 7}

#The next lesson is about how to open and read a file.
#Read, return the entire file in one text
with open("welcome.txt") as text_file:
  text_data = text_file.read()
  print(text_data)
#Readlines, return the text in the file line by line in a variable for all lines.
with open('how_many_lines.txt') as lines_doc:
  for line in lines_doc.readlines():
    print(line)
#Readline, returns the text perline, just one line
with open('just_the_first.txt') as first_line_doc:
  first_line = first_line_doc.readline()
  print(first_line)


#creating a new fila and Writting to the file
with open('bad_bands.txt', 'w') as bad_bands_doc:
  bad_bands_doc.write('Styl Plus!')

#Argument a means append to the file without overwriting the file
with open('cool_dogs.txt', 'a') as cool_dogs_file:
  cool_dogs_file.write('Air Buddy')

with open('logger.csv') as log_csv_file:
  logger_file = log_csv_file.read()
  print(logger_file)


import csv

with open('cool_csv.csv') as cool_csv_file:
  cool_csv_dict = csv.DictReader(cool_csv_file)
  for row in cool_csv_dict:
    print(row['Cool Fact'])




import csv
with open('books.csv') as books_csv:
  books_reader = csv.DictReader(books_csv, delimiter='@')
  isbn_list = [book['ISBN'] for book in books_reader]




access_log = [{'time': '08:39:37', 'limit': 844404, 'address': '1.227.124.181'},
              {'time': '13:13:35', 'limit': 543871, 'address': '198.51.139.193'},
              {'time': '19:40:45', 'limit': 3021, 'address': '172.1.254.208'},
              {'time': '18:57:16', 'limit': 67031769, 'address': '172.58.247.219'},
              {'time': '21:17:13', 'limit': 9083, 'address': '124.144.20.113'},
              {'time': '23:34:17', 'limit': 65913, 'address': '203.236.149.220'},
              {'time': '13:58:05', 'limit': 1541474, 'address': '192.52.206.76'},
              {'time': '10:52:00', 'limit': 11465607, 'address': '104.47.149.93'},
              {'time': '14:56:12', 'limit': 109, 'address': '192.31.185.7'},
              {'time': '18:56:35', 'limit': 6207, 'address': '2.228.164.197'}]
fields = ['time', 'address', 'limit']

import csv

with open('logger.csv', 'w') as logger_csv:
  log_writer = csv.DictWriter(logger_csv, fieldnames=fields)
  log_writer.writeheader()
  for data in access_log:
    log_writer.writerow(data)

import json

with open('message.json') as message_json:
  message = json.load(message_json)
  print(message['text'])



data_payload = [
  {'interesting message': 'What is JSON? A web application\'s little pile of secrets.',
   'follow up': 'But enough talk!'}
]

import json

with open('data.json', 'w') as data_json:
  json.dump(data_payload, data_json)


class DistanceConverter:
  kms_in_a_mile = 1.609
  def how_many_kms(self, miles):
    return miles * self.kms_in_a_mile

converter = DistanceConverter()
kms_in_5_miles = converter.how_many_kms(5)
print(kms_in_5_miles)
# prints "8.045"


class Circle:
  pi = 3.14

  def area(self, radius):
    return self.pi * radius ** 2

circle = Circle()
pizza_area = circle.area(12 / 2)
teaching_table_area = circle.area(36 / 2)
round_room_area = circle.area(11460 / 2)


class Circle:
  pi = 3.14

  # Add constructor here:
  def __init__(self, diameter):
    print("New circle with diameter: {diameter}".format(diameter=diameter))


teaching_table = Circle(36)


class Store:
  pass

alternative_rocks = Store()
isabelles_ices = Store()

alternative_rocks.store_name = "Alternative Rocks"
isabelles_ices.store_name = "Isabelle's Ices"


how_many_s = [{'s': False}, "sassafrass", 18, ["a", "c", "s", "d", "s"]]

for element in how_many_s:
  if hasattr(element, "count"):
    print(element.count("s"))

class SearchEngineEntry:
  def __init__(self, url):
    self.url = url

codecademy = SearchEngineEntry("www.codecademy.com")
wikipedia = SearchEngineEntry("www.wikipedia.org")

print(codecademy.url)
# prints "www.codecademy.com"

print(wikipedia.url)
# prints "www.wikipedia.org"


class SearchEngineEntry:
  secure_prefix = "https://"
  def __init__(self, url):
    self.url = url

  def secure(self):
    return "{prefix}{site}".format(prefix=self.secure_prefix, site=self.url)

codecademy = SearchEngineEntry("www.codecademy.com")

print(codecademy.secure())
# prints "https://www.codecademy.com"

print(wikipedia.secure())
# prints "https://www.wikipedia.org"


class Circle:
  pi = 3.14

  def __init__(self, diameter):
    print("Creating circle with diameter {d}".format(d=diameter))
    # Add assignment for self.radius here:

    self.radius = diameter / 2

  def circumference(self):
    return 2 * self.pi * self.radius


medium_pizza = Circle(12)
teaching_table = Circle(36)
round_room = Circle(11460)

print(medium_pizza.circumference())
print(teaching_table.circumference())
print(round_room.circumference())



print(dir(5))

def this_function_is_an_object(num):
  return "Cheese is {} times better than everything else".format(num)

print(dir(this_function_is_an_object))


class Circle:
  pi = 3.14

  def __init__(self, diameter):
    self.radius = diameter / 2

  def area(self):
    return self.pi * self.radius ** 2

  def circumference(self):
    return self.pi * 2 * self.radius

  def __repr__(self):
    return "Circle with radius {radius}".format(radius=self.radius)


medium_pizza = Circle(12)
teaching_table = Circle(36)
round_room = Circle(11460)

print(medium_pizza)
print(teaching_table)
print(round_room)



class OutOfStock(Exception):
  pass


# Update the class below to raise OutOfStock
class CandleShop:
  name = "Here's a Hot Tip: Buy Drip Candles"

  def __init__(self, stock):
    self.stock = stock

  def buy(self, color):
    if self.stock[color] < 1:
      raise OutOfStock
    self.stock[color] = self.stock[color] - 1


candle_shop = CandleShop({'blue': 6, 'red': 2, 'green': 0})
candle_shop.buy('blue')

# This should raise OutOfStock:
# candle_shop.buy('green')


class Message:
  def __init__(self, sender, recipient, text):
    self.sender = sender
    self.recipient = recipient
    self.text = text


class User:
  def __init__(self, username):
    self.username = username

  def edit_message(self, message, new_text):
    if message.sender == self.username:
      message.text = new_text


class Admin(User):
  def edit_message(self, message, new_text):
    message.text = new_text


class PotatoSalad:
  def __init__(self, potatoes, celery, onions):
    self.potatoes = potatoes
    self.celery = celery
    self.onions = onions


class SpecialPotatoSalad(PotatoSalad):
  def __init__(self, potatoes, celery, onions):
    super().__init__(potatoes, celery, onions)
    self.raisins = 40


class Chess:
  def __init__(self):
    self.board = setup_board()
    self.pieces = add_chess_pieces()

  def play(self):
    print("Playing chess!")

class Checkers:
  def __init__(self):
    self.board = setup_board()
    self.pieces = add_checkers_pieces()

  def play(self):
    print("Playing checkers!")

def play_game(chess_or_checkers):
  chess_or_checkers.play()

chess_game = Chess()
checkers_game = Checkers()
chess_game_2 = Chess()

for game in [chess_game, checkers_game, chess_game_2]:
  play_game(game)
"""
Prints out the following:
Playing chess!
Playing checkers!
Playing chess!
"""

class InsurancePolicy:
  def __init__(self, price_of_item):
    self.price_of_insured_item = price_of_item

class VehicleInsurance(InsurancePolicy):
  def get_rate(self):
    return self.price_of_insured_item * .001

class HomeInsurance(InsurancePolicy):
  def get_rate(self):
    return self.price_of_insured_item * .00005



class Color:
  def __init__(self, red, blue, green):
    self.red = red
    self.blue = blue
    self.green = green

  def __repr__(self):
    return "Color with RGB = ({red}, {blue}, {green})".format(red=self.red, blue=self.blue, green=self.green)

  def add(self, other):
    """
    Adds two RGB colors together
    Maximum value is 255
    """
    new_red = min(self.red + other.red, 255)
    new_blue = min(self.blue + other.blue, 255)
    new_green = min(self.green + other.green, 255)

    return Color(new_red, new_blue, new_green)

red = Color(255, 0, 0)
blue = Color(0, 255, 0)

magenta = red.add(blue)
print(magenta)
# Prints "Color with RGB = (255, 255, 0)"

import os

def make_folders(folders_list, nest=False):
  if nest:
    """
    Nest all the folders, like
    ./Music/fun/parliament
    """
    path_to_new_folder = ""
    for folder in folders_list:
      path_to_new_folder += "/{}".format(folder)
      try:
        os.makedirs(path_to_new_folder)
      except FileExistsError:
        continue
  else:
    """
    Makes all different folders, like
    ./Music/ ./fun/ and ./parliament/
    """
    for folder in folders_list:
      try:
        os.makedirs(folder)

      except FileExistsError:
        continue

make_folders(['./Music', './fun', './parliament'])


def scream_and_whisper(text):
  scream = text.upper()
  whisper = text.lower()
  return scream, whisper


the_scream, the_whisper = scream_and_whisper("Hello There!")
print(the_scream)
print(the_whisper)



from os.path import join

path_segment_1 = "/Home/User"
path_segment_2 = "Codecademy/videos"
path_segment_3 = "cat_videos/surprised_cat.mp4"

# join all three of the paths here!
print(join(path_segment_1, path_segment_2, path_segment_3))


print("My name is {name} and I'm feeling {feeling}.".format(
	name="Tim",
  feeling="10/10",
))

# Checkpoint 2
from products import create_product

# Update create_products() to take arbitrary keyword arguments
def create_products(**products_dict):
  for name, price in products_dict.items():
    create_product(name, price)

# Checkpoint 3
# Update the call to `create_products()` to pass in this dictionary as a series of keyword
create_products(
  Baseball='3',
  Shirt='14',
  Guitar='70')


def main(filename, *args, user_list=None, **kwargs):
  if user_list is None:
    user_list = []

  if '-a' in args:
    user_list = all_users()

  if kwargs.get('active'):
    user_list = [user for user_list if user.active]

  with open(filename) as user_file:
    user_file.write(user_list)

  from products import create_product

  def create_products(**products_dict):
    for name, price in products_dict.items():
      create_product(name, price)

  new_product_dict = {
    'Apple': 1,
    'Ice Cream': 3,
    'Chocolate': 5,
  }

  # Call create_product() by passing new_product_dict
  # as kwargs!
  create_products(**new_product_dict)


def create_product(name, price):
  print("{} created, being sold for ${}".format(name, price))

def item_summer(*args):
  current_sum = 0
  for arg in args:
    current_sum += arg
  return current_sum

my_list = [5, 19, 23, 88]

item_summer(*my_list)


def unite_args(*args):
  new_string = ""
  for arg in args:
    new_string += arg
  return new_string


print(unite_args("I'm ", "here ", "for ", "this "))

def return_translated_point(x, y, change_x, change_y):
  return x + change_x, y + change_y

a, b = return_translated_point(1, 2, 5, 8)
print(b)

from math import sin, cos, atan2, sqrt

def get_distance(from_lat, from_long, to_lat, to_long):
  dlon = to_long - from_long
  dlat = from_lat - to_lat
  a = (sin(dlat/2)) ** 2 + cos(from_lat) * cos(to_lat) * (sin(dlon/2)) ** 2
  c = 2 * atan2(sqrt(a), sqrt(1-a))
  distance = a * c
  return distance

SHIPPING_PRICES = {
  'Ground': 1,
  'Priority': 1.6,
  'Overnight': 2.3,
}

def format_price(price):
  return "${0:.2f}".format(price)


def get_math_function(operation): #+ or -
  def add(n1, n2):
    return n1 + n2
  def sub(n1, n2):
    return n1 - n2

  if operation == '+':
    return add
  elif operation == '-':
    return sub

add_function = get_math_function('+')
sub_function = get_math_function('-')
print(sub_function(4, 6))
print(add_function(3, 5))


def title_decorator(print_name_function):
  def wrapper():
    print("Production Network Engineer")
    print_name_function()

  return wrapper

@title_decorator
def print_my_name():
  print('Ernest')

@title_decorator
def print_my_lastname():
  print('Ogbuanya')

print_my_name()
print_my_lastname()

decorated_function = title_decorator(print_my_name)
decorated_lastname = title_decorator(print_my_lastname)
decorated_function()
decorated_lastname()


from matplotlib import pyplot as plt
import random
numbers_a = range(1, 13)
numbers_b = random.sample(range(1000), 12)
plt.plot(numbers_a, numbers_b)
plt.show()

import csv

list_of_email_addresses = []
with open('users.csv', newline='') as users_csv:
  user_reader = csv.DictReader(users_csv)
  for row in user_reader:
    list_of_email_addresses.append(row['Email'])

import csv

with open('books.csv') as books_csv:
  books_reader = csv.DictReader(books_csv, delimiter='@')
  isbn_list = [book['ISBN'] for book in books_reader]

access_log = [{'time': '08:39:37', 'limit': 844404, 'address': '1.227.124.181'}, {'time': '13:13:35', 'limit': 543871, 'address': '198.51.139.193'}, {'time': '19:40:45', 'limit': 3021, 'address': '172.1.254.208'}, {'time': '18:57:16', 'limit': 67031769, 'address': '172.58.247.219'}, {'time': '21:17:13', 'limit': 9083, 'address': '124.144.20.113'}, {'time': '23:34:17', 'limit': 65913, 'address': '203.236.149.220'}, {'time': '13:58:05', 'limit': 1541474, 'address': '192.52.206.76'}, {'time': '10:52:00', 'limit': 11465607, 'address': '104.47.149.93'}, {'time': '14:56:12', 'limit': 109, 'address': '192.31.185.7'}, {'time': '18:56:35', 'limit': 6207, 'address': '2.228.164.197'}]
fields = ['time', 'address', 'limit']

import csv

with open('logger.csv', 'w') as logger_csv:
  log_writer = csv.DictWriter(logger_csv, fieldnames=fields)
  log_writer.writeheader()
  for line in access_log:
    log_writer.writerow(line)

data_payload = [
  {'interesting message': 'What is JSON? A web application\'s little pile of secrets.',
   'follow up': 'But enough talk!'}
]

import json

with open('data.json', 'w') as data_json:
  json.dump(data_payload, data_json)
