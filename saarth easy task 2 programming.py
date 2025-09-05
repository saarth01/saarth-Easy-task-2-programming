score = 0

print("=== Welcome to the Quiz ===\n")

# Question 1
print("1. What is the capital of France?")
print("a) Berlin\nb) Madrid\nc) Paris\nd) Rome")
ans = input("Enter your answer: ")
if ans.lower() == "c":
    score += 1

# Question 2
print("\n2. Which language is known as the language of the web?")
print("a) C++\nb) Python\nc) JavaScript\nd) Java")
ans = input("Enter your answer: ")
if ans.lower() == "c":
    score += 1

# Question 3
print("\n3. What is 5 + 7?")
print("a) 10\nb) 12\nc) 14\nd) 15")
ans = input("Enter your answer: ")
if ans.lower() == "b":
    score += 1

# Question 4
print("\n4. Who developed Python?")
print("a) James Gosling\nb) Guido van Rossum\nc) Dennis Ritchie\nd) Elon Musk")
ans = input("Enter your answer: ")
if ans.lower() == "b":
    score += 1

# Question 5
print("\n5. Which planet is known as the Red Planet?")
print("a) Earth\nb) Mars\nc) Jupiter\nd) Venus")
ans = input("Enter your answer: ")
if ans.lower() == "b":
    score += 1

print("\n=== Quiz Finished ===")
print("Your Final Score:", score, "/ 5")
