#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)

ht = HashTable(16)
print(len(ht.storage))
def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    """
    if len(ht.storage) < length:
        hash_table_resize(ht)
    for parcels in weights:
        index = 0
        hash_table_insert(ht, index, parcels)
        pair = limit - parcels
        print(pair)
        index += 1






    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
