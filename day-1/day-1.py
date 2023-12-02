FIRST_TEN_INTS = [str(i) for i in range(10)]
FIRST_TEN_SPELLED_INTS = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
FIRST_TEN_SPELLED_INTS_REVERSED = [i[::-1] for i in FIRST_TEN_SPELLED_INTS]

MAP = {k: v for k, v in zip(FIRST_TEN_SPELLED_INTS, FIRST_TEN_INTS[1:10])}
MAP_REVERSED = {k: v for k, v in zip(FIRST_TEN_SPELLED_INTS_REVERSED, FIRST_TEN_INTS[1:10])}

def main(file_path):
    sum = 0
    with open(file_path, "r") as file:
        for line in file:
            first_number = 10
            last_number = 10
            for c in line:
                if c in FIRST_TEN_INTS:
                    if first_number == 10:
                        first_number = c
                    else:
                        last_number = c
            if last_number == 10:
                last_number = first_number
            
            calibration = int(first_number) * 10 + int(last_number)
            print(calibration)
            sum += calibration
    return sum

file_path = "input-1.txt"
# sum = main(file_path)
# print(f"FINAL ANSWER: {sum}")

def find_lines_first_number(line):
    for i in range(len(line)):
        if line[i] in FIRST_TEN_INTS:
            first_number = line[i]
            return int(first_number)
        elif line[i+1] in FIRST_TEN_INTS:
            first_number = line[i+1]
            return int(first_number)
        else:
            for number in FIRST_TEN_SPELLED_INTS:
                num_len = len(number)
                # print(number)
                # print(line[i: i + num_len])
                if number == line[i: i + num_len]:
                    first_number = int(MAP[number])
                    return first_number

def find_lines_last_number(line):
    line = line[::-1]
    for i in range(len(line)):
        if line[i] in FIRST_TEN_INTS:
            last_number = line[i]
            return int(last_number)
        elif line[i+1] in FIRST_TEN_INTS:
            last_number = line[i+1]
            return int(last_number)
        else:
            for number in FIRST_TEN_SPELLED_INTS_REVERSED:
                num_len = len(number)
                if number == line[i: i + num_len]:
                    last_number = int(MAP_REVERSED[number])
                    return last_number     




def main_part_two(file_path):
    with open(file_path, "r") as file:
        sum = 0
        for line in file:
            first_number = find_lines_first_number(line)
            # print(f"{first_number=}")
            last_number = find_lines_last_number(line)
            # print(f"{last_number=}")

            calibration = first_number * 10 + last_number
            print(calibration)
            sum += calibration
    
    return sum


# sum = main_part_two(file_path)
# print(sum)

# print(find_lines_first_number("nkzjrdqrmpztpqninetwofour1znnkd"))
# print(find_lines_last_number("nkzjrdqrmpztpqninetwofour1znnkd"))
print(main_part_two(file_path))
