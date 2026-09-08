'''Timofey has an apple tree growing in his garden; it is a rooted tree of n
 vertices with the root in vertex 1
 (the vertices are numbered from 1
 to n
). A tree is a connected graph without loops and multiple edges.

This tree is very unusual — it grows with its root upwards. However, it's quite normal for programmer's trees.

The apple tree is quite young, so only two apples will grow on it. Apples will grow in certain vertices (these vertices may be the same). After the apples grow, Timofey starts shaking the apple tree until the apples fall. Each time Timofey shakes the apple tree, the following happens to each of the apples:

Let the apple now be at vertex u
.

If a vertex u
 has a child, the apple moves to it (if there are several such vertices, the apple can move to any of them).
Otherwise, the apple falls from the tree.
It can be shown that after a finite time, both apples will fall from the tree.

Timofey has q
 assumptions in which vertices apples can grow. He assumes that apples can grow in vertices x
 and y
, and wants to know the number of pairs of vertices (a
, b
) from which apples can fall from the tree, where a
 — the vertex from which an apple from vertex x
 will fall, b
 — the vertex from which an apple from vertex y
 will fall. Help him do this.'''

def apple_tree(n, edges, queries):
    from collections import defaultdict

    # Build the tree as an adjacency list
    tree = defaultdict(list)
    for u, v in edges:
        tree[u].append(v)
        tree[v].append(u)

    # Function to find the leaves of the tree
    def find_leaves(node, parent):
        if len(tree[node]) == 1 and node != 1:  # Leaf node (not root)
            return [node]
        leaves = []
        for child in tree[node]:
            if child != parent:
                leaves.extend(find_leaves(child, node))
        return leaves

    # Find all leaves in the tree
    leaves = find_leaves(1, -1)

    results = []
    for x, y in queries:
        # Count how many leaves can be reached from x and y
        count_x = sum(1 for leaf in leaves if leaf == x or leaf in tree[x])
        count_y = sum(1 for leaf in leaves if leaf == y or leaf in tree[y])
        results.append(count_x * count_y)

    return results

if __name__ == "__main__":
    n = int(input())
    edges = [tuple(map(int, input().split())) for _ in range(n - 1)]
    q = int(input())
    queries = [tuple(map(int, input().split())) for _ in range(q)]
    results = apple_tree(n, edges, queries)
    for res in results:
        print(res)

