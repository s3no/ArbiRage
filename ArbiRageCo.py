print("------------ARBIRAGE------------")

def twoWayHouseOdds():
    #Get Total Bet And Wage
    wageTotal = input("What Is Your Total Wager Amount?") #eg: 100
    oddsOne = input("Enter First Teams Odds: ") #eg: 1.3    
    oddsTwo = input("Enter Second Teams Odds: ") #eg: 10
    #Storing Total Bet And Wage Complete

     
    #Calculations for arbitrage percentage value
    OddsOneValue = 1 / float(oddsOne)                                        #eg 1 / 1.3 Output: 0.7692307692307692
    OddsTwoValue = 1 / float(oddsTwo)                                        #eg 1 / 10 Output: 0.1
    oddsValue = OddsOneValue + OddsTwoValue                                  #eg output: 0.8692307692307692
    oddsPercent = oddsValue * 100                                            #eg Output:  86.92307692307692
    
    #Calculation For How Much To Wage On Each Team Rounded to 2 Decimal Places
    wageOne = round(float(wageTotal) / (OddsOneValue / OddsTwoValue + 1), 2) #eg: $11.50
    wageTwo = round(float(wageTotal) / (OddsTwoValue / OddsOneValue + 1), 2) #eg: $88.49
    #Calculations Compleate				
	

    #Outputs if the House Wins OR, If you win displays how much to place on each team. 
    if float(oddsPercent) < 100:
       #Calculates Your Profit For Both Results
       profitOne = round(float(wageTwo) * float(oddsOne) - float(wageTotal),2) #eg: Profit: $15.037
       profitTwo = round(float(wageOne) * float(oddsTwo) - float(wageTotal),2) #eg: Profit: $15.00
       #Calculation Finished  
       print("\n!!!PLACE BET!!!\n")
       print("Team One Bet: $" + str(wageTwo) + "       --Profit: $" + str(profitOne))
       print("Team Two Bet: $" + str(wageOne) + "       --Profit: $" + str(profitTwo) + "\n")
    elif casTake > 100:
       print("BAIL---House Wins\n")
       print("BAIL: House Wins - " + str(oddsPercent) + "\n")
       print("BAIL: House Wins - " + str(oddsPercent) + "\n")
    elif casTake == 100:       
       print("EVEN SPREAD----100%----BREAK EVEN")
    else:
       print("ERROR")

    print("-------NEW-GAME-----------------")

while True:
    twoWayHouseOdds()
