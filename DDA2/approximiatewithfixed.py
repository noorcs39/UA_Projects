import re
import requests
import time
from collections import Counter
from bitarray import bitarray  # Install using: pip install bitarray
from prettytable import PrettyTable

def download_text_file(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        raise Exception(f"Failed to download the text file from {url}")

def count_words(text, stop_words=None):
    words = re.findall(r'\b\w+\b', text.lower())
    
    if stop_words:
        words = [word for word in words if word not in stop_words]
    
    word_counter = Counter(words)
    return word_counter

def approximate_counter(words, probability):
    # Implement Bloom Filter with fixed probability
    num_bits = len(words) * 2  # Adjust the size based on your dataset
    bloom_filter = bitarray(num_bits)
    bloom_filter.setall(0)

    for word in words:
        hash_value = hash(word)
        index1 = hash_value % num_bits
        index2 = (hash_value // num_bits) % num_bits

        bloom_filter[index1] = 1
        bloom_filter[index2] = 1

    return bloom_filter

def run_tests(text_content, num_tests, stop_words=None, display_top_n=10):
    execution_times = []
    word_counts = []

    for _ in range(num_tests):
        start_time = time.time()
        word_counter = count_words(text_content, stop_words=stop_words)
        end_time = time.time()

        execution_time = end_time - start_time
        execution_times.append(execution_time)

        word_counts.append(word_counter)

    average_time = sum(execution_times) / num_tests
    std_deviation = (sum((t - average_time) ** 2 for t in execution_times) / num_tests) ** 0.5

    table = PrettyTable()
    table.field_names = ["Test #", "Execution Time (s)"] + [f"Word {i+1}" for i in range(display_top_n)]

    for i in range(num_tests):
        row = [i+1, f"{execution_times[i]:.4f}"]
        most_common_words = word_counts[i].most_common(display_top_n)
        for word, count in most_common_words:
            row.append(f"{word}: {count}")
        table.add_row(row)

    print(table)
    print(f"Average Execution Time: {average_time:.4f} seconds")
    print(f"Standard Deviation: {std_deviation:.4f} seconds")
    
    return word_counts

def compare_counts(exact_counts, approximate_counts):
    # Extract the 20 most frequent words from exact counts
    exact_top_words = [word for count in exact_counts for word, _ in count.most_common(20)]

    # Extract the 20 most frequent words from approximate counts
    approximate_top_words = set()

    for count in approximate_counts:
        for word in exact_top_words:
            hash_value = hash(word)
            index1 = hash_value % len(count)
            index2 = (hash_value // len(count)) % len(count)

            if count[index1] == 1 and count[index2] == 1:
                approximate_top_words.add(word)

    # Compare the 20 most frequent words
    common_words = set(exact_top_words).intersection(approximate_top_words)

    print(f"\nCommon words in the 20 most frequent: {common_words}")

    # Calculate absolute and relative errors for the common words
    absolute_errors = []
    relative_errors = []

    for word in common_words:
        exact_total_count = sum(count[word] for count in exact_counts)
        approximate_total_count = word in approximate_top_words

        absolute_error = abs(exact_total_count - approximate_total_count)
        relative_error = absolute_error / exact_total_count if exact_total_count != 0 else 0

        absolute_errors.append(absolute_error)
        relative_errors.append(relative_error)

    print(f"\nAbsolute Errors: {absolute_errors}")
    print(f"Relative Errors: {relative_errors}")

    # Summary statistics
    print(f"\nSummary Statistics:")
    print(f"Minimum Absolute Error: {min(absolute_errors)}")
    print(f"Maximum Absolute Error: {max(absolute_errors)}")
    print(f"Average Absolute Error: {sum(absolute_errors) / len(absolute_errors)}")
    print(f"Minimum Relative Error: {min(relative_errors)}")
    print(f"Maximum Relative Error: {max(relative_errors)}")
    print(f"Average Relative Error: {sum(relative_errors) / len(relative_errors)}")


def main():
    text_file_url = "https://www.gutenberg.org/cache/epub/72699/pg72699.txt"
    text_content = download_text_file(text_file_url)
    num_tests = 5

    # Define common stop words (modify as needed)
    stop_words = set(['the', 'and', 'to', 'of', 'a', 'in', 'is', 'i', 'you', 'that'])

    # Run tests for exact counting
    exact_counts = run_tests(text_content, num_tests, stop_words=stop_words)

    # Run tests for approximate counting
    approximate_counts = [approximate_counter(re.findall(r'\b\w+\b', text_content.lower()), probability=0.5) for _ in range(num_tests)]

    # Compare the results
    compare_counts(exact_counts, approximate_counts)

if __name__ == "__main__":
    main()
