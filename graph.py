from node import Node

outgoing = 1
incoming = 0
selfie = -1

class Graph:

    def __init__(self):

        self.nodes = {}

    def add_node(self, nid):

        self.nodes[nid] = Node(nid)

    def add_desc(self, d):

        src, dest = d

        self.nodes[src].desc.append(dest)

    def add_edge(self, edge):

        _from, _to = edge

        self.nodes[_from].add_edge(_to, outgoing)
        self.nodes[_to].add_edge(_from, incoming)

    def print_all_edges(self):

        for n in self.nodes.values():
            n.print_all_edges()

    def print_all_descs(self):

        for n in self.nodes.values():
            n.print_descs()

    def get_all_paths(self, start, nid, in_path = []):

        path = list(in_path)

        for (nbr, dir) in self.nodes[nid].edges:

            if (nbr, dir) not in path:
                path.append((nbr, dir))
                self.get_all_paths(start, nbr, path)

            path = list(in_path)

        with open(start + '.txt', 'a') as outfile:
            outfile.write(str(path))
            outfile.write('\n')
        return path

    def reset_files(self):

        for node in self.nodes.values():
            node_letter = node.nid
            with open(node_letter + '.txt', 'w') as outfile:
                outfile.write('')