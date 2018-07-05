'''print("Amy")
answer = input("Hello, how are you my friend! ")
print(answer)
print("Your answer: " + answer)
number = int(input("Give me your favorite number "))
if (number % 2 == 0):
    print("You gave me an even number!")
else:
    print("The number is odd!")'''



for i in range(0,5):
    userInput = input("What's your favorite color?")
    print(userInput)
decide = True
while decide:
    answer = input("What's your talent?")
    answer = answer.lower()
    print(answer)
    if answer == "stop":
        decide = False
friends_list = []
for i in range(0,5):
    name = input("Put one of your friends name!")
    friends_list.append(name)
print(friends_list[2])
friends_list.append("Amy")
friends_list.remove(friends_list[1])
print(friends_list)
def addition(firstnum, secondnum):
    total = firstnum + secondnum
    return total
fnum = int(input("Put in the first number to add"))
snum = int(input("Put in the second number to add"))
print(addition(fnum, snum))
