###########################################################
#  Computer Project #10
#   
#   GAME:
#  
#    Thumb and Pouch Solitaire
#    
#    Promts for possible input moves
#    check if its a valid move
#    display the resultant 
#    game goes on until user enter enters 'q'
#
###########################################################


import cards        # this is required

YAY_BANNER = """
__   __             __        ___                       _ _ _ 
\ \ / /_ _ _   _    \ \      / (_)_ __  _ __   ___ _ __| | | |
 \ V / _` | | | |    \ \ /\ / /| | '_ \| '_ \ / _ \ '__| | | |
  | | (_| | |_| |_    \ V  V / | | | | | | | |  __/ |  |_|_|_|
  |_|\__,_|\__, ( )    \_/\_/  |_|_| |_|_| |_|\___|_|  (_|_|_)
           |___/|/                                            

"""

RULES = """
    *------------------------------------------------------*
    *-------------* Thumb and Pouch Solitaire *------------*
    *------------------------------------------------------*
    Foundation: Columns are numbered 1, 2, ..., 4; built 
                up by rank and by suit from Ace to King. 
                You can't move any card from foundation, 
                you can just put in.

    Tableau:    Columns are numbered 1, 2, 3, ..., 7; built 
                down by rank only, but cards can't be laid on 
                one another if they are from the same suit. 
                You can move one or more faced-up cards from 
                one tableau to another. An empty spot can be 
                filled with any card(s) from any tableau or 
                the top card from the waste.
     
     To win, all cards must be in the Foundation.
"""

MENU = """
Game commands:
    TF x y     Move card from Tableau column x to Foundation y.
    TT x y n   Move pile of length n >= 1 from Tableau column x 
                to Tableau column y.
    WF x       Move the top card from the waste to Foundation x                
    WT x       Move the top card from the waste to Tableau column x        
    SW         Draw one card from Stock to Waste
    R          Restart the game with a re-shuffle.
    H          Display this menu of choices
    Q          Quit the game
"""

def valid_fnd_move(src_card, dest_card): #check move to foundation is valid
    """
        Takes argument as src_card and dest_card
        and return true or false if the move is possible in foundation or not
    
    """
    if not dest_card and src_card.rank()==1: #if dest_card is not empty and scr_card is an ace card move is valid
        return True
    if dest_card.rank()==src_card.rank()-1 and dest_card.suit()==src_card.suit(): #rank is one less that the dest card and suit are different
        return True     #move is valid
    else:
        return False# any other case is an invalid move
        
def valid_tab_move(src_card, dest_card):    #check move to tab
    """
        Takes argument as src_card and dest_card
        and return true or false if the move is possible in tableau or not
        

    """    

    
    if not dest_card:#if dest card is empty
        return True
    
    elif dest_card.rank()-1==src_card.rank() and dest_card.suit()!=src_card.suit(): #check move
        return True#card rank is one less and suit are different return true
    
    else:
        return False#any other case is an invalid move
            
def tableau_to_foundation(tab, fnd):# tab to foundation move
    """
        Takes argument as TAB and fnd
        and return true or false if the move is possible in foundation or not
        checks for empty tab, suit, and rank

    """    
    
    if not fnd or (valid_fnd_move(tab[-1],fnd[-1]) and tab[-1].is_face_up()):
        fnd.append(tab[-1])#add desired card to foundation
        tab.pop()#remove card from tab
        if tab and not tab[-1].is_face_up():#if tab is not empty and card is not facing up
            tab[-1].flip_card()#flip the card
        
    else:#any other case raise runtimeerror
        raise RuntimeError('Error: invalid move due to mismatched cards') 
            

def tableau_to_tableau(tab1, tab2, n):
    """
    Takes argument as tab1 and tab2
    and return true or false if the move is possible in tableau or not
    checks for empty tab, suit, and rank

    """    

    if not tab2 or valid_tab_move(tab1[-n],tab2[-1]):
        for i in tab1[-n:]:#checks if the cards to be moved are flipped up
            if not i.is_face_up():
                raise RuntimeError('Error: insufficient number of cards to move')
        tab2+=tab1[-n:]

        for i in range(n):#removes card that are added to tab2
            tab1.pop()

        if tab1 and not tab1[-1].is_face_up():#flips card if its not flipped
            tab1[-1].flip_card()

    else:
        raise RuntimeError('Error: invalid move due to mismatched cards')
        
