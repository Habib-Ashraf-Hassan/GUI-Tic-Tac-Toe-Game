from tkinter import *
import random


def next_turn(row, column):
    global player
    if buttons[row][column]['text'] == "" and check_winner() is False:
        # after placing the text on the button we check if there was a winner / tie
        if player == players[0]:
            buttons[row][column]['text'] = player
            if check_winner() is False:
                player = players[1]
                label.config(text=(players[1] + " turn"))
            elif check_winner() is True:
                label.config(text=(players[0] + " wins!"))
            elif check_winner() == "Tie":
                label.config(text=("It's a Tie!"))

        else:
            buttons[row][column]['text'] = player
            if check_winner() is False:
                player = players[0]
                label.config(text=(players[0] + " turn"))
            elif check_winner() is True:
                label.config(text=(players[1] + " wins!"))
            elif check_winner() == "Tie":
                label.config(text=("It's a Tie!"))


def check_winner():
    # Checking if there is a match horizontally
    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
            buttons[row][0].config(bg="#00FF00")
            buttons[row][1].config(bg="#00FF00")
            buttons[row][2].config(bg="#00FF00")
            return True
    # Checking if there is a match vertically
    for column in range(3):
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":
            buttons[0][column].config(bg="#00FF00")
            buttons[1][column].config(bg="#00FF00")
            buttons[2][column].config(bg="#00FF00")
            return True
    # Checking if there is a match in left diagonal
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        buttons[0][0].config(bg="#00FF00")
        buttons[1][1].config(bg="#00FF00")
        buttons[2][2].config(bg="#00FF00")
        return True

    # Checking if there is a match in right diagonal
    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        buttons[0][2].config(bg="#00FF00")
        buttons[1][1].config(bg="#00FF00")
        buttons[2][0].config(bg="#00FF00")
        return True

    elif empty_spaces() is False:
        for row in range(3):
            for column in range(3):
                buttons[row][column].config(bg="yellow")
        return "Tie"

    else:
        return False


def empty_spaces():
    emptyspaces = 9
    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text'] != "":
                emptyspaces -= 1

    if emptyspaces == 0:
        return False  # No empty space available
    else:
        return True


def new_game():
    global player
    player = random.choice(players)
    label.config(text=player + " turn")
    # Return all spaces back to default(empty)
    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="", bg="#F0F0F0")  # #F0F0F0 is default color white of the buttons


window = Tk()
window.title("My Tic-Tac-Toe Game")
icon = PhotoImage(file='game.png')
window.iconphoto(True, icon)
players = ["x", "o"]  # One player is 'x' the other is 'o'
player = random.choice(players)
buttons = [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]]
label = Label(text=player + " turn", font=('Arial', 40))
label.pack(side="top")

reset_button = Button(text="Restart", font=('Arial', 20), command=new_game)
reset_button.pack(side="top")
frame = Frame(window)
frame.pack()
for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame, text="",
                                      font=('Arial', 40), width=5, height=2,
                                      command=lambda row=row, column=column: next_turn(row, column))
        buttons[row][column].grid(row=row, column=column)
window.mainloop()
