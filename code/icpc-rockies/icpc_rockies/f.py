n_islands, n_bridges = map(int, input().split())


class Node:
    def __init__(self, island_number, army_size, nxt):
        self.island_number = island_number
        self.army_size = army_size
        self.nxt = nxt

    def __str__(self):
        return f'island: {self.island_number}, \n army_size: {self.army_size}, \n next: {str(self.nxt)}'

    def add_node(self, nxt_node):
        self.nxt.append(nxt_node)

    def set_army(self, size):
        self.army_size = size


nodes = [Node(i, 0, []) for i in range(1, n_islands + 1)]

for i in range(n_bridges):
    a, b = map(int, input().split())

    # Add connection
    nodes[a - 1].add_node(nodes[b - 1])
    nodes[b - 1].add_node(nodes[a - 1])

for j in range(n_islands):
    # Set army values
    nodes[j].set_army(int(input()))


def conquer(head, army_size, nodes, previous):
    for node in head.nxt:
        print(head.island_number, "->", node.island_number)
        print("possible", node.nxt)
        if army_size > node.army_size:
            # can only conquer smaller armies
            army_size += node.army_size
            node.size = 0

            # move to the next island
            print(head.island_number, "CONQUERED", node.island_number)
            print("current army size", army_size)
            return conquer(node, army_size, nodes, head)
        else:
            print("END OF TREE", head.island_number, "COULDN'T CONQUER", node.island_number)

sizes = []
conquerer = nodes[0]
size = conquerer.army_size
conquerer.army_size = 0
print(conquerer.nxt)

for nxt_node in conquerer.nxt:
    print(nxt_node.island_number)
    sizes.append(conquer(nxt_node, size, nodes, conquerer))

print(sizes)


