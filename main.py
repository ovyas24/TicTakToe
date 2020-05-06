import itertools,random
#with bot 
'''
    1.log every move and check for random move
    2.make it smart if you can 
'''
def bot():
    return random.randint(0,2),random.randint(0,2)
def win(current_game):
    def all_same(l):
        if l.count(l[0]) == len(l) and l[0] != 0:
            return True
        else:
            return False
    #horizontal
    for row in game:
        if all_same(row):
            print(f"Player {row[0]} is the winner Horizontally")
            return True

    #vertical
    for col in range(len(row)):
        check = []
        for row in game:
            check.append(row[col])
        if all_same(check):
            print(f"Player {check[0]} is the winner Verically")
            return True

    #daigonal
    daigs = []
    for ix in range(len(game)):
        daigs.append(game[ix][ix])
    if all_same(daigs):
        print(f"Player {daigs[0]} is the winner Daigonally")
        return True
    daigs=[]       
    for r,c in enumerate(reversed(range(len(game)))):
        daigs.append(game[r][c])
    if all_same(daigs):
        print(f"Player {daigs[0]} is the winner Daigonally")
        return True

def board(game,player=0,row=0,col=0,dis=False):
    try:
        if game[row][col] != 0:
            print("\033[1;31;40mthis position is occupied Choose Another!")
            return game,False
        print("\033[1;37;40m   0  1  2")
        if not dis:
            game[row][col] = player
        for count,row in enumerate(game):
            print(count,row)
        return game,True
    except IndexError as e:
        print("Error: Make sure you input row/column as 0,1 or 2?",e,"You Piece of shit you did it i know!!")
        return False
    except Exception as e:
        print("Somthing Went Very Wrong!! ",e)
        return game,False

play = True 
players = itertools.cycle([1,2])
while play:
    game =[[0,0,0],
           [0,0,0],
           [0,0,0]]
    game_won=False
    game,_ = board(game,dis=True)
    while not game_won:
        current_player = next(players)
        print(f"current player {current_player}")
        played = False
        while not played:
            if current_player==1:
                row_choice = int(input("\033[1;37;40mWhat row  do you wnat to play: "))
                column_choice = int(input("What column do you wnat to play:"))
            else:

                row_choice,column_choice = bot()
                 
            game,played = board(game,current_player,row_choice,column_choice)
            if played:
                print(f"\033[1;32;40mplayer {current_player} played {row_choice},{column_choice}\033[1;37;40m")
            game_won=win(game)