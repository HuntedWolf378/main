#Dylan Wanser
#Integration Project
#SPRINT ONE
#This program demonstrates knowledge and proficiency of concepts learned in
#sprint one so far.

#w3schools
#pynative

#This segment serves as the introduction
print("Hello World!")
print("Welcome to my program!")
print("Lots of time went into this and we're excited to show off round two!")
print("The program might turn out boring still but we think we've got the")
print("skills down to make this great this time around!")
#First variable assigment
username = input("Before we get down into it, please tell me your name: ")
print("Hello", username + "! We're excited to meet you!")
#This segment talks about input and variable operations
print("Please input a variable that you would like to be pasted into")
varOne = input("the blank in the sentence: 'I am having a __ day!': ")
print("I am having a", varOne, "day!")
numOne = (input("Please input a number to be displayed: "))
#Turn this into a loop in which it checks for a number between 1 and 10^^
#Do not turn this into an int(input until ready to check condition
print("The value you chose was", numOne + "!")
#This segment talks about numerical operators
print("This line adds the values 1 + 3")
print(1+3)
print("This line subtracts the values 3 - 1")
print(3-1)
print("This line multiplies the values 2 * 4")
print(2*4)
print("This line divides the values 4 / 2")
print(4/2)
print("This line applies an exponent of 2 to the value of 3")
print("This is also known as 3 to the second power")
#Next segment is non simple numerical operators
print(3 ** 2)
print("This line utilizes floor division. This type of division prints the")
print("value of division without any remainder. The arithmetic we will use is")
print("3 // 2. This would show 1.5 under normal division.")
print(3 // 2)
print("We will use the same numbers again for Modulus. This is an operation")
print("that only shows the remainder of division.")
print(3 % 2)
print("The easiest way to show how modulus works in relation to floor division")
print("is to divide larger, odd numbers by even numbers to show remainder")
print("9 divided by 2 is", 9/2)
print("However 9 divided by 2 using floor division is", 9 // 2)
print("and 9 modulus 2 is", 9 % 2)
print("9 modulus 2 is 1 because using long division for 9/2 results in 4 R1")
#This concludes sprint one
#If/else statements
ifex1 = input("Please input the word 'Computer' ")
#Relational Operator ==
if(ifex1 == "Computer"):
    print("This line prints when the same word is typed.")
else:
    print("This line prints when a different word is typed.")
#Relational Operator =!
ifex3 = input("Please input the word 'Computer' again ")
if(ifex3 != "Computer"):
    print("This line prints when a different word is typed.")
else:
    print("This line prints when the same word is typed.")
#if/else statements with numerical operators
#Relational Operator <
print("This number will serve as the variable in the function 3 < x < 20")
ifex2 = int(input("Please input any number of your choosing "))
if(ifex2 > 3 and ifex2 < 20):
    print("Your value is between 3 and 20")
else:
    print("The number is either less than 3 or greater than 20")
#Elif
#Relational Operators > =< and >=
#boolean and
print("This is a grading scale.")
elifEx2 = int(input("Please enter a number between 0 and 100 "))
if(elifEx2 > 100):
    print("That number is not between 0 and 100.")
elif(elifEx2 <= 100 and elifEx2 > 89):
    print("This is an A")
elif(elifEx2 < 90 and elifEx2 > 79):
    print("This is a B")
elif(elifEx2 < 80 and elifEx2 > 69):
    print("This is a C")
elif(elifEx2 < 70 and elifEx2 > 59):
    print("This is a D")
elif(elifEx2 < 60 and elifEx2 >= 0):
    print("This is a F")
#For loop including in
userword = input("Type a word and this program will split it to separate lines")
for x in userword:
    print(x)
#while loop
print("This will count from whatever number is input to 30.")
whileNum = int(input("Please input a number less than 30 "))
while whileNum <30:
    print(whileNum)
    whileNum += 1
#range
for i in range(5):
    print(i, end=', ')
