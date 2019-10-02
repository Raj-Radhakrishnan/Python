def unique_names(names1, names2):
    names3 = names1 + names2
    names3 = list(set(names3))
    return names3


names1 = ["Ava", "Emma", "Olivia"]
names2 = ["Olivia", "Sophia", "Emma"]
print(unique_names(names1, names2)) # should print Ava, Emma, Olivia, Sophia