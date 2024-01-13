from collections import Counter
import re
import random
import math

def exact_counter(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read().lower()
        words = re.findall(r'\b\w+\b', text)
        return Counter(words)

def approximate_counter_fixed(file_path, probability):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read().lower()
        words = re.findall(r'\b\w+\b', text)

        approx_count = Counter()
        for word in words:
            if random.random() < probability:
                approx_count[word] += 1

        return approx_count

def approximate_counter_decreasing(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read().lower()
        words = re.findall(r'\b\w+\b', text)

        approx_count = Counter()
        probability = 1.0
        for word in words:
            if random.random() < probability:
                approx_count[word] += 1
            probability /= math.sqrt(3)

        return approx_count

# Use the dummy file
dummy_file_path = '/home/noor/UA_Local_Proejcts/UA_Projects/DDA2/noor.txt'

# Task 1: Exact Counter
exact_count = exact_counter(dummy_file_path)
print("Task 1 - Exact Counter Results:")
print("Number of occurrences of words:", sum(exact_count.values()))
print("Most common words:", exact_count.most_common(10))

# Task 2: Approximate Counters
fixed_probability = 1 / 2
approx_count_fixed = approximate_counter_fixed(dummy_file_path, fixed_probability)
approx_count_decreasing = approximate_counter_decreasing(dummy_file_path)

print("\nTask 2 - Approximate Counter with Fixed Probability Results:")
print("Number of occurrences of words:", sum(approx_count_fixed.values()))
print("Most common words:", approx_count_fixed.most_common(10))

print("\nTask 2 - Approximate Counter with Decreasing Probability Results:")
print("Number of occurrences of words:", sum(approx_count_decreasing.values()))
print("Most common words:", approx_count_decreasing.most_common(10))
