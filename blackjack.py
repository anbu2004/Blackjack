# Author: Anbuselven Ragunathan
# Date: November 16, 2021
# Description: A simulation of a Blackjack game. The player can start with a bet ranging from
#              $2000 to $10000.

### PROGRAM START ###

# Importing random library to determine strength of opponent's hand
import random

# Initializing variables needed for the game
user_total = 0
curr_total = 0
dealer_total = 0
user_list = []
game = True
insert = True

# Printing welcome message
print ("""Welcome to Blackjack!
With your minimum bet of $2000 and maximum bet of $10000, you will be playing a regular game of blackjack!
To win, you must get as close to 21 as possible, go over and you lose!
If your total is less than the dealer's, you lose!
To win, you must stay underneath 21 and have a higher total than the dealer. Doing so will award you $100!
If you lose, however, you will lose $100!
If you reach 21, that's a blackjack! You will win $150
""")

# While loop to ensure minimum requirement for money is met 
while (insert):
    money = round(float(input("Enter amount of money: ")),2)
    if (money < 2000):
        print ("Must put in at least $2000!")
        
    elif (money > 10000):
        print ("Must keep input under $10000!")
        
    else:
        insert = False


# While loop to start the game 
while (game):
    start = input("[Y] to play [N] to quit: ")
    start.upper()

    # Ensuring the user does not enter incorrect input
    if (start not in ("Y", "N")):
        print ("Invalid input!")
        start.upper()

    # Taking care of other scenarios and guiding the player through the game accordingly 
    elif (start == "N"):
        print ("You leave with $",money)
        print ("Thanks for playing!")
        game = False

    # Giving the player the option to add more money before the game begins 
    elif (start == "Y"):
        add = True
        while (add):
            add_money = round(float(input("Enter any more money before you begin: ")),2)
            money += add_money
            
            # Displaying to the user if their total amount goes over $10000 and subrtracting it to go back to their value from before
            if (money > 10000):
                print("Over $10000!")
                money -= add_money
            else:
                add = False
                
        # Clearing the user's hand of cards to begin playing
        user_list.clear()
        user_total = 0
        curr_total = 0 
        print ("You are starting with $",money)
        blackjack = True
        
        # Dealing the cards to the user
        for i in range (2):
            user_list.append(random.randrange(1,11))
            print ("You have: ", user_list[i])
            
        # Prompting the user if they want to hit or stand
        while (blackjack):
            choice = input("[H] to hit, [S] to stand: ")
            choice.upper()

            # Ensuring that the user does not enter invalid input
            if (choice not in ("H", "S")):
                print ("Invalid input!")
                choice.upper()
                
            # Taking care of the hit scenario
            elif (choice == "H"):
                curr_total = 0
                new_num = random.randrange(1,11)
                user_list.append(new_num)
                print ("Your new number is: ",new_num)
                
                # Updating the player's current score 
                for elem in (user_list):
                    curr_total += elem
                print ("Current total: ",curr_total)
                
                # Taking care of the Blackjack scenario
                if (curr_total == 21):
                    print ("Blackjack! You win!")
                    money += 150
                    print ("You now have $",money)
                    blackjack = False

                # Taking care of the bust scenario 
                elif (curr_total > 21):
                    print ("Over 21! You lose!")
                    money -= 1000

                    # Taking care of the bankrupt scenario 
                    if (money <= 0):
                        print ("You are bankrupt!")
                        print ("Game over!")
                        blackjack = False
                        game = False

                    else:
                        print ("You now have $",money)
                        blackjack = False
                        
            # Taking care of the stand scenario 
            elif (choice == "S"):
                for elem in (user_list):
                    user_total += elem
                print (user_total)
                # Dealer can only have a score greater than 16 and to simulate the odds in favour of the house, the range of numnbers the dealer
                # has are more favourable for them to win
                dealer_total = random.randrange(16,24)
                print (dealer_total)
                
                # Taking care of the scenario regarding the player winning
                if (dealer_total > 21 and user_total < 21):
                    print ("You win!")
                    money += 100
                    print ("You now have $",money)
                    blackjack = False
                    
                # Taking care of the bust scenario
                elif (user_total > 21):
                    print ("You lose!")
                    money -= 1000
                    
                    # Taking care of the bankrupt scenario 
                    if (money <= 0):
                        print ("You are bankrupt!")
                        print ("Game over!")
                        blackjack = False
                        game = False
                        
                    # Taking care of the scenario if there is still money
                    else:
                        print ("You now have $",money)
                        blackjack = False
                        
                # Taking care of the scenario if the dealer has a higher score under 21 
                elif (user_total < dealer_total):
                    print ("You lost!")
                    money -= 1000

                    # Taking care of the bankrupt scenario 
                    if (money <= 0):
                        print ("You are bankrupt!")
                        print ("Game over!")
                        blackjack = False
                        game = False
                        
                    # Taking care of the scenario if there is still money
                    else:
                        print ("You now have $",money)
                        blackjack = False
                        
                # Taking care of the scenario when there is a Blackjack for the player
                elif (user_total == 21):
                    print ("Blackjack! You win!")
                    money += 150
                    print ("You now have $",money)
                    blackjack = False
                    
                # Taking care of the scenario of whent hey player does not win through Blackjacck
                elif (user_total > dealer_total and not user_total > 21):
                    print ("You win!")
                    money += 100
                    print ("You now have $",money)
                    blackjack = False
                    
                # Taking care of a tie
                elif (user_total == dealer_total):
                    print ("Tie!")
                    money += 50
                    print ("You now have $",money)
                    blackjack = False

            
### PROGRAM END ###
                    
                    
                


                    
        
            
            
        
            
