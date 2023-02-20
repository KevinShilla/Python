import random


name = input("What is your name: ")
question = input("Hello " + name + " What is your question: ")

answer = ""

random_number = random.randint(1,9)
if random_number == 1:
      answer = "Yes - definitely"
elif random_number == 2:
  answer = "No"
elif random_number == 3:
  answer = "Without a doubt"
elif random_number == 4:
  answer = "I dont think so"
elif random_number == 5:
  answer = "Ask again later"
elif random_number == 6:
  answer = "I dont know how to answer that"
elif random_number == 7:
  answer = "Maybe"
elif random_number == 8:
  answer = "You should ask google"
elif random_number == 9:
  answer = "Very doubtful"
else:
  answer = "Error"

if(name == ""):
  print("Question: " + question)
  print("Magic 8-Ball's answer: " + answer)
else:
  print(name + " asks: " + question)
  print("Magic 8-Ball's answer: " + answer)
