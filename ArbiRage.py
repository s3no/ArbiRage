from tkinter import *

def houseOdds():
    wager = entryWage.get()
    teamOne = entryOne.get()
    teamTwo = entryTwo.get()

    tempOne = 1 / float(teamOne)
    tempTwo = 1 / float(teamTwo)
    tempThree = tempOne + tempTwo

    casTake = tempThree * 100

    if casTake > 100:
        temp = casTake - 100
        print("House Cut:" + str(temp) + "%" + "\n")
    elif casTake < 100:
        temp = 100 - casTake
        print("Your Cut:" + str(temp) + "%" + "\n")

    w1 = float(wager) / (tempOne / tempTwo + 1)
    w2 = float(wager) / (tempTwo / tempOne + 1)

    if float(casTake) < 100:
       print("!!!!!PLACE BET!!!!!" + "\n")
       print("Your Total Wager: $" + wager)
       print("Team One Bet " + str(w1))
       print("Team Two Bet " + str(w2) + "\n")

       outcomeLabel = Label(window, text="!!!PLACE BET!!!")
       outcomeLabel.grid(row=3, column=1)
       wageOne = Label(window, text="Team One Bet " + str(w1))
       wageOne.grid(row=4,column=0)
       wageTwo = Label(window, text="Team Two Bet " + str(w2))
       wageTwo.grid(row=5,column=0)
    elif casTake > 100:
       print("BAIL---House Wins" + "\n")

       outcomeLabel = Label(window, text="BAIL---House Wins")
       outcomeLabel.grid(row=3, column=1)
    elif casTake == 100:
       print("EVEN SPREAD----100%" + "\n")
       
       outcomeLabel = Label(window, text="EVEN SPREAD----100%")
       outcomeLabel.grid(row=3, column=1)
    else:
       print("ERROR")

   

window = Tk()

totalWage = Label(window, text="Enter First Teams Odds: ")
entryWage = Entry(window)
oddOne = Label(window, text="Enter First Teams Odds: ")
entryOne = Entry(window)
oddTwo = Label(window, text="Enter Second Teams Odds: ")
entryTwo = Entry(window)
acceptButton = Button(window, text="Calculate", command= houseOdds)

totalWage.grid(row=0, column=0)
entryWage.grid(row=0, column=1)
oddOne.grid(row=1, column=0)
entryOne.grid(row=1, column=1)
oddTwo.grid(row=2, column=0)
entryTwo.grid(row=2, column=1)
acceptButton.grid(row=3, column=0)

window.mainloop()
