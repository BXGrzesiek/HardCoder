#Write a program that asks the user for age and then displays the following subtitles:
#Great! Now you have <age should appear here>!
#Next year you will have: <here should be the age for the year>#

print("HOW OLD ARE YOU? : ", end="")
age = input()
print("Great! Now you have: " + str(age) + "!")
#print(type(age)) #str
print("Next year you will have: "+ str(int(age)+1) + "!") #double change type from str=>int=>str