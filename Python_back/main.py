print("Hello to quizz game")

playing = input("Do you want play quizz? ")

if playing.lower() != "yes": 
    quit()

print("Let's play!!!")
Score = 0

answer = input("What does CPU stand for? ").lower()
if answer == "central processing unit":
    print("Nice")
    Score += 1
else:
    print("That Bad")

answer = input("What does CPU stand for? ").lower()
if answer == "central processing unit":
    print("Nice")
    Score += 1
else:
    print("That Bad")

answer = input("What does CPU stand for? ").lower()
if answer == "central processing unit":
    print("Nice")
    Score += 1
else:
    print("That Bad")        

print("You got " + str(Score) + " Score!!")
print("You got " + str((Score / 3) * 100) + " %")