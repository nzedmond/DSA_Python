# Problem set version 1
# Q1
def find_balanced_subsequence(art_pieces):
    frequencies = {} # each art piece value
    for value in art_pieces:
        frequencies[value] = frequencies.get(value, 0) + 1

    max_length = 0
    for value in frequencies:
        if value + 1 in frequencies:
            current_length = frequencies[value] + frequencies[value + 1]
            max_length = max(max_length, current_length)
    return max_length



art_pieces1 = [1,3,2,2,5,2,3,7]
art_pieces2 = [1,2,3,4]
art_pieces3 = [1,1,1,1]

print(find_balanced_subsequence(art_pieces1))
print(find_balanced_subsequence(art_pieces2))
print(find_balanced_subsequence(art_pieces3))  