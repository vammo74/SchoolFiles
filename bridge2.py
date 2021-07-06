# there are four people that are trying to cross a rickety bridge at night
# A takes 1 min
# B takes 2 min
# C takes 5 min
# D takes 8 min
# they have a torch that burns down in 15 min can they all cross?

# minimum tours 5
# total combinations 4x3 x 2 x 3x2 x 3 x 1 = 432
#
#


starting_people = [{"A": 1}, {"B": 2}, {"C": 5}, {"D": 8}]

result = []

first_pass = []

for person_one in starting_people:
    for person_two in starting_people:
        if person_one != person_two and [person_two, person_one] not in first_pass:
            first_pass.append([person_one, person_two])

for element in first_pass:
    temp_dict = {}
    permutation = {1: [], 2: [], 3: [], 4: [], 5: []}
    for n in element:
        for key, value in n.items():
            temp_dict[key] = value

    permutation[1] = temp_dict
    result.append(permutation)


second_pass = []

for element in result:
    first_people = element[1]
    permutation_one = dict({1: first_people, 2: [], 3: [], 4: [], 5: []})
    permutation_two = dict({1: first_people, 2: [], 3: [], 4: [], 5: []})
    temp_dict_one = {}
    temp_dict_two = {}
    temp_list = []

    for key, value in first_people.items():
        temp_list.append(key)
        temp_list.append(value)

    temp_dict_one[temp_list[0]] = temp_list[1]
    temp_dict_two[temp_list[2]] = temp_list[3]

    permutation_one[2] = temp_dict_one
    permutation_two[2] = temp_dict_two

    second_pass.append(permutation_one)
    second_pass.append(permutation_two)


third_pass = []

for element in second_pass:
    first_people = element[1]
    temp_first_people = dict.copy(first_people)
    second_people = element[2]
    for key, value in second_people.items():
        temp_first_people.pop(key)
    for key, value in temp_first_people.items():
        left_people = {"A": 1, "B": 2, "C": 5, "D": 8}
        left_people.pop(key)

    temp_list = []

    for key, value in left_people.items():
        temp_list.append(key)
        temp_list.append(value)
        samlings_list = []

    for i in range(0, 5, 2):
        for j in range(0, 5, 2):
            if i != j and [j, i] not in samlings_list:
                samlings_list.append([i, j])

    for element in samlings_list:
        third_people = {}
        third_people[temp_list[element[0]]] = temp_list[element[0] + 1]
        third_people[temp_list[element[1]]] = temp_list[element[1] + 1]

        permutation = dict(
            {1: first_people, 2: second_people, 3: third_people, 4: [], 5: []}
        )
        third_pass.append(permutation)

fourth_pass = []

for element in third_pass:
    first_people = element[1]
    second_people = element[2]
    third_people = element[3]

    temp = []

    for key, value in first_people.items():
        temp.append(key)

    for key, value in second_people.items():
        temp.remove(key)

    for key, value in third_people.items():
        temp.append(key)

    all_people = {"A": 1, "B": 2, "C": 5, "D": 8}

    for key in temp:
        temp_dict = {}
        temp_dict[key] = all_people[key]
        permutation = dict(
            {1: first_people, 2: second_people, 3: third_people, 4: temp_dict, 5: []}
        )
        fourth_pass.append(permutation)

fifth_pass = []

for element in fourth_pass:
    first_people = element[1]
    second_people = element[2]
    third_people = element[3]
    fourth_people = element[4]

    temp = ["A", "B", "C", "D"]

    for key, value in first_people.items():
        temp.remove(key)

    for key, value in second_people.items():
        temp.append(key)

    for key, value in third_people.items():
        temp.remove(key)

    for key, value in fourth_people.items():
        temp.append(key)

    fifth_people = {}

    all_people = {"A": 1, "B": 2, "C": 5, "D": 8}
    for key in temp:
        fifth_people[key] = all_people[key]

    permutation = dict(
        {
            1: first_people,
            2: second_people,
            3: third_people,
            4: fourth_people,
            5: fifth_people,
        }
    )

    fifth_pass.append(permutation)

# calculations
print(fifth_pass)
print(len(fifth_pass))

times = []

for element in fifth_pass:

    time = 0
    for i in range(1, len(element) + 1):
        temp_time = 0
        for key, value in element[i].items():
            if value > temp_time:
                temp_time = value
        time = time + temp_time
    times.append(time)

print(times)
