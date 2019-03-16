from tkinter import *

def houseOdds():
    #Gets the total Wager and Odds from user entrys
    wager = entryWage.get()
    teamOne = entryOne.get()
    teamTwo = entryTwo.get()

    #Calculation for betting system
    tempOne = 1 / float(teamOne)
    tempTwo = 1 / float(teamTwo)
    tempThree = tempOne + tempTwo
    casTake = tempThree * 100
    
    w1 = round(float(wager) / (tempOne / tempTwo + 1), 2)
    w2 = round(float(wager) / (tempTwo / tempOne + 1), 2)

    profitOne = float(w2) * float(wager)
    profitTwo = float(w1) * float(wager)

    #Outputs if the House Wins OR, If you win displays how much to place on each team. 
    if float(casTake) < 100:
       outcomeLabel = Label(window, text="!!!PLACE BET!!!")
       outcomeLabel.grid(row=3, column=1)
       wageOne = Label(window, text="Team One Bet: $" + str(w2) + "       --Profit: $" + str(profitOne))
       wageOne.grid(row=4,column=0)
       wageTwo = Label(window, text="Team Two Bet: $" + str(w1) + "       --Profit: $" + str(profitTwo))
       wageTwo.grid(row=5,column=0)
    elif casTake > 100:
       outcomeLabel = Label(window, text="BAIL---House Wins")
       outcomeLabel.grid(row=3, column=1)
       wageOne = Label(window, text="Team One Bet: $0")
       wageOne.grid(row=4,column=0)
       wageTwo = Label(window, text="Team Two Bet: $0")
       wageTwo.grid(row=5,column=0)
    elif casTake == 100:       
       outcomeLabel = Label(window, text="EVEN SPREAD----100%")
       outcomeLabel.grid(row=3, column=1)
    else:
       print("ERROR") 
  
#Sets up Main Window
window = Tk()

#Setting up labels and User entrys
totalWage = Label(window, text="Enter Your Total Wage Amount: ")
entryWage = Entry(window)
oddOne = Label(window, text="Enter First Teams BestOdds: ")
entryOne = Entry(window)
oddTwo = Label(window, text="Enter Second Teams BestOdds: ")
entryTwo = Entry(window)
acceptButton = Button(window, text="Calculate", command= houseOdds)

#Places Labels and User entrys into the main window
totalWage.grid(row=0, column=0)
entryWage.grid(row=0, column=1)
oddOne.grid(row=1, column=0)
entryOne.grid(row=1, column=1)
oddTwo.grid(row=2, column=0)
entryTwo.grid(row=2, column=1)
acceptButton.grid(row=3, column=0)

#Runs the main window
window.mainloop()
