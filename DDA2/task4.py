from collections import Counter
import re
import random
import math

def download_file(url, local_path):
    response = requests.get(url)
    with open(local_path, 'wb') as file:
        file.write(response.content)

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
exact_counts = []
for _ in range(15):
    exact_count = exact_counter(dummy_file_path)
    exact_counts.append(exact_count)

# Task 2: Approximate Counter with Fixed Probability
fixed_probability = 1 / 2
approx_counts_fixed = []
for _ in range(15):
    approx_count_fixed = approximate_counter_fixed(dummy_file_path, fixed_probability)
    approx_counts_fixed.append(approx_count_fixed)

# Task 3: Approximate Counter with Decreasing Probability
approx_counts_decreasing = []
for _ in range(15):
    approx_count_decreasing = approximate_counter_decreasing(dummy_file_path)
    approx_counts_decreasing.append(approx_count_decreasing)

# Display results
# Display results
print("Task 1 - Exact Counter Results (Average):")
average_exact_count = Counter()
for count in exact_counts:
    average_exact_count += count
average_exact_count = Counter({word: count / 15 for word, count in average_exact_count.items()})  # Convert to Counter
print("Number of occurrences of words:", sum(average_exact_count.values()))
print("Average most common words:", average_exact_count.most_common(10))

# Display results
print("\nTask 2 - Approximate Counter with Fixed Probability Results (Average):")
average_approx_count_fixed = Counter()
for count in approx_counts_fixed:
    average_approx_count_fixed += count
average_approx_count_fixed = Counter({word: count / 15 for word, count in average_approx_count_fixed.items()})  # Convert to Counter
print("Number of occurrences of words:", sum(average_approx_count_fixed.values()))
print("Average most common words:", average_approx_count_fixed.most_common(10))


# Display results
print("\nTask 3 - Approximate Counter with Decreasing Probability Results (Average):")
average_approx_count_decreasing = Counter()
for count in approx_counts_decreasing:
    average_approx_count_decreasing += count
average_approx_count_decreasing = Counter({word: count / 15 for word, count in average_approx_count_decreasing.items()})  # Convert to Counter
print("Number of occurrences of words:", sum(average_approx_count_decreasing.values()))
print("Average most common words:", average_approx_count_decreasing.most_common(10))

