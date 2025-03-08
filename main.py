from stats import count_words
from stats import count_chars
from stats import make_sorted_list

import sys


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    num_count = count_words(book_text)

    dict_of_chars = count_chars(book_text)

    sorted_list = make_sorted_list(dict_of_chars)

    # Format Report

    # Header
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")

    # Printing the number of words in the document
    print("----------- Word Count ----------")
    print(f"Found {num_count} total words")

    # iterating through the sorted list and printing the character count
    print("--------- Character Count -------")
    for item in sorted_list:
        char = item["char"]
        if char.isalpha():
            print(f"{char}: {item['count']}")

    print("============= END ===============")


main()
