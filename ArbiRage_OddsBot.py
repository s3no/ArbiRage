import json
import requests

# An api key is emailed to you when you sign up to a plan at (https://the-odds-api.com)
api_key = ''

# Use 'upcoming' for upcoming and live game odds
sport_key = ['aussierules_afl', 'americanfootball_nfl', 'mma_mixed_martial_arts', 'soccer_fifa_world_cup', 'baseball_nba', 'cricket_test_match', 'basketball_euroleague', 'basketball_ncaab', 'rugbyunion_premiership_rugby', 'cricket_odi', 'basketball_mlb']

def houseOdds():
    #Gets the total Wager and Odds from user entrys
    wager = 20
    teamOne = teamOneHigh
    teamTwo = teamTwoHigh
    #Calculation for betting system
    try:
        tempOne = 1 / float(teamOne)
        tempTwo = 1 / float(teamTwo)
        tempThree = tempOne + tempTwo
        casTake = tempThree * 100
        w1 = round(float(wager) / (float(tempOne) / float(tempTwo) + 1), 2)
        w2 = round(float(wager) / (float(tempTwo) / float(tempOne) + 1), 2)
    except ZeroDivisionError as error:
        print('ERROR')
    #Outputs if the House Wins OR, If you win displays how much to place on each team. 
    if float(casTake) < 100:
       profitOne = round(float(w2) * float(teamOne) - float(wager),2)
       profitTwo = round(float(w1) * float(teamTwo) - float(wager),2)
       print("!!!PLACE BET!!!")
       print("Team One Bet: $" + str(w2) + "       --Profit: $" + str(profitOne))
       print("Team Two Bet: $" + str(w1) + "       --Profit: $" + str(profitTwo))
       print()
    elif casTake > 100:
       print("-----BAIL: House Wins-----" + "\n")
    elif casTake == 100:       
       print("EVEN SPREAD----100%")
    else:
       print("ERROR") 

tempNumb = 0    
for sports in sport_key:
    odds_response = requests.get('https://api.the-odds-api.com/v3/odds', params={
    'api_key': api_key,
    'sport': sport_key[tempNumb],
    'region': 'au', #Change as needed with options - uk | us | au
    'mkt': 'h2h' #Change as needed with options - h2h | spreads | totals
    })
    odds_json = json.loads(odds_response.text)
    if not odds_json['success']:
        print(
            'There was a problem with the odds request:',
            odds_json['msg']
        )
    else:
    # odds_json['data'] contains a list of live and 
    # upcoming events and odds for different bookmakers.
    # Events are ordered by start time (live events are first)
        print('----------------------------------------------------------------------------')
        print(
            'Successfully got {} events'.format(len(odds_json['data'])),
            'Hereare the ' + sport_key[tempNumb] + ' events:'
        )
        tempNum = 0
        #Getting the game Info
        for matches in odds_json['data']:
            tempDict = odds_json['data'][tempNum]
            #goes through each game and prints team
            for teams in tempDict['teams']:
                print(teams)
            teamOneHigh = float(0.0)
            teamTwoHigh = float(0.0)
            #for each game it outputs the odds and the site they are on
            for x in tempDict['sites']:
                tempH2hOdds = x['odds']
                if tempH2hOdds['h2h'][0] >= teamOneHigh:
                    teamOneHigh = float(tempH2hOdds['h2h'][0])
                if tempH2hOdds['h2h'][0] >= teamTwoHigh:
                    teamTwoHigh = float(tempH2hOdds['h2h'][1])
            if teamOneHigh == 0.00:
                print()
            elif teamTwoHigh == 0.00:
                print()
            else:
                houseOdds()
            tempNum += 1            
    tempNumb += 1
    
# Check your API Request usage
print()
print('Remaining requests', odds_response.headers['x-requests-remaining'])
print('Used requests', odds_response.headers['x-requests-used'])

