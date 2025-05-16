

print("Welcome to Learn Italian Fast!")

playing=input("Are you ready to test your knowledge of Italian vocabulary for THE KITCHEN? ")

if playing.lower() != "yes":
    quit()

print ("Okay! Let's begin!")
score = 0

answer = input("1) What is the correct translation for Kitchen? ")
if answer.lower() == "la cucina":
    print("Correct!")
    score += 1
else:
    print("Incorrect")

answer = input("2) What is the correct translation for Cabinets? ")
if answer.lower() == "i pensili":
    print("Correct!")
    score += 1
else:
    print("Incorrect")

answer = input("3) What is the correct translation for Counter? ")
if answer.lower() == "il piano di lavoro":
    print("Correct!")
    score += 1
else:
    print("Incorrect")

answer = input("4) What is the correct translation for Pantry? ")
if answer.lower() == "la dispensa":
    print("Correct!")
    score += 1
else:
    print("Incorrect")

answer = input("What is the correct translation for Sink? ")
if answer.lower() == "il lavandino":
    print("Correct!")
    score += 1
else:
    print("Incorrect")

answer = input("What is the correct translation for Faucet? ")
if answer.lower() == "il rubinetto":
    print("Correct!")
    score += 1
else:
    print("Incorrect")

answer = input("2) What is the correct translation for Stove? ")
if answer == "la stufa":
    print("Correct!")
    score += 1
else:
    print("Incorrect")

answer = input("What is the correct translation for Oven? ")
if answer.lower() == "il forno":
    print("Correct!")
    score += 1
else:
    print("Incorrect")

answer = input("What is the correct translation for Refrigerator? ")
if answer.lower() == "il frigorifero":
    print("Correct!")
    score += 1
else:
    print("Incorrect")

answer = input("What is the correct translation for Freezer? ")
if answer.lower() == "il congelatore":
    print("Correct!")
    score += 1
else:
    print("Incorrect")

answer = input("What is the correct translation for Microwave? ")
if answer.lower() == "il forno a microonde":
    print("Correct!")
    score += 1
else:
    print("Incorrect")

answer = input("What is the correct translation for Dishwasher? ")
if answer.lower() == "la lavastoviglie":
    print("Correct!")
    score += 1
else:
    print("Incorrect")

answer = input("What is the correct translation for Blender? ")
if answer.lower() == "il flullatore":
    print("Correct!")
    score += 1
else:
    print("Incorrect")

answer = input("What is the correct translation for Coffee maker? ")
if answer.lower() == "la caffettiera":
    print("Correct!")
    score += 1
else:
    print("Incorrect")

answer = input("What is the correct translation for Dish drainer? ")
if answer.lower() == "il scolapiatti":
    print("Correct!")
    score += 1
else:
    print("Incorrect")

answer = input("What is the correct translation for Table? ")
if answer.lower() == "il tavolo":
    print("Correct!")
    score += 1
else:
    print("Incorrect")

answer = input("What is the correct translation for Chairs? ")
if answer.lower() == "le sedie":
    print("Correct!")
    score += 1
else:
    print("Incorrect")

answer = input("What is the correct translation for Garbage can? ")
if answer.lower() == "il secchio della spazzatura":
    print("Correct!")
    score += 1
else:
    print("Incorrect")

answer = input("What is the correct translation for Knife? ")
if answer.lower() == "il coltello":
    print("Correct!")
    score += 1
else:
    print("Incorrect")

answer = input("What is the correct translation for Fork? ")
if answer.lower() == "La forchetta":
    print("Correct!")
    score += 1
else:
    print("Incorrect")

answer = input("What is the correct translation for Spoon? ")
if answer.lower() == "il cucchiaio":
    print("Correct!")
    score += 1
else:
    print("Incorrect")

answer = input("What is the correct translation for Plate? ")
if answer.lower() == "il piatto":
    print("Correct!")
    score += 1
else:
    print("Incorrect")

answer = input("What is the correct translation for Glass? ")
if answer.lower() == "il bicchiere":
    print("Correct!")
    score += 1
else:
    print("Incorrect")

answer = input("What is the correct translation for Pot? ")
if answer.lower() == "il tegame":
    print("Correct!")
    score += 1
else:
    print("Incorrect")

answer = input("What is the correct translation for Pan? ")
if answer.lower() == "la padella":
    print("Correct!")
    score += 1
else:
    print("Incorrect")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 4) * 100) + "%.")