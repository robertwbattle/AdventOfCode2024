def part1():
    left_list = []
    right_list = []
    with open("inputs/1.txt", "r") as f:
        for line in f.readlines():
            x_1, x_2 = line.split("   ")
            left_list.append(int(x_1))
            right_list.append(int(x_2))
    left_list.sort()
    right_list.sort()

    total = 0
    for i in range(len(left_list)):
        total += abs(left_list[i]-right_list[i])
    return total

def part2():
    left_map = dict()
    right_map = dict()
    with open("inputs/1.txt", "r") as f:
        for line in f.readlines():
            x_1, x_2 = line.split("   ")
            x_1 = int(x_1)
            x_2 = int(x_2)
            if x_1 in left_map:
                left_map[x_1] += 1
            else:
                left_map[x_1] = 1
            
            if x_2 in right_map:
                right_map[x_2] += 1
            else:
                right_map[x_2] = 1
    total = 0
    for number in left_map:
        if number in right_map:
            total += left_map[number]*int(number)*right_map[number]
    return total

print("Part 1: ", part1())
print("Part 2: ", part2())