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

# Problem 3
def organize_exhibition(collection):
    # We need to display arts on the wall (2D array)
    # Keep track of the arts that meet the criteria
    display_wall = []
    print_counts = {}

    for art in collection:
        curr_count = print_counts.get(art, 0)
        print_counts[art] = curr_count + 1

        if curr_count >= len(display_wall):
            display_wall.append([])

        display_wall[curr_count].append(art)

    return display_wall

    

collection1 = ["O'Keefe", "Kahlo", "Picasso", "O'Keefe", "Warhol", 
              "Kahlo", "O'Keefe"]
collection2 = ["Kusama", "Monet", "Ofili", "Banksy"]

print(organize_exhibition(collection1))
print(organize_exhibition(collection2)) 
