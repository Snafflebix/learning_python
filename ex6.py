#this sets variables as strings, with the assigned 10 in x
# being part of the variable - we can have variables within
#string variables! That's cool
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

#this prints x and y
print x #no string-within-string (10 is a number)
print y #this has two strings within a string

#This is different than previously because there are single quote marks
print "I said: %r." % x #this is a s-w-s because x is a string
print "I also said: '%s'." % y #y is a string w two inside,
    # so this is ((two strings) within a string) within a string

#this allows joke_evaluation to have any response you set as a variable
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

#here we combine joke_evaluation with the boolean hilarious
print joke_evaluation % hilarious #not a string-within-string

#again, assigning strings to variables
w = "This is the left side of..."
e = "a string with a right side."

#this combines the two string variables: note, you don't get the space!
print w + e #not a string-within-string
    #this is a longer string because you're adding the variables together
