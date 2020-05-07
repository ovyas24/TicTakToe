import itertools
from os import system,name
def board(game):
	print(f" {game[0][0]} | {game[0][1]} | {game[0][2]} ")
	print("---|---|---")
	print(f" {game[1][0]} | {game[1][1]} | {game[1][2]} ")
	print("---|---|---")
	print(f" {game[2][0]} | {game[2][1]} | {game[2][2]} ")
	return game

def win(current_game):
    def all_same(l):
        if l.count(l[0]) == len(l) and l[0] != 0:
            return True
        else:
            return False
    #horizontal
    for row in game:
        if all_same(row):
            return True

    #vertical
    for col in range(len(row)):
        check = []
        for row in game:
            check.append(row[col])
        if all_same(check):
            return True,0

    #daigonal
    daigs = []
    for ix in range(len(game)):
        daigs.append(game[ix][ix])
    if all_same(daigs):
        return True
    daigs=[]       
    for r,c in enumerate(reversed(range(len(game)))):
        daigs.append(game[r][c])
    if all_same(daigs):
        return True

def clear():
	if name == 'nt':
		_= system('cls')
	else:
		_= system('clear')

def move(player=0,pos=0):
	#liner search algo
	for i in range(len(game)):
		for j in range(len(game[i])):
			#print(game[i][j],pos)
			if game[i][j] == pos:
				#print(i,j)
				if player == 1:
					game[i][j] = 'X'
				elif player == 2:
					game[i][j] = 'O'
				return True
	return False
			#return True
			#if player 1 than X and player 2 than O

player = itertools.cycle([1,2])
play=True
while play:
	ch = input("Press 'Y' To Start game: ")
	if ch =="Y":
		clear()
	game = [[1,2,3],[4,5,6],[7,8,9]]
	game = board(game)
	gameWon = False
	tai=0
	while not gameWon:
		Current_player = next(player)
		played = False
		while not  played:
			pos = int(input(f"Player {Current_player} : Choose the number where you want to Play: "))
			played = move(Current_player,pos)
			if not gameWon:
				clear()
			game = board(game)
			if not played:
				print("Chose Again!!!!")
			gameWon = win(game)

	print(f"Game Won By Player {Current_player}")


	ch = input("Wana play Again: (yes/no)")
	if ch =="yes":
		clear()
	elif ch =="no":
		play = False
	else:
		print("KeyWord error!!!! closing Game !!!!...!!!!")
		play = False


print("Thanks For playing!!! :)")