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
    
    for i in range(len(weights)):
        num_one = weights[i]
        num_two = hash_table_retrieve(ht, limit - num_one)
        if num_two != None:
            answer = (i, num_two)
            return answer
        hash_table_insert(ht, num_one, i)
        

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")

weights_2 = [4, 4]
answer_2 = get_indices_of_item_weights(weights_2, 2, 8)