def waste_to_foundation(waste, fnd, stock):
    """
    Takes argument as waste and fnd and stock
    and moves a card from waste to foundation
    checks for empty tab, suit, and rank
    
    """    
    if not fnd:#if its not empty
        if waste[-1].rank()==1:# and rank is ACE
            fnd.append(waste[-1])#adds it to foundation
            waste.pop(-1)#remove card
        else:
            raise RuntimeError('Error: invalid command because card is not ACE')
    elif valid_fnd_move(waste[-1],fnd[-1]):#if valid move
        fnd.append(waste[-1])#does the work
        waste.pop(-1)
    else:
        raise RuntimeError('Error: invalid move due to mismatched cards')
        
def waste_to_tableau(waste, tab, stock):
    """
    Takes argument as waste tab and stock 
    and adds card to tab from waste
    checks for empty tab, suit, and rank
    """    
    if not waste: # if waste is not empty raise error
        raise RuntimeError('Error: invalid command because waste is Empty')
    if not tab or valid_tab_move(waste[-1],tab[-1]):#if tab is full and valid move is TRUE
        tab.append(waste[-1])#does the work
        waste.pop(-1)
    else:
        raise RuntimeError('Error: invalid move due to mismatched cards')
        
                    
def stock_to_waste(stock, waste):
    """
    Takes argument as stock and waste
    and adds a card to waste
    checks for empty stock
    """    
    if stock:
        waste.append(stock.deal())#if stock is not empty adds a card to waste
    else:
        raise RuntimeError('Error: invalid command because stock empty')
        
        
def is_winner(foundation):
    """
        checks for the winner.
    """    
    for i in foundation:
        if len(i)<13:#if foundation has 13 cards in all the tabs thats a winner case
            return False
    return True

def setup_game():
    """
        The game setup function, it has 4 foundation piles, 7 tableau piles, 
        1 stock and 1 waste pile. All of them are currently empty. This 
        function populates the tableau and the stock pile from a standard 
        card deck. 

        7 Tableau: There will be one card in the first pile, two cards in the 
        second, three in the third, and so on. The top card in each pile is 
        dealt face up, all others are face down. Total 28 cards.

        Stock: All the cards left on the deck (52 - 28 = 24 cards) will go 
        into the stock pile. 

        Waste: Initially, the top card from the stock will be moved into the 
        waste for play. Therefore, the waste will have 1 card and the stock 
        will be left with 23 cards at the initial set-up.

        This function will return a tuple: (foundation, tableau, stock, waste)
    """
    # you must use this deck for the entire game.
    # the stock works best as a 'deck' so initialize it as a 'deck'
    stock = cards.Deck()
    stock.shuffle()

    # the game piles are here, you must use these.
    foundation = [[], [], [], []]           # list of 4 lists
    tableau = [[], [], [], [], [], [], []]  # list of 7 lists
    waste = []                              # one list
    
    x=0#to help with dealing 
    for i in range (7):
        for j in range(7-x):#even i dont know how this works but it does
            flipped_card=stock.deal()#stores dealt card 
            flipped_card.flip_card()#flip it
            tableau[j+x].append(flipped_card)#add it to tableau at the correct possition
        x+=1#increaments x
    #x decreases the number of cards that are delt to make a triangle matrix of tableau cards
    
    for i in range(7):#since all the cards are flipped
        tableau[i][-1].flip_card()#this flips the last card of each tab
                
        
    waste.append(stock.deal()) #adds one card to waste to begin the game
    
    return foundation, tableau, stock, waste

