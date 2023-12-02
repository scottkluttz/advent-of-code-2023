RED_CUBES = 12
GREEN_CUBES = 13
BLUE_CUBES = 14

MAX_COLORS_MAP = {"red": RED_CUBES, "green": GREEN_CUBES, "blue": BLUE_CUBES}

input_file = "input-2.txt"

def game_round_possible(game_round):
    game_round_possible = True
    trial = game_round.split(',')
    trial = [entry.strip() for entry in trial]
    # print(trial)
    for entry in trial:
        first_space_index = entry.find(" ")
        color = entry[first_space_index+1:len(entry)]
        number = entry[0:2]
        max_color = MAX_COLORS_MAP[color]
        if int(number) > max_color:
            game_round_possible = False
            break
    return game_round_possible

def game_round_power(game_round):
    game_round_possible = True
    trial = game_round.split(',')
    trial = [entry.strip() for entry in trial]
    maxes = {"red": 0, "green": 0, "blue": 0}
    # print(trial)
    for entry in trial:
        first_space_index = entry.find(" ")
        color = entry[first_space_index+1:len(entry)]
        number = entry[0:2]
        max_color = maxes[color]
        if int(number) > max_color:
            maxes[color] = int(number)
    print(maxes)
    return maxes["red"] * maxes["blue"] * maxes["green"]

def main(input_file):
    possible_games = 0
    id_sum = 0
    with open(input_file, "r") as file:
        for line in file:
            print(line)
            first_space_index = line.find(" ")
            second_space_index = line.find(" ", first_space_index + 1)
            id = line[first_space_index + 1: second_space_index-1]
            print(id)
            print(id)
            rounds = line[second_space_index + 1:].split(';')
            # print(rounds)
            round_possible = True
            for game_round in rounds:
                game_round_possible_bool = game_round_possible(game_round)
                if not game_round_possible_bool:
                    round_possible = False
                    break
            if round_possible:
                possible_games +=1
                id_sum += int(id)
                print(possible_games)
                print(id_sum)
    return possible_games

def main_2(input_file):
    power_sum = 0
    with open(input_file, "r") as file:
        for line in file:
            print(line)
            first_space_index = line.find(" ")
            second_space_index = line.find(" ", first_space_index + 1)
            rounds = line[second_space_index + 1:].split(';')
            # print(rounds)
            maxes = {"red": 0, "green": 0, "blue": 0}

            for game_round in rounds:
                game_round_possible = True
                trial = game_round.split(',')
                trial = [entry.strip() for entry in trial]
                # print(trial)
                for entry in trial:
                    first_space_index = entry.find(" ")
                    color = entry[first_space_index+1:len(entry)]
                    number = entry[0:2]
                    max_color = maxes[color]
                    if int(number) > max_color:
                        maxes[color] = int(number)
                print(maxes)
            
            power = maxes["red"] * maxes["blue"] * maxes["green"]
            power_sum += power
                
    return power_sum


# possible_games = main(input_file)
possible_games = main_2(input_file)
print(possible_games)
