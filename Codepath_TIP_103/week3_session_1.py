# Counting the layers of a sandwich
import time

def count_layers(sandwich):
    if not sandwich:
        return 0

    # base case
    if len(sandwich) == 1:
        return 1

    return count_layers(sandwich[1]) + 1

run_time = time.time()
sandwich1 = ["bread", ["lettuce", ["tomato", ["bread"]]]]
sandwich2 = ["bread", ["cheese", ["ham", ["mustard", ["bread"]]]]]
print(count_layers(sandwich1))
print(time.time() - run_time)

print(count_layers(sandwich2))

# Reversing Deli Orders
def reverse_orders(order):
    if ' ' not in order:
        return order

    first_element, rem_orders = order.split(' ', 1)

    return reverse_orders(rem_orders)+' '+first_element



print(reverse_orders("Bagel Sandwich Coffee"))  

# Sharing coffee
def can_split_coffee(coffee, n):
    total_volume = sum(coffee)

    if total_volume % n != 0:
        return False
    # targ_volume = total_volume // n

    def add_coffee(coffee, i):
        if i == len(coffee):
            return 0
        return coffee[i] + add_coffee(coffee, i+1)

    return add_coffee(coffee, 0) % n == 0


print(can_split_coffee([4, 4, 8], 2))
print(can_split_coffee([5, 10, 15], 4))