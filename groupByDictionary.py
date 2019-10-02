def group_by_owners(d):
    flipped = {}

    for key, value in d.items():
        if value not in flipped:
            flipped[value] = [key]
        else:
            flipped[value].append(key)

    return flipped



files = {
    'Input.txt': 'Randy',
    'Code.py': 'Stan',
    'Output.txt': 'Randy'
}
print(group_by_owners(files))