class Value:
    """
    Wraps a Number as a node in a computation graph.
    
    This allows us to do backpropogation, meaning we compute local derivatives,
    and recurse backwards through the graph applying the chain rule, and then
    use that global derivatives to nudge the input weights to minimize the
    final loss function.
    """

    def __init__(self):
        pass

    def __add__(self,b):
        pass
    
    def __mul__():
        pass
    
    def __repr__(self):
        pass

class Neuron:
    """
    A simplified mathematical model of a neuron where initialize with input
    weights and an activation function and get back a Neuron that accepts data
    and gives output.
    """

class MultiLayerPerception:
    """A simple neural network: a directed graph of Neurons"""

