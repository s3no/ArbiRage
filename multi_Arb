print("------------ARBIRAGE------------")

def twoWayArb():
    #Gets the total Wager and Odds from user entrys
    wageTotal = float(input("What Is Your Total Wager Amount?"))
    teamOne = float(input("Enter First Teams Odds: "))
    teamTwo = float(input("Enter Second Teams Odds: "))

    #Calculations for arbitrage percentage value
    OddsOneValue = 1 / float(teamOne)                       
    OddsTwoValue = 1 / float(teamTwo)                                     
    oddsValue = OddsOneValue + OddsTwoValue                                 
    oddsPercent = oddsValue * 100                                           
    
    #Calculation For How Much To Wage On Each Team Rounded to 2 Decimal Places
    wageOne = round(float(wageTotal) / (OddsOneValue / OddsTwoValue + 1), 2) 
    wageTwo = round(float(wageTotal) / (OddsTwoValue / OddsOneValue + 1), 2)
    print(wageTwo)
    print(wageOne)

    #Calculates Your Profit For Both Results
    profitOne = round(float(wageTwo) * float(teamOne) - float(wageTotal),2) 
    profitTwo = round(float(wageOne) * float(teamTwo) - float(wageTotal),2)
    print(profitTwo)
    print(profitOne)
  

def threeWayArb():
    #Gets the total Wager and Odds from user entrys
    wageTotal = float(input("What Is Your Total Wager Amount?"))
    teamOne = float(input("Enter First Teams Odds: "))
    teamTwo = float(input("Enter Second Teams Odds: "))
    teamThree = float(input("Enter Third Teams Odds: "))

    #Calculation for betting Odds
    teamOneProb = round(1 / float(teamOne) * int(100),2)
    teamTwoProb = round(1 / float(teamTwo) * int(100),2)
    teamThreeProb = round(1 / float(teamThree) * int(100),2)
    tempThree = teamOneProb + teamTwoProb + teamThreeProb   
    probability = tempThree #(Win < 100% > Loss)
    #Prints Probability Percentage
    print(str(round(probability,2)) + "%")

    #Calculation For How Much To Wage On Each Team Rounded to 2 Decimal Places
    wageOne = round(float(wageTotal) * teamOneProb / probability,2)
    wageTwo = round(float(wageTotal) * teamTwoProb / probability,2)
    wageThree = round(float(wageTotal) * teamThreeProb / probability,2)

    #Calculation for Profits If Game Results In A Win
    TeamOnePayout = round(float(wageOne * teamOne - wageTotal),2)
    TeamTwoPayout = round(float(wageTwo * teamTwo - wageTotal),2)
    TeamThreePayout = round(float(wageThree * teamThree - wageTotal),2)



#Runs The Program
userPick = input("1 = Two Way Arbitrage\n2 = Three Way Arbitrage\n")
while True:
    if userPick == "1":
        twoWayArb()
    elif userPick == "2":
        threeWayHouseOdds()
    else:
        userPick = input("1 = Two Way Arbitrage\n2 = Three Way Arbitrage")

