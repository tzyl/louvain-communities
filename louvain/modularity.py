from itertools import product


def modularity(G, partition):
    """Returns the modularity of the partition of an undirected graph G.

    Definition as given in:
        M. E. J. Newman. Networks: An Introduction, page 224.
    Oxford University Press, 2011.

    """
    m = G.size(weight="weight")
    degrees = dict(G.degree(weight="weight"))
    Q = 0
    for community in partition:
        for u, v in product(community, repeat=2):
            try:
                w = G[u][v].get("weight", 1)
            except KeyError:
                w = 0
            if u == v:
                # Double count self-loop weight.
                w *= 2
            Q += w - degrees[u] * degrees[v] / (2 * m)
    return Q / (2 * m)
