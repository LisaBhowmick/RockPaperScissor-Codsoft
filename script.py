from tkinter import *
from PIL import Image, ImageTk
from random import randint
import os

root = Tk()
root.title("Rock Paper Scissors")
root.geometry("800x500")
root.configure(bg="#1e1e1e")
root.resizable(False, False)

# Load images
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
def load_img(name, size=(130, 130)):
    path = os.path.join(BASE_DIR, "public", name)
    return ImageTk.PhotoImage(Image.open(path).resize(size))

rock_img = load_img("rock.png")
paper_img = load_img("paper.png")
scissor_img = load_img("scissor.png")

rock_img_comp = rock_img
paper_img_comp = paper_img
scissor_img_comp = scissor_img

choices = ["rock", "paper", "scissor"]

# Title
title_label = Label(root, text="ROCK  •  PAPER  •  SCISSORS", font=("Segoe UI", 22, "bold"), fg="#00CED1", bg="#1e1e1e")
title_label.pack(pady=15)

# Frame for player & computer
frame = Frame(root, bg="#1e1e1e")
frame.pack(pady=10)

# Player Section
player_frame = Frame(frame, bg="#1e1e1e")
player_frame.grid(row=0, column=1, padx=50)

Label(player_frame, text="PLAYER", font=("Segoe UI", 14, "bold"), fg="white", bg="#1e1e1e").pack()
user_label = Label(player_frame, image=rock_img, bg="#2e2e2e", bd=2, relief="flat")
user_label.pack(pady=5)
playerScore = Label(player_frame, text="0", font=("Segoe UI", 18, "bold"), fg="#00FA9A", bg="#1e1e1e")
playerScore.pack()

# Computer Section
comp_frame = Frame(frame, bg="#1e1e1e")
comp_frame.grid(row=0, column=0, padx=50)

Label(comp_frame, text="COMPUTER", font=("Segoe UI", 14, "bold"), fg="white", bg="#1e1e1e").pack()
comp_label = Label(comp_frame, image=rock_img_comp, bg="#2e2e2e", bd=2, relief="flat")
comp_label.pack(pady=5)
computerScore = Label(comp_frame, text="0", font=("Segoe UI", 18, "bold"), fg="#FF6347", bg="#1e1e1e")
computerScore.pack()

# Message
msg = Label(root, text="", font=("Segoe UI", 16, "bold"), bg="#1e1e1e", fg="white")
msg.pack(pady=15)

# Update functions
def updateMessage(text, color="white"):
    msg.config(text=text, fg=color)

def updateUserScore():
    score = int(playerScore["text"])
    playerScore["text"] = str(score + 1)

def updateCompScore():
    score = int(computerScore["text"])
    computerScore["text"] = str(score + 1)

def checkWin(player, computer):
    if player == computer:
        updateMessage("It's a tie!", "#FFD700")
    elif (player == "rock" and computer == "scissor") or \
         (player == "scissor" and computer == "paper") or \
         (player == "paper" and computer == "rock"):
        updateMessage("You win!", "#00FA9A")
        updateUserScore()
    else:
        updateMessage("You lose!", "#FF6347")
        updateCompScore()  # ✅ FIX: increase computer's score when it wins


def animate_transition(label, img):
    label.config(image=img)
    label.image = img

# Game logic
def updateChoice(userChoice):
    compChoice = choices[randint(0, 2)]
    comp_img = rock_img_comp if compChoice == "rock" else paper_img_comp if compChoice == "paper" else scissor_img_comp
    user_img = rock_img if userChoice == "rock" else paper_img if userChoice == "paper" else scissor_img
    animate_transition(comp_label, comp_img)
    animate_transition(user_label, user_img)
    checkWin(userChoice, compChoice)

# Modern button style
btn_style = {
    "width": 10,
    "height": 2,
    "font": ("Segoe UI", 13, "bold"),
    "bg": "#333",
    "fg": "white",
    "activebackground": "#00CED1",
    "activeforeground": "black",
    "relief": "flat",
    "bd": 0
}

# Buttons frame
btn_frame = Frame(root, bg="#1e1e1e")
btn_frame.pack(pady=10)

rock_btn = Button(btn_frame, text="ROCK", command=lambda: updateChoice("rock"), **btn_style)
paper_btn = Button(btn_frame, text="PAPER", command=lambda: updateChoice("paper"), **btn_style)
scissor_btn = Button(btn_frame, text="SCISSOR", command=lambda: updateChoice("scissor"), **btn_style)

rock_btn.grid(row=0, column=0, padx=15)
paper_btn.grid(row=0, column=1, padx=15)
scissor_btn.grid(row=0, column=2, padx=15)

root.mainloop()
