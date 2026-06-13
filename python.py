score = 0
name = input("enter the name :")
print(f"welcome {name} to the quiz!")
print("There is five question each question carry one marks and incorrect answer will not carry any marks")
q1 = input("what is first aroplane name?")

if q1.lower() == "beoing 747":
    print("correct")
    score += 1
    print("your score is",score)
else:
    print("incorrect",score)
    print("the correct answer is boeing 747")
q2 = input("what is first jet india made?")
if q2.lower() == "hal marut":
    print("correct")
    score += 1
    print("your score is",score)
else:
    print("incorrect",score)
    print("the correct answer is hal marut")
q3 =input("name the engine used in hal marut?")
if q3.lower()=="turbojet":
    print("correct")
    score += 1
    print("your score is",score)
else:
    print("incorrect", score)
    print("the correct answer is turbojet")
q4 = input("name the engine used in tejus?")
if q4.lower() == "ge f404":
    print("correct")
    score += 1
    print("your score is",score)
else:
    print("incorrect", score)
    print("the correct answer is ge f404")
q5 = input("name the engine used in su-30mki?")
if q5.lower() == "al-31fp":
    print("correct")
    score += 1
    print("your score is",score)
else:
    print("incorrect", score)
    print("the correct answer is al-31fp")
print("your final score is",score)
percentage = (score/5)*100
print("your percentage is",percentage)
if score == 5:
    print("excellent")
elif score == 4:
    print("very good")
elif score == 3:
    print("good")
elif score == 2:
    print("average")
elif score == 1:
    print("poor")
else:
    print("very poor")
print(name,"thanks for playing the quiz your score is ",score,"percentage is ",percentage)
if percentage >= 80:
    print("Aviation expert")    
elif percentage >= 60:
    print("Aviation enthusiast")
else:
    print("keep learning 😁")
