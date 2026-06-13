score = 0
name = input("enter the name :")
print(f"welcome {name} to the quiz!😄")
print("There is ten question each question carry one marks and incorrect answer will not carry any marks")
q1 = input("what is first aroplane name?✈️")
print("A. Boeing 747")
print("B. Airbus A380")
print("C. Concorde")
print("D. Learjet")

q1 = input("enter your answer: ")

if q1.lower() == "Boeing 747":
    print("correct")
    score += 1
    print("your score is",score)
else:
    print("incorrect",score)
    print("the correct answer is boeing 747")
q2 = input("what is first jet india made?🛩️")
print("A. Sukhoi Su-30MKI")
print("B. HAL Marut")
print("C. Dassault Rafale")
print("D. MiG-29")

q2 = input("enter your answer: ")

if q2.lower() == "HAL Marut":
    print("correct")
    score += 1
    print("your score is",score)
else:
    print("incorrect",score)
    print("the correct answer is hal marut")
q3 =input("name the engine used in hal marut?🛩️")
print("A. Electric Motor")
print("B. Turbojet")
print("C. Piston Engine")
print("D. Rocket Engine")

q3 = input("enter your answer: ")

if q3.lower()=="turbojet":
    print("correct")
    score += 1
    print("your score is",score)
else:
    print("incorrect", score)
    print("the correct answer is turbojet")
q4 = input("name the engine used in tejus?✈️")
print("A. GE F404")
print("B. Pratt & Whitney F100")
print("C. Rolls-Royce Engine")
print("D. Engine")

q4 = input("enter your answer: ")

if q4.lower() == "ge f404":
    print("correct")
    score += 1
    print("your score is",score)
else:
    print("incorrect", score)
    print("the correct answer is ge f404")
q5 = input("name the engine used in su-30mki?🛫")
print("A. AL-31FP")
print("B. GE F404")
print("C. Pratt & Whitney F100")
print("D. Rolls-Royce Engine")

q5 = input("enter your answer: ")

if q5.lower() == "al-31fp":
    print("correct")
    score += 1
    print("your score is",score)
else:
    print("incorrect", score)
    print("the correct answer is al-31fp")

q6 = input("name the engine used in rafale?🛫")
print("A. AL-31FP")
print("B. GE F404")
print("C. Pratt & Whitney F100")
print("D. Rolls-Royce Engine")

q6 = input("enter your answer: ")

if q6.lower() == "ge f404":
    print("correct")
    score += 1
    print("your score is",score)
else:
    print("incorrect", score)
    print("the correct answer is ge f404")

q7 = input("name the engine used in mig-29?🛫")
print("A. AL-31FP")
print("B. GE F404")
print("C. Pratt & Whitney F100")
print("D. Rolls-Royce Engine")

q7 = input("enter your answer: ")

if q7.lower() == "al-31fp":
    print("correct")
    score += 1
    print("your score is",score)
else:
    print("incorrect", score)
    print("the correct answer is al-31fp")

q8 = input("name the engine used in su-57?🛫")
print("A. AL-31FP")
print("B. GE F404")
print("C. Pratt & Whitney F100")
print("D. Rolls-Royce Engine")

q8 = input("enter your answer: ")

if q8.lower() == "al-31fp":
    print("correct")
    score += 1
    print("your score is",score)
else:
    print("incorrect", score)
    print("the correct answer is al-31fp")
q9 = input("name the engine used in tejas mk2?🛫")
print("A. AL-31FP")
print("B. GE F404") 
print("C. Pratt & Whitney F100")
print("D. Rolls-Royce Engine")

q9 = input("enter your answer: ")

if q9.lower() == "ge f404":
    print("correct")
    score += 1
    print("your score is",score)
else:
    print("incorrect", score)
    print("the correct answer is ge f404")

q10 = input("name the engine used in rafale mk2?🛫")
print("A. AL-31FP")
print("B. GE F404")
print("C. Pratt & Whitney F100")
print("D. Rolls-Royce Engine")

q10 = input("enter your answer: ")

if q10.lower() == "ge f404":
    print("correct")
    score += 1
    print("your score is",score)
else:
    print("incorrect", score)
    print("the correct answer is ge f404")

print("your final score is",score)
percentage = (score/5)*100
print("your percentage is🤧",percentage)
if score == 5:
    print("🫅excellent")
elif score == 4:
    print("👸very good")
elif score == 3:
    print("🤴good")
elif score == 2:
    print("😿average")
elif score == 1:
    print("🤡poor")
else:
    print("💀very poor")
print(name,"thanks for playing the quiz your score is ",score,"percentage is ",percentage)
if percentage >= 80:
    print("😍Aviation expert")    
elif percentage >= 60:
    print("🤩Aviation enthusiast")
else:
    print("keep learning 😁")
