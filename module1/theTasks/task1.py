#Task 1 Write a program that will display your
#first name,
#last name,
#age
#and title of your favorite book
#in the following lines (titles should be quoted!)
print("User Data:")
print("|>------------------------------\n|>")
print("|>Please provide Your first name: ", end="")
firstName=input()
print("|>Please provide Your last name: ", end="")
lastName=input()
print("|>How old are you? : ", end="")
userAge=input()
print("|>What is the title of your favorite book? : ", end="")
bookTitle=input()

print("|>______________________________\n"
+ firstName
+ " "
+ lastName
+ "\tAge: "
+ userAge
+ "\nFavorite book: \""
+ bookTitle
+ "\"")