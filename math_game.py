# Game first Round
print("Welcome to the Basic Math Game :)")

player = input("Do you want to play? ")

if player.lower() != "yes":
    quit()

print("Okay lets start of with some basic questions")
score = 0

answer = input("What is 2 + 2 ? ")
if answer == str(4):
    print("Correct, Well Done")
    score += 1
else:
    print("Oh no that's Incorrect")

answer = input("\nWhat is 29 + 2 ? ")
if answer == str(31):
    print("Correct, Well Done")
    score += 1
else:
    print("Oh no that's Incorrect")

answer = input("\nWhat is 20 x 10 ? ")
if answer == str(200):
    print("Correct, Well Done completing the first round")
    score += 1
else:
    print("Oh no that's Incorrect")

player = input("\nDo you want to continue to round 2 ? ")

#Game Second Round of questions

if player.lower() != "yes":
    print("\nYou got " + str(score) + " questions correct out of 3!")
    print("\nThankyou for playing")
    quit()

answer = input("\nWhat is 30 x 4 ? ")
if answer == str(120):
    print("Correct, Well Done")
    score += 1
else:
    print("Oh no that's Incorrect")

answer = input("\nWhat is 50 / 2 ? ")
if answer == str(25):
    print("Correct, Well Done")
    score += 1
else:
    print("Oh no that's Incorrect")

print("\nHere's the last Question")

answer = input("\nWhat is 200 / 4 ? ")
if answer == str(31):
    print("Correct, Well Done")
    score += 1
else:
    print("Oh no that's Incorrect")

# Score + Goodbye

print("\nYou got " + str(score) + " questions correct out of 6!")
print("Thankyou for playing!")
