#quiz program

questions = (("What is my name?"),
             ("How old am I?"),
             ("What is my favourite food?"),
             ("What colour do i like?"),
             ("What is my favourite animal? "))

options = (("A. Duc Anh", "B. Anh Duc", "C. Anh Anh", "D. Duc Duc"),
           ("A. 25", "B. 26", "C. 27", "D. 28"),
           ("A. dog", "B. cat", "C. pizza", "D. hot dog"),
           ("A. orange", "B. yellow", "C. blue", "D. green"),
           ("A. tiger", "B. lion", "C. elephant", "D. dog"))

answers = ("A", "B", "C", "C", "D")
guesses = []

score = 0
question_num = 0

for question in questions:
    print("------------------------------")
    print(question)
    for option in options:
        print(option)
    
    guess = input("Enter your guess (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers:
        score += 1
        print("Correct!")
    else:
        print("Incorrect!")
        print(f"The correct answer is {answers[question_num]}")
    question_num += 1

print("------------------------------")
print("          RESULTS             ")
print("------------------------------")
print("Answer:  ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("Guesses: ", end="")
for guess in guesses:
    print(guess, end= " ")
print()

score = int(score/ len(questions) * 100)
print(f"Your score is: {score}%")