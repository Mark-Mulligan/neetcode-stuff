class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)


class Tree:
    def __init__(self, root):
        self.root = root

    def dfs(self, node, visited=None):
        if visited is None:
            visited = []

        visited.append(node.value)
        for child in node.children:
            self.dfs(child, visited)

        return visited

    def bfs(self):
        visited = []
        queue = [self.root]

        while queue:
            node = queue.pop(0)
            visited.append(node.value)

            for child in node.children:
                queue.append(child)

        return visited


# Example Usage
root = TreeNode('root')
tree = Tree(root)
child1 = TreeNode('child1')
child2 = TreeNode('child2')
root.add_child(child1)
root.add_child(child2)
child1.add_child(TreeNode('child1_1'))
child1.add_child(TreeNode('child1_2'))
child2.add_child(TreeNode('child2_1'))

print("DFS:", tree.dfs(tree.root))
print("BFS:", tree.bfs())
