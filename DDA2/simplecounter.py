import requests
import re
from collections import Counter
import matplotlib.pyplot as plt
import time

def download_text_file(url):
    response = requests.get(url)
    return response.text

def tokenize(text):
    words = re.findall(r'\b\w+\b', text.lower())
    return words

def count_words(text):
    tokenized_words = tokenize(text)
    return Counter(tokenized_words)

def identify_most_common_words(word_counts, n=10):
    return word_counts.most_common(n)

def perform_tests(text, repetitions=5):
    start_time = time.time()

    for _ in range(repetitions):
        word_counts = count_words(text)

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Time taken for tests: {elapsed_time} seconds")

    return word_counts, elapsed_time

def plot_bar_graph(word_counts, elapsed_time, n=10):
    common_words = dict(identify_most_common_words(word_counts, n))
    plt.bar(common_words.keys(), common_words.values())
    plt.xlabel('Words')
    plt.ylabel('Frequency')
    plt.title('Top Words in the Text\nTime taken for tests: {:.4f} seconds'.format(elapsed_time))
    plt.show()

def main():
    url = "https://www.gutenberg.org/cache/epub/72703/pg72703.txt"
    text_content = download_text_file(url)

    word_counts, elapsed_time = perform_tests(text_content)

    most_common_words = identify_most_common_words(word_counts)

    print("Most Common Words:")
    for word, count in most_common_words:
        print(f"{word}: {count}")

    # Plot the bar graph
    plot_bar_graph(word_counts, elapsed_time)

if __name__ == "__main__":
    main()
