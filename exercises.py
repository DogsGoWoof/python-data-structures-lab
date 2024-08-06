# Exercise 0: Example
#
# This is a practice exercise to familiarize you with basic Python data structures.
#
# Create a list called `example_list` and append three elements to it. Print each element using a loop.
#
# Requirements:
# - The list should contain any three elements of your choice.
# - Use a loop to print each element.

def example_list_function():
    example_list = ['element1', 'element2', 'element3']
    # appending_approval = ['Earth', 'Wind', 'Water', 'Fire']
    # example_list += appending_approval
    example_list.append('Wolfram')
    example_list.append('Hydrogen')
    example_list.append('Carbon')

    for element in example_list:
        print(element)

# Call the function and print each element
print('Exercise 0:')
example_list_function()
print()


# Exercise 1: List and Indexing
#
# Create a list named students containing at least three student names (strings).
# Assign the second student’s name to a variable named first_student.
# Assign the last student’s name to a variable named last_student.

def manage_students():
    # your code here
    students = ['TJ', 'Spinelli', 'Gretchen']
    first_student = students[1]
    last_student = students[-1]
    return first_student, last_student

# Call the function and print the result
print('Exercise 1:', manage_students())
print()



# Exercise 2: Loop and String Concatenation
#
# Create a tuple named foods containing the same number of foods (strings) as there are names in the students list.
# Create a variable named meal and assign an empty string to it.
# Use a for loop to iterate over the strings in foods and append each string to meal.

foods = ('Winger Dinger', 'Scooby Snacks', 'Senzu Bean') # moved variable declaration outside of function for Exercise 3

def combine_foods():
    # your code here
    meal = ''
    # meal = ' '.join(foods)
    for food in foods:
        # if food == foods[-1]:
        #     meal += food
        # else: meal += f'{food} '
        meal += food
    return meal


# Call the function and print the result
print('Exercise 2:', combine_foods())
print()



# Exercise 3: Slicing Tuples
#
# Using the slice operator, assign a new tuple containing only the last two food strings in the foods to a variable named last_two_foods.

def slice_foods():
    # your code here
    last_two_foods = (foods[1:])
    # last_two_foods = (foods[:0:-1])
    return last_two_foods

# Call the function and print the result
print('Exercise 3:', slice_foods())
print()



# Exercise 4: Dictionaries and String Formatting
#
# Create a dictionary named home_town containing the keys of city, state, and population.
# Using the home_town dictionary, assign to a variable named home_town_message a string with this format: “I was born in <city>, <state> - population of <population>”

home_town = {
    'city': 'Springfield',
    'state': 'Oregon',
    'population': 30720,
    }

def hometown_info():
    # your code here
    home_town_message = f"I was born in {home_town['city']}, {home_town['state']} - population of {home_town['population']}."
    return home_town_message

# Call the function and print the result
print('Exercise 4:', hometown_info())
print()



# Exercise 5: Iterating Over Dictionary Items
#
# Define an empty list named home_town_items.
# Use a for loop to iterate over the key: value pairs in the home_town dictionary and append a string with the following format to home_town_items: "<key> = <value>"

def list_home_town_items():
    # your code here
    home_town_items = []
    # for key, value in home_town.items():
    #     home_town_items.append(f'{key} = {value}')
    for item in home_town:
        home_town_items.append(item + ' = ' + str(home_town[item]))
    return home_town_items

# Call the function and print the result
print('Exercise 5:', list_home_town_items())
