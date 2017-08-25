from neuron import Neuron


class Layer:
    def __init__(self, neurons=1, inputs=3):
        self.grid = []
        for i in range(neurons):
            neb = Neuron(inputs)
            neb.new_name(i)
            self.grid.append(neb)

    def competitive_learning(self, learning_matrix):
        for i in range(len(learning_matrix)):
            learning_vector = learning_matrix[i]
            results = []
            for neuron in self.grid:
                results.append(neuron.run(learning_vector))
            max_index = results.index(max(results))
            best = self.grid[max_index]
            best.learn_anti([learning_vector])
        return
