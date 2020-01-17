#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    """
    for weight, index in enumerate(weights):
        hash_table_insert(ht, index, weight)

    for i in range(len(weights)):
        check_weight = limit - weights[i]
        complementary_weight = hash_table_retrieve(ht, check_weight)

        if complementary_weight:
            return (complementary_weight, i)

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
