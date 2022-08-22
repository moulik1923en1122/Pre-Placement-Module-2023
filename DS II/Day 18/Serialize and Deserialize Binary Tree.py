class Codec:
    def __init__(self):
        self.builder = []

    def serialize(self, root):
        if root is None:
            return '#'
        self.traverse(root)
        return ''.join(self.builder)

    def traverse(self, root):
        if root is None:
            self.builder.append('#')
            self.builder.append(',')
            return
        self.builder.append(str(root.val))
        self.builder.append(',')
        self.traverse(root.left)
        self.traverse(root.right)

    def deserialize(self, data):
        if data is None:
            return None
        nodes = data.split(',')
        return self.buildTree(nodes)

    def buildTree(self, nodes):
        if len(nodes) == 0:
            return
        first = nodes.pop(0)
        if first == '#':
            return

        root = TreeNode(int(first))
        root.left = self.buildTree(nodes)
        root.right = self.buildTree(nodes)
        return root