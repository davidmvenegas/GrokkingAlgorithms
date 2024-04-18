from collections import deque

friend_graph = {
    "David": ["Cassidy", "Jonas"],
    "Cassidy": ["David"],
    "Jonas": ["David", "Cassidy", "Eva"],
    "Eva": ["Jonas"],
    "Toby": ["Sarah"],
    "Sarah": ["Toby", "Eva"],
    "Erik": ["Sarah"],
    "Nora": ["Erik"],
    "Kaitlyn": ["Nora", "Erik", "Sarah", "Toby", "Eva"],
}


def bfs(witness, convicted_felon):
    # make an "already searched" set
    searched = set()

    # create a double-ended queue with the witness in it
    search_queue = deque([witness])

    # while the queue has people in it...
    while search_queue:
        person = search_queue.popleft()  # remove the next person from the queue
        if person not in searched:  # if they're not already searched...
            searched.add(person)  # add them to "visited" so we don't visit them again
            if person == convicted_felon:  # if they're the convicted_felon, nail 'em!
                return f"We found his ass! {person}, we know you're friends with {witness}. Don't try and funny business and no one has to get hurt. Come out with your hands where we can see 'em! I'll shoot! I'll fucking do it, SHOW YOUR HANDS DAMMIT! oh god he has a gun... *BANG BANG*"
            else:  # ...else, add their friends to the graph.
                search_queue.extend(friend_graph[person])

    return f"{witness} isn't friends with {convicted_felon}, but we'll get them next time... trust me, CRIME DOESN'T PAY."


print(bfs("Jonas", "Eva"))  # -> True
print()
print(bfs("David", "Sarah"))  # -> False
print()
print(bfs("Kaitlyn", "David"))  # -> True
