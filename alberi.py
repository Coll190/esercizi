class tree:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = tree(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = tree(value)
            else:
                self.right.insert(value)

num = tree(10)
num.insert(9)
num.insert(3)
num.insert(20)
num.insert(7)
num.insert(6)
num.insert(100)
num.insert(50)
num.insert(1)

print(num.left.left.left.value)
