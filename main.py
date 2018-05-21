from graph import Graph
import ast
import itertools


def add_nodes(g):

    nodes = ['a', 'b', 'c', 'd']
    for n in nodes:
        g.add_node(n)

def add_desc(g):
    desc = [('b', 'a'), ('b', 'c'), ('d', 'c')]

    for d in desc:
        g.add_desc(d)

def add_edges(g):

    edges = [('b', 'a'), ('b', 'c'), ('d', 'c')]

    for e in edges:
        g.add_edge(e)

def read_all_paths(n):
    all_paths = {}
    with open(n+'.txt', 'r') as infile:
        for line in infile:
            path = ast.literal_eval(line)
            if path:
                dest = path[-1][0]
                if dest in all_paths:
                    all_paths[dest].append(path)
                else:
                    all_paths[dest] = [path]

    return all_paths

def is_blocked(path, obs_dict, g):

    prev_edge = []

    for cur_edge in path:
        # try to find blocking transitions - either non-observed v-structures, or observed regulars

        if prev_edge:
            prev_node, prev_dir = prev_edge
            cur_node, cur_dir = cur_edge

            if prev_dir == 1 and cur_dir == 0:
                # V-structure

                blocking_v = True
                for n in g.nodes[prev_node].desc:
                    if obs_dict[n]:
                        blocking_v = False

                if blocking_v:
                    return True


            else:
                # not V-structure

                if obs_dict[prev_node]:
                    return True

        prev_edge = cur_edge

    return False



def is_indep(obs_dict, all_paths, g):

    for path in all_paths:
        block = is_blocked(path, obs_dict, g)
        if block:
            continue
        else:
            # we have found a non-blocked path, so indep does not hold
            return False

    return True

if __name__=='__main__':

    g = Graph()
    add_nodes(g)
    add_edges(g)
    add_desc(g)
    g.print_all_edges()
    g.print_all_descs()
    for n in g.nodes.keys():
        g.get_all_paths(n, n)

    all_nodes = list(g.nodes.keys())

    all_paths = {}
    for n in all_nodes:
        all_paths[n] = read_all_paths(n)

    s = len(all_nodes)
    obs_dict = {}

    combs = list(itertools.product([0,1], repeat = s))
    for c in combs:
        for n, val in zip(all_nodes, c):
            obs_dict[n] = val

        for i, j in itertools.combinations(all_nodes, 2):

            indep = is_indep(obs_dict, all_paths[i][j], g)
            if indep:
                observed = [all_nodes[idx] for idx, val in enumerate(c) if val]
                if (not (i in observed)) and (not (j in observed)):
                    print(i, j, str(observed))
                # print(i, j, str([all_nodes[idx] for idx, val in enumerate(c) if val]))


    g.reset_files()


