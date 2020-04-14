#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route_length = length - 1
    route = [None] * route_length

    for ticket in tickets:
        hash_table_insert(hashtable, ticket.source, ticket.destination)
    a = 0;

    for ticket in range(length-1):

        if a == 0:
            route[a] = hash_table_retrieve(hashtable, "NONE")
            a += 1
        else:
            if hash_table_retrieve(hashtable, route[a-1]) == "None":
                return
            route[a] = hash_table_retrieve(hashtable, route[a-1])
            a += 1
    print(route)
    return route


