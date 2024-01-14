#Nooruddin

import random

def n(v, a):
    return a * ((1 + 1 / a) ** v - 1)

def increment(v, a):
    delta = 1 / (n(v + 1, a) - n(v, a))

    if random.random() <= delta:
        return v + 1
    else:
        return v

def approximate_count(n_items, a):
    v = 0
    for i in range(n_items):
        v = increment(v, a)

    return n(v, a)

def test_approximate_count(n_trials, n_items, a, threshold):
    samples = [approximate_count(n_items, a) for i in range(n_trials)]

    avg = sum(samples) / n_trials

    if abs((avg - n_items) / n_items) < threshold:
        print("passed")
    else:
        print("failed")

print("[#]\nCounting Tests, 100 trials")

print("[#]\ntesting 1,000, a = 30, 10% error")
test_approximate_count(100, 1000, 30, 0.1)

print("[#]\ntesting 12,345, a = 10, 10% error")
test_approximate_count(100, 12345, 10, 0.1)

print("[#]\ntesting 222,222, a = 0.5, 20% error")
test_approximate_count(100, 222222, 0.5, 0.2)
