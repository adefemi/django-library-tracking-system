import random
rand_list = [random.randint(1, 20) for _ in range(10)]

list_comprehension_below_10 = [x for x in rand_list if x < 10]

def handler(x): # just for better readability
    return x < 10

# list_comprehension_below_10 = using filter
list_comprehension_below_10_with_filter = list(filter(handler, rand_list))