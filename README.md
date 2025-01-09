# My-automatic-search-program

Got it! Here's a description tailored for a GitHub repository:

---

## Automated Web Search Program

This Python program automates web searches using random search strings from a CSV file. It performs the following tasks:

1. **Generate Unique Random Numbers**: The `generate_unique_random_number` function generates unique random numbers within a specified range (1 to 200). It ensures that no number is repeated until all possible numbers have been generated.

2. **Read Search Strings from CSV**: The `read_search_strings` function reads search strings from a specified column in a CSV file. The file path and column name are provided as inputs.

3. **Shuffle Search Strings**: The program randomly shuffles the search strings to ensure randomness in the search process.

4. **Determine Number of Searches**: A random number of searches to perform is determined based on the length of the search strings list.

5. **Perform Web Searches**: The program performs web searches using the default web browser. It opens a search URL for each search string, replacing spaces with '+' for proper URL formatting. A delay of 5 to 10 seconds is added between each search to avoid rapid consecutive searches.

### Usage

1. Ensure you have a CSV file with the search strings and the appropriate column name.
2. Update the `file_path` and `column_name` variables in the script with your CSV file path and column name.
3. Run the script to perform automated web searches.

---

Feel free to let me know if you need any further details or modifications!
