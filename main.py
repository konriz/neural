from neuron import Neuron
from tools import signal_gen
from layer import Layer

layer = Layer(100, 3)
w0 = []
for neuron in layer.grid:
    w0.append(neuron.weights)
training_signal = signal_gen(10000)
layer.competitive_learning(training_signal)

for neuron in layer.grid:
#    neuron.learn_anti(training_signal)
    print "\nMy name is %s" % neuron.name
    learn_matrix = []
    for wei in range(len(neuron.weights)):
        learn_matrix.append(neuron.weights[wei] - w0[layer.grid.index(neuron)][wei])
    print "I've learned: %s" % learn_matrix
#    print "My weights are  %s " % neuron.weights
    run_vectors = [[0, 0, 0], [1, 0, 0], [0, 1, 0], [1, 1, 0], [0, 0, 1], [1, 0, 1], [0, 1, 1], [1, 1, 1]]
    reactions = []

    for vector in run_vectors:
        reactions.append(neuron.run(vector))

    min_max = [max(reactions), reactions.index(max(reactions)), min(reactions), reactions.index(min(reactions))]
#    print "My reactions are: %s" % reactions
#    print "My best reaction is: %s for vector %s" % (min_max[0], run_vectors[min_max[1]])
#    print "My worse reaction is: %s for vector %s" % (min_max[2], run_vectors[min_max[3]])
