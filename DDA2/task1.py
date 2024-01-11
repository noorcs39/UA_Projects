import requests
import re
from datasketch import HyperLogLog
import random
import time

def download_text(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        print(f"Failed to download the text file from {url}. Status Code: {response.status_code}")
        return None

def preprocess_text(text):
    # Remove non-alphabetic characters and convert to lowercase
    cleaned_text = re.sub(r'[^a-zA-Z\s]', '', text)
    return cleaned_text.lower().split()

def exact_counter(words):
    return {word: words.count(word) for word in set(words)}

def approximate_counter_fixed_probability(words):
    hll = HyperLogLog()
    for word in words:
        hll.update(word.encode('utf-8'))
    return len(hll)

def approximate_counter_decreasing_probability(words, iterations=5):
    estimates = []
    for _ in range(iterations):
        hll = HyperLogLog()
        for word in words:
            hll.update(word.encode('utf-8'))
        estimates.append(len(hll))
    return sum(estimates) / iterations

def test_counters(words, iterations=5):
    exact_counts = []
    fixed_prob_counts = []
    decreasing_prob_counts = []

    for _ in range(iterations):
        # Shuffle the words to have a different order in each iteration
        random.shuffle(words)

        # Exact Counter
        start_time = time.time()
        exact_counter(words)
        exact_time = time.time() - start_time
        exact_counts.append(exact_time)

        # Approximate Counter with Fixed Probability
        start_time = time.time()
        approximate_counter_fixed_probability(words)
        fixed_prob_time = time.time() - start_time
        fixed_prob_counts.append(fixed_prob_time)

        # Approximate Counter with Decreasing Probability
        start_time = time.time()
        approximate_counter_decreasing_probability(words)
        decreasing_prob_time = time.time() - start_time
        decreasing_prob_counts.append(decreasing_prob_time)

    print(f"Exact Counter Time (avg): {sum(exact_counts) / iterations}")
    print(f"Fixed Probability Counter Time (avg): {sum(fixed_prob_counts) / iterations}")
    print(f"Decreasing Probability Counter Time (avg): {sum(decreasing_prob_counts) / iterations}")

# Download the text file from Project Gutenberg
url = "https://www.gutenberg.org/cache/epub/72670/pg72670.txt"
text = download_text(url)

if text:
    # Preprocess the text
    words = preprocess_text(text)

    # Test the counters
    test_counters(words)
