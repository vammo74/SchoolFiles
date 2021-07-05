# there are four people that are trying to cross a rickety bridge at night
# A takes 1 min
# B takes 2 min
# C takes 5 min
# D takes 8 min
# they have a torch that burns down in 15 min can they all cross?

# minimum tours 5
# total combinations 4x3 x 2 x 3x2 x 3 x 1 = 432


dict_left = {'a': 1, 'b': 2, 'c': 5, 'd': 8}
dict_right= {}

x = 0

    
for person, time in dict_left.items():
    dict_right[person] = time
    

    for person2, time2 in dict_left.items():
        dict_right[person] = time
        del dict_left[person]
        del dict_left[person2]
        x = x + time

print(x)
print(dict_left)
print(dict_right)
