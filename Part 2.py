#Example of string concatenation using slices:

captain = "Malcolm Reynolds"
first_name = captain[:8]
last_name = captain[9:]
print(first_name + " 'Mal' " + last_name + " 'Reynolds'")

Output: 'Malcolm 'Mal' Reynolds'

#In this example, we use string concatenation to create a new string that includes the first and last name of the
# character Malcolm Reynolds, but with his nickname 'Mal' in between. We use string slicing to extract the first and
# last name from the original string.

#Example of reversing a string using slices:

ship_name = "Serenity"
reversed_name = ship_name[::-1]
print(reversed_name)

Output: 'ytinereS'

#In this example, we use string slicing to reverse the order of the characters in the string representing the name of
# the spaceship Serenity. We use the step value of -1 to indicate that we want to go backwards through the string.

#Example of checking if a string contains a certain substring using slices:

pilot = "Hoban Washburne"
if "Wash" in pilot[8:]:
    print("The pilot's nickname is 'Wash'.")
else:
    print("The pilot doesn't have a nickname.")

Output: 'The pilot's nickname is 'Wash'.'

#In this example, we use string slicing to check if the substring "Wash" appears in the part of the string that
# represents the pilot's last name. We use the slice pilot[8:] to get the last name part of the string, starting at
# index 8, where the last name begins. We then use the in keyword to check if the substring "Wash" appears in this
# slice of the string.