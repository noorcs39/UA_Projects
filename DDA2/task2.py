import requests
import re
from datasketch import HyperLogLog
import random
import time
from collections import Counter

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
    return Counter(words)

def approximate_counter_fixed_probability(words):
    hll = HyperLogLog()
    for word in words:
        hll.update(word.encode('utf-8'))
    return len(hll)

def approximate_counter_decreasing_probability(words):
    hll = HyperLogLog()
    for word in words:
        hll.update(word.encode('utf-8'))
    return len(hll)

def compare_counters(exact_counter_result, approximate_counter_result, top_n=20):
    exact_top_words = [word for word, _ in exact_counter_result.most_common(top_n)]
    approximate_top_words = [word for word, _ in approximate_counter_result.most_common(top_n)]

    common_words = set(exact_top_words) & set(approximate_top_words)

    absolute_errors = {word: abs(exact_counter_result[word] - approximate_counter_result[word]) for word in common_words}
    relative_errors = {word: absolute_errors[word] / max(exact_counter_result[word], 1) for word in common_words}

    print(f"\nComparison for the {top_n} most frequent words:")
    print(f"Common Words: {common_words}")
    print(f"Exact Counter Results: {exact_counter_result.most_common(top_n)}")
    print(f"Approximate Counter Results: {approximate_counter_result.most_common(top_n)}")
    print(f"Absolute Errors: {absolute_errors}")
    print(f"Relative Errors: {relative_errors}")

def test_counters(words):
    # Exact Counter
    exact_counter_result = exact_counter(words)

    # Approximate Counter with Fixed Probability
    approximate_counter_result_fixed = Counter()
    for word in words:
        approximate_counter_result_fixed[word] = approximate_counter_fixed_probability([word])

    # Approximate Counter with Decreasing Probability
    approximate_counter_result_decreasing = Counter()
    for word in words:
        approximate_counter_result_decreasing[word] = approximate_counter_decreasing_probability([word])

    # Compare Counters
    compare_counters(exact_counter_result, approximate_counter_result_fixed)
    compare_counters(exact_counter_result, approximate_counter_result_decreasing)

# Download the text file from Project Gutenberg
url = "https://www.gutenberg.org/cache/epub/72670/pg72670.txt"
text = download_text(url)

if text:
    # Preprocess the text
    words = preprocess_text(text)

    # Test the counters
    test_counters(words)
