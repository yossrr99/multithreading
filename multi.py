import re
from collections import Counter
import threading
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
    global total_word_count
    total_word_count = len(words)

# Function to count occurrences of 'poste'
def count_poste(words):
    global poste_count
    word_counter = Counter(words)
    poste_count = word_counter.get('poste', 0)

# Function to find the longest word
def find_longest_word(words):
    global longest_word
    longest_word = max(words, key=len, default="")

# Function to analyze word frequencies
def word_frequencies(words):
    global frequencies
    frequencies = Counter(words)

# Function to count unique words
def count_unique_words(words):
    global unique_words
    unique_words = len(set(words))

# Function to calculate average word length
def average_word_length(words):
    global avg_word_length
    avg_word_length = sum(len(word) for word in words) / len(words) if words else 0

# Function to find top n longest words
def top_longest_words(words, n=10):
    global longest_words
    longest_words = sorted(set(words), key=len, reverse=True)[:n]

# Function to count words longer than a specific length
def count_long_words(words, min_length=10):
    global long_words_count
    long_words_count = sum(1 for word in words if len(word) > min_length)

# Function to find the most common starting letter of words
def most_common_starting_letter(words):
    global common_starting_letter
    starting_letters = [word[0] for word in words]
    common_starting_letter = Counter(starting_letters).most_common(1)[0] if starting_letters else ('N/A', 0)

# Function to calculate the percentage of words longer than a specific length
def percentage_long_words(words, min_length=10):
    global long_words_percentage
    total_words = len(words)
    long_words_count = sum(1 for word in words if len(word) > min_length)
    long_words_percentage = (long_words_count / total_words * 100) if total_words > 0 else 0

# Function to run multithreaded operations
def run_multithreaded(filename):
    start_time = time.time()  # Start timing

    text = read_file(filename)
    words, processed_text = process_text(text)

    # Create threads for each function
    thread_count_total = threading.Thread(target=count_total_words, args=(words,))
    thread_count_poste = threading.Thread(target=count_poste, args=(words,))
    thread_find_longest = threading.Thread(target=find_longest_word, args=(words,))
    thread_word_frequencies = threading.Thread(target=word_frequencies, args=(words,))
    thread_count_unique = threading.Thread(target=count_unique_words, args=(words,))
    thread_avg_word_length = threading.Thread(target=average_word_length, args=(words,))
    thread_longest_words = threading.Thread(target=top_longest_words, args=(words,))
    thread_long_words_count = threading.Thread(target=count_long_words, args=(words,))
    thread_common_starting_letter = threading.Thread(target=most_common_starting_letter, args=(words,))
    thread_percentage_long_words = threading.Thread(target=percentage_long_words, args=(words,))

    # Start threads
    thread_count_total.start()
    thread_count_poste.start()
    thread_find_longest.start()
    thread_word_frequencies.start()
    thread_count_unique.start()
    thread_avg_word_length.start()
    thread_longest_words.start()
    thread_long_words_count.start()
    thread_common_starting_letter.start()
    thread_percentage_long_words.start()

    # Wait for threads to finish
    thread_count_total.join()
    thread_count_poste.join()
    thread_find_longest.join()
    thread_word_frequencies.join()
    thread_count_unique.join()
    thread_avg_word_length.join()
    thread_longest_words.join()
    thread_long_words_count.join()
    thread_common_starting_letter.join()
    thread_percentage_long_words.join()

    end_time = time.time()  # End timing
    execution_time = end_time - start_time

    # Print results
    print(f"Multithreaded Execution Time: {execution_time:.3f} seconds")
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

# Run multithreaded
filename = 'exemple.txt'  # Replace with your file name
run_multithreaded(filename)
