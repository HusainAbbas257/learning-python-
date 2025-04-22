print("Welcome to the Indian Current Affairs Quiz!\n")
score = 0

# Q1
print("Q1: Who is the current President of India?")
print("a) Droupadi Murmu")
print("b) Ram Nath Kovind")
print("c) Narendra Modi")
ans = input("Your answer: ")
if ans == "a":
    score += 1
    print("Correct!\n")
else:
    print("Wrong! Correct answer: a) Droupadi Murmu\n")

# Q2
print("Q2: What is the capital of Ladakh?")
print("a) Srinagar")
print("b) Leh")
print("c) Kargil")
ans = input("Your answer: ")
if ans == "b":
    score += 1
    print("Correct!\n")
else:
    print("Wrong! Correct answer: b) Leh\n")

# Q3
print("Q3: Who is the current Chief Election Commissioner of India?")
print("a) Rajiv Kumar")
print("b) Sushil Chandra")
print("c) Sunil Arora")
ans = input("Your answer: ")
if ans == "a":
    score += 1
    print("Correct!\n")
else:
    print("Wrong! Correct answer: a) Rajiv Kumar\n")

# Q4
print("Q4: In which year did Chandrayaan-3 land on the Moon?")
print("a) 2022")
print("b) 2023")
print("c) 2024")
ans = input("Your answer: ")
if ans == "b":
    score += 1
    print("Correct!\n")
else:
    print("Wrong! Correct answer: b) 2023\n")

# Q5
print("Q5: Which city hosted the G20 Summit 2023?")
print("a) New Delhi")
print("b) Mumbai")
print("c) Bengaluru")
ans = input("Your answer: ")
if ans == "a":
    score += 1
    print("Correct!\n")
else:
    print("Wrong! Correct answer: a) New Delhi\n")

# Q6
print("Q6: Who is the current Chief Minister of Uttar Pradesh?")
print("a) Akhilesh Yadav")
print("b) Mayawati")
print("c) Yogi Adityanath")
ans = input("Your answer: ")
if ans == "c":
    score += 1
    print("Correct!\n")
else:
    print("Wrong! Correct answer: c) Yogi Adityanath\n")

# Q7
print("Q7: Which team won the IPL 2023?")
print("a) Gujarat Titans")
print("b) Chennai Super Kings")
print("c) Mumbai Indians")
ans = input("Your answer: ")
if ans == "b":
    score += 1
    print("Correct!\n")
else:
    print("Wrong! Correct answer: b) Chennai Super Kings\n")

# Q8
print("Q8: Which river is being cleaned under the 'Namami Gange' project?")
print("a) Yamuna")
print("b) Narmada")
print("c) Ganga")
ans = input("Your answer: ")
if ans == "c":
    score += 1
    print("Correct!\n")
else:
    print("Wrong! Correct answer: c) Ganga\n")

# Q9
print("Q9: Who is the current RBI Governor?")
print("a) Urjit Patel")
print("b) Shaktikanta Das")
print("c) Raghuram Rajan")
ans = input("Your answer: ")
if ans == "b":
    score += 1
    print("Correct!\n")
else:
    print("Wrong! Correct answer: b) Shaktikanta Das\n")

# Q10
print("Q10: Which city recently got India’s first underwater metro?")
print("a) Mumbai")
print("b) Kolkata")
print("c) Chennai")
ans = input("Your answer: ")
if ans == "b":
    score += 1
    print("Correct!\n")
else:
    print("Wrong! Correct answer: b) Kolkata\n")

# Final Score
print("Your final score is:", score, "/ 10")
if score >= 8:
    print("Excellent! You're well informed.")
elif score >= 5:
    print("Good job! Keep reading the news.")
else:
    print("You need to stay more updated!")
