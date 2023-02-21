from tkinter import *
import random

#changes the turn
def next_turn(row, column):

    #want to use the same player list
    global player

    #checks to see if button is empty by using its text
    if buttons[row][column]['text'] == "" and check_winner() is False:

        #checks to make sure it is the first player
        if player == players[0]:


            buttons[row][column]['text'] = player

            #if no winner then switches players turn and changes text
            if check_winner() is False:

                player = players[1]

                label.config(text=(players[1] + " turn"))

            elif check_winner() is True:
                label.config(text=(players[0] + " wins"))

            elif check_winner() == "Tie":
                label.config(text=("Tie"))

        else:

            buttons[row][column]['text'] = player

            #if no winner then switches players turn and changes text
            if check_winner() is False:

                player = players[0]

                label.config(text=(players[0] + " turn"))

            elif check_winner() is True:
                label.config(text=(players[1] + " wins"))

            elif check_winner() == "Tie":
                label.config(text=(" Tie"))



#checks for win condition
def check_winner():
    #checks for all horizontal win conditions 
    for row in range (3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
            #sets winning buttons to green
            buttons[row][0].config(bg="green")
            buttons[row][1].config(bg="green")
            buttons[row][2].config(bg="green")
            return True
    
    #checks for all vertical win conditions
    for column in range (3):
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":
            #sets winning buttons to green
            buttons[0][column].config(bg="green")
            buttons[1][column].config(bg="green")
            buttons[2][column].config(bg="green")
            return True
 
    #checks for both diagonal win conditions
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        #sets winning buttons to green
        buttons[0][0].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][2].config(bg="green")
        return True
    
    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        #sets winning buttons to green
        buttons[0][2].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][0].config(bg="green")
        return True
    
    #calls to see if anymore empty spaces left
    elif empty_spaces() is False:

        #if tie everything yellow
        for row in range (3):
            for column in range (3):
                buttons[row][column].config(bg="yellow")
        return "Tie"
    
    else: 
        return False



#determines where a player can play
def empty_spaces():

    spaces = 9

    for row in range (3):
        for column in range (3):
            if buttons[row][column]['text'] != "":
                spaces -=1
    
    if spaces == 0:
        return False
    else: 
        return True

#makes the new game
def new_game():
 

    global player

    #changes new player
    player = random.choice(players)
    label.config(text=player + "turn")
    
    #changes color back to default and tect back to empty
    for row in range (3):
        for column in range (3):
            buttons[row][column].config(text="",bg="#F0F0F0")
    

#makes the window
window = Tk()
#Titles the window
window.title("Tic-Tac-Toe")

#makes player list
players = ["x","o"]
#picks a random player to go
player = random.choice(players)

#makes the 2d array board
buttons = [[0,0,0] , 
           [0,0,0] , 
           [0,0,0]]

#shows user who goes first
label = Label(text = player + " turn", font = ('Times New Roman', 40))
label.pack(side="top")

#Makes a restart button that calls to the new_game function
reset_button = Button(text="restart", font=('time new roman', 20), command=new_game)
reset_button.pack(side="top")


frame = Frame(window)
frame.pack()

#makes a button inside each frame 
#uses grid for looks
for row in range (3):
    for column in range(3):
        buttons[row][column] = Button(frame, text= "", font=('times new roman', 40), width=5, height=2,
                                      command = lambda row=row, column=column:next_turn(row,column))
        buttons[row][column].grid(row=row,column=column)




window.mainloop()
