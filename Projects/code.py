# --------------
# Code starts here

# Create the lists 
class_1=['Geoffrey Hinton','Andrew Ng','Sebastian Raschka','Yoshua Bengio']
#print(class_1)
class_2=['Hilary Mason','Carla Gentry','Corinna Cortes']
# Concatenate both the strings
new_class=class_1+class_2
# Append the list
new_class.append('Peter Wardon')
# Print updated list
#print(new_class)
# Remove the element from the list
new_class.remove('Carla Gentry')
# Print the list
#print(new_class)
# Create the Dictionary
courses={'math':65, 'English':70, 'History':80, 'French':70 ,'Science':60}
#print(courses)
# Slice the dict and stores  the all subjects marks in variable
Total=courses['math']+courses['English']+courses['History']+courses['French']+courses['Science']
#print(Total)

# Store the all the subject in one variable `Total`

# Print the total

# Insert percentage formula
percentage=((Total*100)/500)
# Print the percentage
#print(percentage)



# Create the Dictionary
 
mathematics={'Geoffrey Hinton':78, 'Andrew Ng':95, 'Sebastian Raschka':65,'Yoshua Benjio':50, 'Hilary Mason':70, 'Corinna Cortes':66, 'Peter Warden':75}
topper=max(mathematics,key=mathematics.get)
#print(topper)
# Given string
topper.split(sep=" ",maxsplit=1)
# Create variable first_name 
first_name=topper[:6]
#print(first_name)
# Display the results.
last_name=topper[7:9]
#print(last_name)
# Concatenae the string
full_name=last_name+" "+first_name
#print(certificate_name)
# print the full_name
# print the name in upper case
certificate_name=full_name.upper()
print(certificate_name)
# Code ends here


