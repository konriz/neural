from neuron import Neuron
from tools import signal_gen
from layer import Layer

layer = Layer(30, 3)
training_signal = signal_gen(100)
for neuron in layer.grid:
    neuron.learn_anti(training_signal)
    print "\nMy name is %s" % neuron.name
#    print "My weights are  %s " % neuron.weights
    run_vectors = [[0, 0, 0], [1, 0, 0], [0, 1, 0], [1, 1, 0], [0, 0, 1], [1, 0, 1], [0, 1, 1], [1, 1, 1]]
    reactions = []
    index = 0
    max_reaction = -1
    max_index = -1
    min_reaction = 1
    min_index = -1
    for vector in run_vectors:
        reaction = neuron.run(vector)
        reactions.append(reaction)
        if reaction > max_reaction:
            max_reaction = reaction
            max_index = index
        if reaction < min_reaction:
            min_reaction = reaction
            min_index = index
        index += 1
#    print "My reactions are: %s" % reactions
    print "My best reaction is: %s for vector %s" % (max_reaction, run_vectors[max_index])
    print "My worse reaction is: %s for vector %s" % (min_reaction, run_vectors[min_index])
