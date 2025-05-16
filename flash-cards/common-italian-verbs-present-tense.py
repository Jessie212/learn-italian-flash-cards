from tkinter import *
from random import randint

root = Tk()
root.title("Italian language flashcards for common verbs in the present tense")
root.iconbitmap()
root.geometry("550x410")

verbs = [
    (("To be"), ("Essere")),
    (("I am"), ("Sono")),
    (("You are"), ("Sei")),
    (("He/she/it is"), ("E")),
    (("We are"), ("Siamo")),
    (("You all are"), ("Siete")),
    (("They are"), ("Sono")),

    (("To be (physically)"), ("Stare")),
    (("I am (physically)"), ("Sto")),
    (("You are (physically)"), ("Stai")),
    (("He/she/it is (physically)"), ("Sta")),
    (("We are (physically)"), ("Stiamo")),
    (("You all are (physically)"), ("State")),
    (("They are (physically)"), ("Stanno")),

    (("To have"), ("Avere")),
    (("I have"), ("Ho")),
    (("You have"), ("Hai")),
    (("He/she/it has"), ("Ha")),
    (("We have"), ("Abbiamo")),
    (("You all have"), ("Avete")),
    (("They have"), ("Hanno")),

    (("To have to"), ("Dovere")),
    (("I must"), ("Devo")),
    (("You must"), ("Devi")),
    (("He/she/it must"), ("Deve")),
    (("We must"), ("Dobbiamo")),
    (("You all must"), ("Dovete")),
    (("They must"), ("Devono")),

    (("To do/To make"), ("Fare")),
    (("I do/make"), ("Faccio")),
    (("You do/make"), ("Fai")),
    (("He/she/it does/makes"), ("Fa")),
    (("We do/make"), ("Facciamo")),
    (("You all do/make"), ("Fate")),
    (("They do/make"), ("Fanno")),

    (("To go"), ("Andare")),
    (("I go"), ("Vado")),
    (("You go"), ("Vai")),
    (("He/she/it goes"), ("Va")),
    (("We go"), ("Andiamo")),
    (("You all go"), ("Andate")),
    (("They go"), ("Vanno")),

    (("To be able"), ("Potere")),
    (("I can"), ("Posso")),
    (("You can"), ("Puoi")),
    (("He/she/it can"), ("Puo")),
    (("We can"), ("Possiamo")),
    (("You all can"), ("Potete")),
    (("They can"), ("Possono")),

    (("To want"), ("Volere")),
    (("I want"), ("Voglio")),
    (("You want"), ("Voui")),
    (("He/she/it wants"), ("Vuole")),
    (("We want"), ("Vogliamo")),
    (("You all want"), ("Volete")),
    (("They want"), ("Vogliono")),

    (("To see"), ("Vedere")),
    (("I see"), ("Vedo")),
    (("You see"), ("Vedi")),
    (("He/she/it sees"), ("Vede")),
    (("We see"), ("Vediamo")),
    (("You all see"), ("Vedete")),
    (("They see"), ("Vedono")),

    (("To say"), ("Dire")),
    (("I say"), ("Dico")),
    (("You say"), ("Dici")),
    (("He/she/it says"), ("Dice")),
    (("We say"), ("Diciamo")),
    (("You all say"), ("Dite")),
    (("They say"), ("Dicono")),
]

# Get a count of verb list
count = len(verbs)

def action(event):
    print("Enter pressed")
    root.bind("<Enter>", action())

def next():

# Reset hinter
    hinter = ""
    hint_count = 0

# Create random selection
    global random_verb
    random_verb = randint(0, count-1)

# Update label with a new Italian verb
    italian_verb.config(text=verbs[random_verb][0])

# Clear the screen
    answer_label.config(text="")
    my_entry.delete(0, END)
    hint_label.config(text="")

def answer():
    if my_entry.get().capitalize() == verbs[random_verb][1]:
        answer_label.config(text=f"Correct! {verbs[random_verb][0]} is {verbs[random_verb][1]}")
    else:
        answer_label.config(text=f"Incorrect {verbs[random_verb][0]} is not {my_entry.get().capitalize()}")

# Keep track of the hints
hinter = ""
hint_count = 0
def hint():
    global hint_count
    global hinter

    if hint_count < len(verbs[random_verb][1]):
        hinter = hinter + (verbs[random_verb][1][hint_count])
        hint_label.config(text=hinter)
        hint_count +=1

# Bind the Enter key tot the window
def clicker(event):
    my_label =Label(root, text="")
    my_label.pack()

# Create labels
italian_verb = Label(root, text="", font=("Helvetica", 36))
italian_verb.pack(pady=50)

answer_label = Label(root, text="")
answer_label.pack(pady=20)

my_entry = Entry(root, font=("Helvetica", 18))
my_entry.pack(pady=20)

# Create buttons
button_frame = Frame(root)
button_frame.pack(pady=20)

answer_button = Button(button_frame, text="Answer", command=answer)
answer_button.grid(row=0, column=0, padx=20)

next_button = Button(button_frame, text="Next", command=next)
next_button.grid(row=0, column=1)

hint_button = Button(button_frame, text="Hint", command = hint)
hint_button.grid(row=0, column=2, padx=20)

# Create Hint Label
hint_label = Label(root, text="")
hint_label.pack(pady=20)

# Run conjugations function when program starts
next()


root.mainloop()