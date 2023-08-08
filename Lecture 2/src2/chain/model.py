from pomegranate import pomegranate

# Define starting probabilities
start = pomegranate.DiscreteDistribution({
    "sun": 0.5,
    "rain": 0.5
})

# Define transition model
transitions = pomegranate.ConditionalProbabilityTable([
    ["sun", "sun", 0.8],
    ["sun", "rain", 0.2],
    ["rain", "sun", 0.3],
    ["rain", "rain", 0.7]
], [start])

# Create Markov chain
model = pomegranate.MarkovChain([start, transitions])

# Sample 50 states from chain
print(model.sample(50))
