#The "print" function displays whatever is in the parenthesis. Ex. Strings, variables, etc.
#print('Hello World!')
#age = 20
#price = 19.95
#first_name = "Josh"
#Booleans (true or false) must have a capital letter in the begining.
#is_online = False


#EXCERSICE:
#age = 20
#first_name = "John Smith"
#new_patient = True
#print(age,first_name,new_patient)


#input is for user interactions. Inputs anything typed in the terminal. If you put something before the equal sign it is considered a variable that changes with the input.
#name = input("What is your name? ")
#print("Hello "+ name)



#Here we are using type conversion to calculate the age of the person with the birth_year variable. we used the - int(x) to change the string into an int value.
#birth_year = input("Input your birth year")
#age = 2022-int(birth_year)
#print(age)



#Float is a data type which is a decimal. It is like a double in java but with a different name. Ex. 10.1, 67.7
#int()
#float()
#bool()
#str()


#EXCERCISE 2
#first = input("First: ")
#second = input("Second: ")
#To Convert a string to any other kind of data type, on the math/execute line, use content from line 31-34
#sum = float(first) + float(second)
#print("Sum = " + str(sum))


#Methods. Below is a method called upper which changes a variable to all upercase.
#course = "Python for beginners"
#print(course.upper())
#print(course.lower())
#Below is the find method, which sees if the string contains a certain character.
#print(course.find("y"))
#You can put replace before the find to replace the character or the parameters with whatever you want.
#print(course.replace("for", "4"))
#Below is the in operator which is expressed with "in". This will return a boolean (true or false) answer to see if the string entered is true or false.
#print("Python" in course)





#ARITHMETIC OPERATIONS
#you can use the following to calculate numbers. For example, +, -, *, /, //
#The double division gives an integer instead of a float value.
#print(10 + 3)
#print(14 * 4)
#print(31 - 65)
#print(45/2.3)
#print(45//2.3)
#the % gives the remainder of the division problem.
#print(32%6.3)
#Exponents are displayed using double asterisks.
#print(4**3)
#Augmented assignment operator "x+=x" is something that increments by any value
#x = 10
#x+=3
#print(x)





#OPERATOR PRECEDENCE
#Order of operations and shit. You get it.
#x = 10 + 3 * 2





#COMPARISON OPERATORS 
#It compares numbers and gives a boolean value
#You can use >, <, >=, <=, ==, !=
#== expresses value equality. != indicates not equality.
#x = 3 > 2
#y = 3 == 4
#z = 3 !=4
#print(x)
#print(y)
#print(z)






#LOGICAL OPERATORS
#logical operators are operators that can be used to build complex rules and conditions.
#this will see if all of the parameters that are inside the parenthesis are true or false.
#price = 25
#print(price > 10 and price < 30)
#or statements will display a boolean if one of the statements are true
#price = 30
#print(price > 10 or price < 1)
#Not operator will inverse the boolean value.





#IF STATEMENTS
#If statements execute what ever is after the word if or elif (parenthesis optional). If statements are only used once.
#elif is the else if
#temp = 20
#if (temp > 70):
#  print("It's gonna be a hot day!")
#elif (temp > 60):
#  print("It's a nice day.")
#elif (temp > 40):
#  print("It's a bit cold.")
#Else statement is executed when none of the if or elif conditions are met.
#else:
#  print("Jet your jackets!")
#  print("It's pretty cold!")
#print("Done")





#IF STATEMENT EXCERSICE.
#weight = int(input("Weight: "))
#unit = input ("Kilograms or Lbs? Type K for kilograms or L for lbs: ")
#if unit.upper == "K":
#  converted = weight / 0.45
#  print("In pounds you weigh: " + str(converted))
#else:
#  converted2 = weight * 0.45
#  print("In Kgs you weigh: " + str(converted2))





#WHILE LOOPS
#While loops end until a certain specification is met.
#i = 1
#while i <= 10:
#  print(i * "*")
#  i = i + 1






#LISTS
#lists are things that can have multiple things inside it. Square brackets are used.
#names = ["John", "Mary", "Chuck", "Pedro"]
#print(names)
#you can print a certain index in the list with the first one being zero.
#print(names[0])
#You can change an object in a list with the line below
#names[0] = "Jon"