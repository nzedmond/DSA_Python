from collections import defaultdict

def total_treasure(treasure_map):
    sum_treasure = 0

    for key in treasure_map:
        sum_treasure += treasure_map[key]
    return sum_treasure

treasure_map1 = {
    "Cove": 3,
    "Beach": 7,
    "Forest": 5
}

treasure_map2 = {
    "Shipwreck": 10,
    "Cave": 20,
    "Lagoon": 15,
    "Island Peak": 5
}

print(total_treasure(treasure_map1))
print(total_treasure(treasure_map2))

def can_trust_message(message):
    count = {}
    for i in message:
        if i != " ":
            count[i] = count.get(i, 0) + 1

    return len(count) == 26

message1 = "sphinx of black quartz judge my vow"
message2 = "trust me"

print(can_trust_message(message1))
print(can_trust_message(message2))

print("========Question 3========")

def find_duplicate_chests(chests):
    freq = defaultdict(int)
    for i in chests:
        freq[i] += 1

    dup_arr = []
    for k in freq:
        if freq[k] == 2:
            dup_arr.append(k)

    return dup_arr

chests1 = [4, 3, 2, 7, 8, 2, 3, 1]
chests2 = [1, 1, 2]
chests3 = [1]

print(find_duplicate_chests(chests1))
print(find_duplicate_chests(chests2))
print(find_duplicate_chests(chests3))

print("=======Question 4=======")

def can_make_balanced(code):
    n = len(code)
    chars_dict = defaultdict(int)
    for char in code:
        chars_dict[char] += 1

    return n % len(chars_dict) == 1

code1 = "arghh"
code2 = "haha"

print(can_make_balanced(code1)) 
print(can_make_balanced(code2)) 

print("========Question 5==========")

def find_treasure_indices(gold_amounts, target):
    ind_dict = {}
    # ind_arr = []
    for index, value in enumerate(gold_amounts):
        result = target - value
        if result in ind_dict.keys():
            return [index, ind_dict[result]]

        else:
            ind_dict[value] = index

gold_amounts1 = [2, 7, 11, 15]
target1 = 9

gold_amounts2 = [3, 2, 4]
target2 = 6

gold_amounts3 = [3, 3]
target3 = 6

print(find_treasure_indices(gold_amounts1, target1))  
print(find_treasure_indices(gold_amounts2, target2))  
print(find_treasure_indices(gold_amounts3, target3))  

print("========Question 6========")