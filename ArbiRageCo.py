def houseOdds():
   wageTotal = input("What Is Your Total Wager Amount?")
   teamOne = input("Enter First Teams Odds: ")
   teamTwo = input("Enter Second Teams Odds: ")

   tempOne = 1 / float(teamOne)
   tempTwo = 1 / float(teamTwo)
   tempThree = tempOne + tempTwo

   casTake = tempThree * 100
   print("\n")

   if casTake > 100:
      print("Percentage(above 100% YOU LOOSE!)" + str(casTake) + "%" + "\n")
   elif casTake < 100:
      print("Percentage(below 100% YOU WIN!!!!!!):" + str(casTake) + "%" + "\n")

   w1 = round(float(wageTotal) / (tempOne / tempTwo + 1))
   w2 = round(float(wageTotal) / (tempTwo / tempOne + 1))

   profitOne = float(w2) * float(teamOne)
   profitTwo = float(w1) * float(teamTwo)
                        
   if float(casTake) < 100:
      print("!!!!!PLACE BET!!!!!" + "\n")
      print("Your Total Wager: $" + wageTotal)
      print("Team One Bet " + str(w2) + "       --Profit: $" + str(profitOne))
      print("Team Two Bet " + str(w1) + "       --Profit: $" + str(profitTwo) + "\n")
   elif casTake > 100:
      print("BAIL---House Wins" + "\n")
   elif casTake == 100:
      print("EVEN SPREAD----100%" + "\n")
   else:
      print("ERROR")

   print("\n" + "\n")
   print("-----NEW GAME-----" + "\n")

      

while True:
   houseOdds()


                           
         
