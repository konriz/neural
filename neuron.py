from random import uniform


class Neuron:
    def __init__(self, inputs=1, weights=None):
        self.name = 0
        self.inputs = 1
        self.weights = []
        self.configure(inputs, weights)

    def about(self):
        return [self.name, self.inputs, self.weights]

    def new_name(self, name):
        self.name = name
        return

    def configure(self, inputs, weights=None):
        self.inputs = inputs
        self.weights = self.weights_gen(weights)

    def weights_gen(self, weights=None):
        if weights is None:
            weights = []
            for i in range(self.inputs):
                weights.append(uniform(-0.1, 0.1))
        elif len(weights) != self.inputs:
            print "Error: Difference in inputs and weights amount; doing random!"
            self.weights_gen()
        else:
            return weights
        return weights

    def run(self, input_vector):
        if len(input_vector) == self.inputs:
            output = 0
            for i in range(self.inputs):
                output += input_vector[i] * self.weights[i]

            return output
        else:
            print 'Wrong input vector size!'
            return

# used for learning neuron to do specific things (supervised learning)
    def teach(self, inputs_matrix, outputs_matrix, eta=0.6):
        if len(inputs_matrix) != len(outputs_matrix):
            print 'Wrong amount of inputs or outputs!'
            return
        elif len(inputs_matrix[0]) != self.inputs:
            print 'Wrong amount of input variables!'
            return
        else:
            out = []
            for i in range(len(inputs_matrix)):
                input_vector = inputs_matrix[i]
                output_vector = outputs_matrix[i]
                value = self.run(input_vector)
                out.append(value)
                diff = output_vector - value
                for j in range(self.inputs):
                    self.weights[j] += eta * diff * input_vector[j]

            return out

# used for self-teaching of neuron to react to certain signal (unsupervised learning)
    def learn(self, inputs_matrix, eta=0.6):
        if len(inputs_matrix[0]) != self.inputs:
            print 'Wrong amount of input variables!'
            return
        else:
            out = []
            for i in range(len(inputs_matrix)):
                input_vector = inputs_matrix[i]
                value = self.run(input_vector)
                out.append(value)
                new_weights = []
                for j in range(self.inputs):
                    new_weight = self.weights[j] + eta * input_vector[j] * value
                    new_weights.append(new_weight)
                self.configure(self.inputs, new_weights)

        return out

    # used for self-teaching of neuron to react to certain signal (unsupervised learning)
    def learn_anti(self, inputs_matrix, eta=0.02):
        if len(inputs_matrix[0]) != self.inputs:
            print 'Wrong amount of input variables!'
            return
        else:
            out = []
            for i in range(len(inputs_matrix)):
                input_vector = inputs_matrix[i]
                value = self.run(input_vector)
                value_strength = 1
                if value <= 0:
                    value_strength = 0
                out.append(value)
                new_weights = []
                for j in range(self.inputs):
                    input_strength = 1
                    if input_vector[j] * self.weights[j] <= 0:
                        input_strength = 0
                    new_weight = self.weights[j] + eta * (2 * input_strength - 1) * (2 * value_strength - 1)
                    new_weights.append(new_weight)
                self.configure(self.inputs, new_weights)

        return out
