print("Welcome to the stone game!")
stone_pile = int(input('Enter the total number of stones in the pile: '))
max_stone = int(input('Enter the maximum number of stones that can be taken at once: '))
p1 = str(input('Enter name of Player 1: '))
p2 = str(input('Enter name of Player 2: '))
who_start = int(input('Who should start the game? (1 for Player 1, 2 for Player 2): '))
print("Game Start!\n")

while stone_pile > 0:
    print(f'The current stone number is {stone_pile}')
    player_name = p1 if who_start == 1 else p2
    taken_stones = int(
        input(
        f"{player_name}', how many stones will you take (1 to {min(max_stone, stone_pile)})"
        )
    )
    
    if taken_stones < 1 or taken_stones > stone_pile or taken_stones > max_stone:
        print("Invalid number!")
        continue
    stone_pile -= min(taken_stones, stone_pile)
    
    who_start = 1 if who_start == 2 else 2
    
winner_player = p1 if who_start == 2 else p2
print(f"{winner_player} is the winner!")