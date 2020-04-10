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
    counter = 0
    for weight in weights:
        hash_table_insert(ht, limit - weight, counter)
        if hash_table_retrieve(ht, weight) != None:
            if counter > hash_table_retrieve(ht, weight):
                print(counter, hash_table_retrieve(ht, weight))
                return(counter, hash_table_retrieve(ht, weight))
            else:
                print(hash_table_retrieve(ht, weight), counter)
                return(hash_table_retrieve(ht, weight), counter)


        counter += 1








    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
