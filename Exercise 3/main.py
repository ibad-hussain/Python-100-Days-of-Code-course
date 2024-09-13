# EXERCISE 3 - KAUN BANEGA CROREPATI (KBC)
# Problem Statement: Create a program capable of displaying questions to the user like KBC. Use List data type to store the questions and their correct answers. Display the final amount the person is taking home after playing the game.



from time import sleep

questions = [
    [
        "Q.1) What is the capital of Pakistan ?", "islamabad", "karachi",
        "lahore", "peshawar"
    ],
    [
        "Q.2) Which company owns Facebook ?", "google", "meta", "microsoft",
        "apple"
    ],
    [
        "Q.3) Which company owns Windows ?", "facebook", "google", "microsoft",
        "amazon"
    ],
    [
        "Q.4) Who won Cricket World Cup 2023 ?", "england", "india",
        "pakistan", "australia"
    ],
    [
        "Q.5 Name Pakistan's first winning Cricket World Cup captain ?",
        "imran khan", "younis khan", "sarfaraz ahmed", "babar azam"
    ],
    [
        "Q.6) What is Pakistan's official language ?", "punjabi", "urdu",
        "hindi", "pushto"
    ],
    [
        "Q.7) What is the biggest religion in Pakistan ?", "hinduism",
        "buddhism", "islam", "christanity"
    ],
    [
        "Q.8) Which is Pakistan's most populous city ?", "multan",
        "rawalpindi", "lahore", "karachi"
    ],
    [
        "Q.9) Which drink is most popular in Pakistan ?", "tea", "tang",
        "apple juice", "coffee"
    ],
    [
        "Q.10) Which dish is not a typical Pakistan dish ?", "biryani", "dosa",
        "halwa poori", "nihari"
    ]
]

answers = [
    "islamabad", "meta", "microsoft", "australia", "imran khan", "urdu",
    "islam", "karachi", "tea", "dosa"
]

prizes = [
    "1 Thousand", "10 Thousand", "50 Thousand", "1 Lakh", "5 Lakh", "10 Lakh",
    "20 Lakh", "50 Lakh", "75 Lakh", "1 Crore"
]

money = ""

print("Welcome to KAUN BANEGA CROREPATI\n")
sleep(2)
print("Today we have 10 questions for you and 4 options for each question.\n")
sleep(2)
print("So lets get started !\n")
sleep(2)
print("-------------------------")
print("-------------------------")
print(" ")
sleep(1)

for i in range(0, len(questions)):

  if i == (len(questions)-1):
    print("Congrats! You are just one question away from becoming a Crorepati")
    sleep(2)
    print("Here is your Last Question\n")
    sleep(2)

  print(questions[i][0])
  print(questions[i][1])
  print(questions[i][2])
  print(questions[i][3])
  print(questions[i][4], "\n")

  reply = str(input("Enter your answer (or type 'zero' to quit): "))
  sleep(1)

  if reply == "zero":
    money = prizes[i - 1]
    if i == 0:
      money = 0
    print("You quit the game")
    break

  elif reply == answers[i]:
    if i == (len(questions) - 1):
      money = prizes[i]
      print("Correct answer ! You have won Rs.", prizes[i])
    else:
      money = prizes[i - 1]
      print("Correct answer ! You have won Rs.", prizes[i])
      sleep(1)
      print(" ")
      print("-------------------------")
      print(" ")
      sleep(1)

  else:
    money = prizes[i - 1]
    if i == 0:
      money = 0
    print("Wrong answer ! You have lost the game")
    break

print(" ")
sleep(1)
print("-------------------------")
print("-------------------------")
print(" ")
sleep(2)
print("Your total earned amount: Rs.", money)
print("Thanks for playing !!!")