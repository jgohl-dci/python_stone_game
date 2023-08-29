print("Welcome to the stone game!")
stone_pile = int(input('Enter the total number of stones in the pile: '))
max_stone = int(input('Enter the maximum number of stones that can be taken at once: '))
p1 = str(input('Enter name of Player 1: '))
p2 = str(input('Enter name of Player 2: '))
who_start = int(input('Who should start the game? (1 for Player 1, 2 for Player 2): '))
print("Game Start!\n")

while stone_pile >= 1:
    print('Currently there are', stone_pile, 'stones on the pile.')
    
    if who_start == 1:
        check = 1
        while check == 1:
            print(p1, end=' ')
            stones_take = int(input('how many stones you want to take from the pile? '))
            if stones_take <= max_stone and stones_take <= stone_pile:
                stone_pile -= stones_take
                check = 0
            else:
                print('Invalid number! There are only', stone_pile, 'stones on the pile.')
            
        who_start = 2
    elif who_start == 2:
        check = 1
        while check == 1:
            print(p2, end=' ')
            stones_take = int(input('how many stones you want to take from the pile? '))
            if stones_take <= max_stone and stones_take <= stone_pile:
                stone_pile -= stones_take
                check = 0
            else:
                print('Invalid number! There are only', stone_pile, 'stones on the pile.')
        who_start = 1
        
if who_start == 2:
    print("Congrats", p1, 'you won the game!')
elif who_start == 1:
    print("Congrats", p2, 'you won the game!')