def display_game(foundation, tableau, stock, waste):
    """
        display the ongoing game.
    """    
    print('================= FOUNDATION =================')
    header_foundation=['f1','f2','f3','f4']
    for i in header_foundation:
        print('{:<10s}'.format(i),end="")#display f1 f2... 
    print()   
    for i in foundation:#display last foundation card 
        if len(i)>0:
            print('[ {}]'.format(i[-1],''),end="     ")
        else:
            print('{:<10}'.format('[   ]'),end="")
    print()#
    print('==================  TABLEAU  =================')
    header_tableau=['t1','t2','t3','t4','t5','t6','t7',]
    
    y=[len(i) for i in tableau]#len of tabs list
    print(end=' ')
    for i in header_tableau:#display t1 t2...
        print('{:<7s}'.format(i),end="")
    print()
    print(end=' ')

  #  str(my_card)

    for row in range(7+13):#thats the maximum number of card in a row 6 face down and 13 in a suit 
        for col in range(7):#maximum number of column
            if len (tableau[col])<row+1:# if makes the desired matrix of cards
                print('{:>7s}'.format(''),end='')
                continue
                
            if tableau[col][row]:
                print('{:<7s}'.format(str(tableau[col][row])),end='')#print the cards with formating
        print('\n',end=' ')
        if row > max(y):#break the loop if no cards left
            break
        
    print('================= STOCK/WASTE =================')
    print('Stock #({}) ==> '.format(len(stock)),end=' ')
    print(waste)

print(RULES)
fnd, tab, stock, waste = setup_game()
display_game(fnd, tab, stock, waste)
print(MENU)
command = input("prompt :> ")
while command.strip().lower() != 'q':#stops at q
    try:
        command_list=command.split()        
        command_len=len(command_list)
        if command.strip().lower() == 'h':
            print(MENU)
        elif command.strip().lower() == 'r':
            print(RULES)
            fnd, tab, stock, waste = setup_game()
            display_game(fnd, tab, stock, waste)
            print(MENU)
            command = input("prompt :> ")
            
        elif command.strip().lower() == 'sw':
            if command_len != 1:#check for number if commands
                raise RuntimeError('Error: wrong number of arguments')
            stock_to_waste(stock,waste)#does the work
            
        elif 'wt' in command.strip().lower():
            
            if command_len != 2:#check for number if commands
                raise RuntimeError('Error: wrong number of arguments') 
            
            if int(command_list[1]) not in range(1,8):
                print(command_list[1])
                raise RuntimeError('Error: arguments must be numbers in range')
            
            waste_to_tableau(waste,tab[int(command_list[1])-1],stock)#does the work
            
        elif 'wf' in command.strip().lower():
            
            if command_len != 2:#check for number if commands
                raise RuntimeError('Error: wrong number of arguments')  
                
            if int(command_list[1]) not in range(1,5):
                print(command_list[1])
                raise RuntimeError('Error: arguments must be numbers in range')

            waste_to_foundation(waste,fnd[int(command_list[1])-1],stock)#does the work
        
        elif 'tf' in command.strip().lower():
            if command_len != 3:#check for number if commands
                raise RuntimeError('Error: wrong number of arguments')  
                
            if int(command_list[1]) not in range(1,8):
                print(command_list[1])
                raise RuntimeError('Error: arguments must be numbers in range')
            if int(command_list[2]) not in range(1,5):
                print(command_list[1])
                raise RuntimeError('Error: arguments must be numbers in range')

            tableau_to_foundation(tab[int(command_list[1])-1],fnd[int(command_list[2])-1])#does the work
        
            
        elif 'tt' in command.strip().lower():
            if command_len != 4:#check for number if commands
                raise RuntimeError('Error: wrong number of arguments')
                
            if int(command_list[1]) not in range(1,8):
                print(command_list[1])
                raise RuntimeError('Error: arguments must be numbers in range')
            if int(command_list[2]) not in range(1,8):
                print(command_list[1])
                raise RuntimeError('Error: arguments must be numbers in range')
                
            if int(command_list[3])<1:
                print(command_list[1])
                raise RuntimeError('Error: arguments must be numbers in range')
                
            tableau_to_tableau(tab[int(command_list[1])-1],tab[int(command_list[2])-1],int(command_list[3]))#does the work
        elif '' == command.strip().lower():
            raise RuntimeError('Error: no command entered')
        else:
            raise RuntimeError('{} is an Invalid Command'.format(command))
            
    except RuntimeError as error_message:  # any RuntimeError you raise lands here
        print("{:s}\nTry again.".format(str(error_message)))       

    if is_winner(fnd):#checks for win situation
        print(YAY_BANNER)
    display_game(fnd, tab, stock, waste)                
    command = input("prompt :> ")
        