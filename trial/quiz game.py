#python quiz game
questions = ("How many elements are there in the peridoic table?","which animal lays the biggest egg?",
             "Which is the most abundant gas in Earths atmosphere?", "How many bones are there in the human body?")
options = (("A.117", "B.116", "C.118", "D.119"),
            ("A.Whale", "B.crocodile", "C.ostrich", "D.shark"),
            ("A.oxygen", "B.Nitrogen", "C.Chlorine","D.carbon dioxide"),
            ("A.205", "B.206", "C.207", "D.208"))
Answers = ["C", "C", "B", "B"]
questionnum = 0
score = 0
for question in questions:
    print("------------------------------------")
    print(question)
    for option in options[questionnum]:
        print(option)
    guess = input("enter ur ans (A,B,C,D): ").upper()
    if guess == Answers[questionnum]:
        print("CORRECT")
        score += 1
    else:
        print("INCORRECT")
        print(f"{Answers[questionnum]} is the correct answer")
    questionnum += 1
print("----------------------------")
print(f"Your total score is {score}")
print("----------------------------")
print("Thank you for playing!")
   

   