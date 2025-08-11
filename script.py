from tkinter import *
from PIL import Image, ImageTk
from random import randint
import os


root = Tk()
root.title("Rock Paper Scissors")
root.geometry("700x500")
root.configure(bg="#f5f5dc")
root.resizable(False, False)

# Load images
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
def load_img(name, size=(150, 150)):
    path = os.path.join(BASE_DIR, "public", name)
    return ImageTk.PhotoImage(Image.open(path).resize(size))


rock_img = load_img("rock.png")
paper_img = load_img("paper.png")
scissor_img = load_img("scissor.png")


rock_img_comp = rock_img
paper_img_comp = paper_img
scissor_img_comp = scissor_img


choices = ["rock", "paper", "scissor"]


user_label = Label(root, image=rock_img, bg="#f5f5dc", bd=5, relief="groove")
comp_label = Label(root, image=rock_img_comp, bg="#f5f5dc", bd=5, relief="groove")
user_label.place(x=450, y=100)
comp_label.place(x=100, y=100)


playerScore = Label(root, text=0, font=("Comic Sans MS", 20, "bold"), fg="dark green", bg="#f5f5dc")
computerScore = Label(root, text=0, font=("Comic Sans MS", 20, "bold"), fg="dark red", bg="#f5f5dc")
playerScore.place(x=500, y=270)
computerScore.place(x=150, y=270)


Label(root, text="PLAYER", font=("Comic Sans MS", 15, "bold"), bg="#f5f5dc", fg="black").place(x=500, y=240)
Label(root, text="COMPUTER", font=("Comic Sans MS", 15, "bold"), bg="#f5f5dc", fg="black").place(x=135, y=240)


msg = Label(root, text="", font=("Lucida Handwriting", 16), bg="#f5f5dc", fg="black")
msg.place(x=260, y=320)


def updateMessage(text):
    msg.config(text=text)


def updateUserScore():
    score = int(playerScore["text"])
    playerScore["text"] = str(score + 1)

def updateCompScore():
    score = int(computerScore["text"])
    computerScore["text"] = str(score + 1)


def checkWin(player, computer):
    if player == computer:
        updateMessage("It's a tie!")
    elif (player == "rock" and computer == "scissor") or \
         (player == "scissor" and computer == "paper") or \
         (player == "paper" and computer == "rock"):
        updateMessage("You win!")
        updateUserScore()
    else:
        updateMessage("You lose!")
        updateCompScore()


def animate_transition(label, img):
    label.config(image=img)
    label.image = img

# Logic
def updateChoice(userChoice):
    compChoice = choices[randint(0, 2)]


    comp_img = rock_img_comp if compChoice == "rock" else paper_img_comp if compChoice == "paper" else scissor_img_comp
    user_img = rock_img if userChoice == "rock" else paper_img if userChoice == "paper" else scissor_img

    animate_transition(comp_label, comp_img)
    animate_transition(user_label, user_img)

    checkWin(userChoice, compChoice)


style = {
    "width": 12,
    "height": 2,
    "font": ("Courier New", 14, "bold"),
    "bd": 4,
    "relief": "ridge",
    "bg": "#fffaf0",
    "activebackground": "#d3d3d3"
}

rock_btn = Button(root, text="ROCK", fg="#000", command=lambda: updateChoice("rock"), **style)
paper_btn = Button(root, text="PAPER", fg="#000", command=lambda: updateChoice("paper"), **style)
scissor_btn = Button(root, text="SCISSOR", fg="#000", command=lambda: updateChoice("scissor"), **style)

rock_btn.place(x=100, y=400)
paper_btn.place(x=300, y=400)
scissor_btn.place(x=500, y=400)

Label(root, text="Rock ✊ Paper ✋ Scissors ✌", font=("Chalkduster", 22, "bold"), bg="#f5f5dc", fg="brown").pack(pady=20)

root.mainloop()
