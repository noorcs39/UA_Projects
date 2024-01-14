import re
import requests
from collections import Counter
import time
from prettytable import PrettyTable

# Function to download the text file
def download_text_file(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        raise Exception(f"Failed to download the text file from {url}")

# Function to count words, excluding stop-words
def count_words(text, stop_words):
    words = re.findall(r'\b\w+\b', text.lower())
    
    # Exclude stop-words
    filtered_words = [word for word in words if word not in stop_words]
    
    word_counter = Counter(filtered_words)
    return word_counter

# Function to run tests and display results
def run_tests(text_content, stop_words, num_tests, display_top_n=10):
    execution_times = []
    word_counts = []

    for _ in range(num_tests):
        start_time = time.time()
        word_counter = count_words(text_content, stop_words)
        end_time = time.time()

        execution_time = end_time - start_time
        execution_times.append(execution_time)

        most_common_words = word_counter.most_common(display_top_n)
        word_counts.append({word: count for word, count in most_common_words})

    average_time = sum(execution_times) / num_tests
    std_deviation = (sum((t - average_time) ** 2 for t in execution_times) / num_tests) ** 0.5

    table = PrettyTable()
    table.field_names = ["Test #", "Execution Time (s)"] + [f"Word {i+1}" for i in range(display_top_n)]

    for i in range(num_tests):
        row = [i+1, f"{execution_times[i]:.4f}"]
        for word, count in word_counts[i].items():
            row.append(f"{word}: {count}")
        table.add_row(row)

    print(table)
    print(f"Average Execution Time: {average_time:.4f} seconds")
    print(f"Standard Deviation: {std_deviation:.4f} seconds")
    print()

def main():
    text_file_url = "https://www.gutenberg.org/cache/epub/72699/pg72699.txt"
    text_content = download_text_file(text_file_url)
    
    # List of common stop-words to be excluded
    stop_words = ["the", "and", "in", "of", "to", "a", "is", "it", "that", "was"]

    num_tests = 5
    run_tests(text_content, stop_words, num_tests)

if __name__ == "__main__":
    main()
