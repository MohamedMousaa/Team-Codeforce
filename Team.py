lines = int(input())
count = 0
implemented_problems = 0
while lines > count:
    number_of_problems = input()
    count = count + 1
    number_one_counter = number_of_problems.count("1")
    if number_one_counter >= 2:
        implemented_problems = implemented_problems + 1
print(implemented_problems)