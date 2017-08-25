from neuron import Neuron


class Layer:
    def __init__(self, neurons=1, inputs=3):
        self.grid = []
        for i in range(neurons):
            neb = Neuron(inputs)
            neb.new_name(i)
            self.grid.append(neb)
