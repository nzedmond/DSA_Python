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

# Problem 2
def is_authentic_collection(art_pieces):

    if not art_pieces:
        return False

    n = len(art_pieces) - 1

    # numbers 1 to n-1 appear once... n appears twice.
    expected_count = {}
    for i in range(1, n):
        expected_count[i] = 1
    expected_count[n] = 2

    shipment_count = {}
    for piece in art_pieces:
        shipment_count[piece] = shipment_count.get(piece, 0) + 1

    return shipment_count == expected_count

collection1 = [2, 1, 3]
collection2 = [1, 3, 3, 2]
collection3 = [1, 1]

print(is_authentic_collection(collection1))
print(is_authentic_collection(collection2))
print(is_authentic_collection(collection3))