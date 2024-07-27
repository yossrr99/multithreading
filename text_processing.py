import re
from collections import Counter
import time

# Function to read the text file
def read_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read()

# Function to process text
def process_text(text):
    # Remove punctuation and convert to lowercase
    text = re.sub(r'[^\w\s]', '', text).lower()
    return text.split(), text

# Function to count total words
def count_total_words(words):
    return len(words)

# Function to count occurrences of 'poste'
def count_poste(words):
    word_counter = Counter(words)
    return word_counter.get('poste', 0)

# Function to find the longest word
def find_longest_word(words):
    return max(words, key=len, default="")

# Function to analyze word frequencies
def word_frequencies(words):
    return Counter(words)

# Function to count unique words
def count_unique_words(words):
    return len(set(words))

# Function to calculate average word length
def average_word_length(words):
    return sum(len(word) for word in words) / len(words) if words else 0

# Function to find top n longest words
def top_longest_words(words, n=10):
    return sorted(set(words), key=len, reverse=True)[:n]

# Function to count words longer than a specific length
def count_long_words(words, min_length=10):
    return sum(1 for word in words if len(word) > min_length)

# Function to find the most common starting letter of words
def most_common_starting_letter(words):
    starting_letters = [word[0] for word in words]
    time.sleep(0.01)
    return Counter(starting_letters).most_common(1)[0] if starting_letters else ('N/A', 0)

# Function to calculate the percentage of words longer than a specific length
def percentage_long_words(words, min_length=10):
    total_words = len(words)
    long_words_count = count_long_words(words, min_length)
    return (long_words_count / total_words * 100) if total_words > 0 else 0


    


# Function to run single-threaded operations
def run_single_threaded(filename):
    start_time = time.time()  # Start timing

    text = read_file(filename)
    words, processed_text = process_text(text)
    
    total_word_count = count_total_words(words)
    poste_count = count_poste(words)
    longest_word = find_longest_word(words)
    frequencies = word_frequencies(words)
    unique_words = count_unique_words(words)
    avg_word_length = average_word_length(words)
    longest_words = top_longest_words(words)
    long_words_count = count_long_words(words)
    common_starting_letter = most_common_starting_letter(words)
    long_words_percentage = percentage_long_words(words)

    end_time = time.time()  # End timing
    execution_time = end_time - start_time

    print(f"Single-Threaded Execution Time: {execution_time:.3f} seconds")
    print(f"Total Word Count: {total_word_count}")
    print(f"Occurrences of 'poste': {poste_count}")
    print(f"Longest Word: {longest_word}")
    print(f"Top 10 Word Frequencies: {frequencies.most_common(10)}")
    print(f"Unique Words Count: {unique_words}")
    print(f"Average Word Length: {avg_word_length:.2f}")
    print(f"Top 10 Longest Words: {', '.join(longest_words)}")
    print(f"Count of Words Longer Than 10 Characters: {long_words_count}")
    print(f"Most Common Starting Letter: {common_starting_letter[0]} (Count: {common_starting_letter[1]})")
    print(f"Percentage of Words Longer Than 10 Characters: {long_words_percentage:.2f}%")

# Run single-threaded
filename = 'exemple.txt'  # Replace with your file name
run_single_threaded(filename)
