import Node

class Layer(object):
    """ 2D square array of Node objects.
    :param length: number of nodes along each side of the square layer
    """

    def __init__(self, length, name):
        self.length = length
        self.nodes = [[Node.Node() for i in range(0, length)] for j in range(0, length)]
        self.name = name