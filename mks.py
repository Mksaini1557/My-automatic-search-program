
import webbrowser
import csv
import time
import random

generated_numbers = set()

def generate_unique_random_number():
    """
    Generate a single unique random number within the specified range.

    :return: A unique random number.
    :raises: ValueError if all possible numbers have been generated.
    """
    range_start = 1
    range_end = 200
    
    if len(generated_numbers) >= (range_end - range_start + 1):
        raise ValueError("All possible numbers have been generated.")
    
    while True:
        random_number = random.choice(range(range_start, range_end + 1))
        if random_number not in generated_numbers:
            generated_numbers.add(random_number)
            return random_number

# Function to read search strings from a CSV file
def read_search_strings(file_path, column_name):
    search_strings = []
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            search_strings.append(row[column_name])
    return search_strings

# Path to the CSV file containing search strings
file_path = 'mks.csv'
column_name = 'Trends'  # Replace with the actual column name in your CSV file

# Read search strings from the CSV file
search_strings = read_search_strings(file_path, column_name)

# Randomly shuffle the search strings to ensure randomness
random.shuffle(search_strings)

# Determine a random number of searches to perform
number_of_searches = random.randint(1, len(search_strings))

# Perform searches using the default browser
for i, search_string in enumerate(search_strings):
    if i >= number_of_searches:
        break
    search_string = search_string.replace(' ', '+')
    webbrowser.open("https://www.bing.com/search?q=" + search_string)
    # Add a delay of 5 to 10 seconds after each search
    time.sleep(random.randint(5, 10))
