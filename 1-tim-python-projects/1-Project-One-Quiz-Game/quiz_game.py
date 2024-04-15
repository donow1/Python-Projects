print("Welcome to the game.")

playing = input("Enter the game? (yes/no) ")
if playing.lower() != "yes":
    quit()
print("Great! Let's play!")


score = 0

answer = input("WHat does CPU stand for? ").lower()
if answer == "central processing unit":
    # score = score + 1   while we can use this code, we can also use score += 1
    score += 1
    print("Correct!")
else:
    print("Incorrect!")

answer = input("WHat does GPU stand for? ").lower()
if answer == "graphic processing unit":
    score += 1
    print("Correct!")
else:
    print("Incorrect!")

answer = input("WHat does RAM stand for? ").lower()
if answer == "random access memory":
    score += 1
    print("Correct!")
else:
    print("Incorrect!")

answer = input("WHat does PSU stand for? ").lower()
if answer == "power supply":
    score += 1
    print("Correct!")
else:
    print("Incorrect!")

print(f"You got {score} points, and the correction rate is {(score/4*100)}%")


# python quiz_game.py

# central processing unit    graphic processing unit   random access memory  power supply