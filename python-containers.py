# PYTHON CONTAINERS LESSON

#### Pt 1 #####
where_my_things_are = {
  'elk antler': 'attic storage',
  'dustbuster': 'hexagonal table',
  'piggy bank': 'kitchen counter'
}

output = 'My thing is kept in/on the location'
# for key, val in where_my_things_are.items():
#   print(f'My {key} is kept in/on the {val}.')

#### Pt 2 #####
scores = [
  {
    'name': 'fizz',
    'points': 25  # points the player scored
  }
]

scores.append(
  {
    'name': 'will',
    'points': 180001
  }
)

# for player in scores:
#   print(f"{player['name']} scored {player['points']} points.")


#### Lab #####

# Exercise 1
  # Create a list named students containing some student names (strings).
  # Print out the second student’s name.
  # Print out the last student’s name.

students = ['jaquelyn', 'jayce', 'aaron', 'timothy']
print(students[1])
print(students[-1])

# Exercise 2
  # Create a tuple named foods containing the same number of foods (strings) as there are names in the students list.
  # Use a for loop to print out the string “[food goes here] is a good food”.

foods = ('jerky', 'popcorn', 'kimchi', 'injera')
for food in foods:
  print(f'{food} is a good food.')

# Exercise 3
  # Using a for loop, print just the last two food strings from foods.

for food in foods[-2:]:
  print(food)

# Exercise 4
  # Create a dictionary named home_town containing the keys of city, state and population.
  # Print a string with this format:
  # “I was born in city, state - population of population”

home_town = {
  'city': 'Truth or Consequences',
  'state': 'New Mexico',
  'population': 6052,
}

print(f"I was born in {home_town['city']}, {home_town['state']} - population of {home_town['population']}.")


# Exercise 5
  # Iterate over the key: value pairs in home_town and print a string for each item, for example:
  # “city = Arcadia”
  # “state = California”
  # “population = 58000”

for key, val in home_town.items():
  print(f"{key} = {val}")


# Exercise 6

cohort = []

for idx, student in enumerate(students):
  # print(idx, student)
  cohort.append(
    {
      'student': students[idx],
      'fav_food': foods[idx]
    }
  )
  print(cohort)


# Exercise 7
  # Using the list of students and a list comprehension, assign to a variable named awesome_students a new list containing strings similar to this:
  # ["Tina is awesome!", "Fred is awesome!", "Wilma is awesome!"]
  # Iterate over the awesome_students list, printing out each string.

students_praise = [f'{student} is awesome!' for student in students]
print(students_praise)

# Exercise 8
  # Use a for loop to iterate over a list comprehension that filters the foods tuple to only include food strings that contains the letter a.
  # Within the for loop, print each food string.

foods_with_a = [food for food in foods if 'a' in food]
for food in foods_with_a:
  print(food)