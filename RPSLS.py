# Rock-paper-scissors-lizard-Spock template

# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

def name_to_number(name):
    # convert name to number using if/elif/else
    # don't forget to return the result!
    ans = -1
    if (name=="rock") ans=0
    elif (name=="Spock") ans=1
    elif (name=="paper") ans=2
    elif (name=="lizard") ans=3
    elif (name=="scissors") ans=4
    else
        print "Option non valid"
    return ans




def number_to_name(number):
    ans = ""
    if (number==0) ans="rock"
    elif (name==1) ans="Spock"
    elif (name==2) ans="paper"
    elif (name==3) ans="lizard"
    elif (name==4) ans="scissors"
    else
        print "Number out of range"
    return ans

def rpsls(player_choice): 
    # print a blank line to separate consecutive games
    print "\n"
    # print out the message for the player's choice
    print "Give me your choice: "
    player_choice = raw_input(prompt)
    # convert the player's choice to player_number using the function name_to_number()
    player_number = name_to_number(player_choice)
    # compute random guess for comp_number using random.randrange()
    comp_choice= random.randrange(0,4)
    # convert comp_number to comp_choice using the function number_to_name()
    comp_number= name_to_number(comp_choice)    
    # print out the message for computer's choice
    print "The computer choice is:", comp_choice
    # compute difference of comp_number and player_number modulo five
    diff=(comp_choice-player_choice)%5
    # use if/elif/else to determine winner, print winner message
    if (diff<3)
        print 
  
    
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric


