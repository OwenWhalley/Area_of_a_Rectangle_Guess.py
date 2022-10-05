print("Weclome to the area of a rectangle guessing game")

#Asks the user what the length and width of the rectangle is and assigns the value to the variables.
L = int(input("The length of the rectangle: "))
W = int(input("The width of the rectangle: "))

#Calculates the area of the rectangle. Length * Width.
area = L * W

#Asks the user what they think the area of this rectangle is.
user_answer = int(input("The area of this rectangle = "))

#Uses an if else statement to see if the area they gave is the actual area of the rectangle. If they are equal, it says, "You're right!" If it is not right, it will say the real area of the rectangle.
if area == user_answer:
  print("You're right!")
else:
  print("The real area of the rectangle is: %d" %(area))