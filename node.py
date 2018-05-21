class Node:

    def __init__(self, nid):

        self.nid = nid
        self.edges = []
        self.desc = [nid]


    def add_edge(self, nid, direction):

        self.edges.append((nid, direction))

    def print_all_edges(self):

        print(self.edges)

    def print_descs(self):
        print(self.nid, ' and descs is: ', self.desc)