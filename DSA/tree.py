class TreeNode:
    def __init__(self, data, children = []):
        self.data = data
        self.children = children

    def __str__(self, level=0):
        ret = "  " * level + str(self.data) + "\n"
        for child in self.children:
            ret += child.__str__(level + 1)
        return ret

    def addChild(self, TreeNode):
        self.children.append(TreeNode)


cola = TreeNode('Cola', [])
fanta = TreeNode('Fanta', [])
cold = TreeNode('Cold', [cola, fanta])


tea = TreeNode('tea', [])
coffee = TreeNode('coffee', [])
hot = TreeNode('hot', [tea, coffee])

tree = TreeNode('Drinks', [cold, hot])
print(tree)