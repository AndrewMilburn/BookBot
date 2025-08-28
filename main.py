from stats import *
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def print_report(book_path, word_count, chars_sorted):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for item in chars_sorted:
        if item['char'].isprintable():
            print(f"{item['char']}: {item['count']}")
        else:
            print(f"NPC has AXII value: {ord(item['char'])}: {item['count']}")
    print("============= BIGRAMS ===============")


            

def main():
    if len(sys.argv) > 1:
        path_to_file = sys.argv[1]
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
#    path_to_file = "books/frankenstein.txt"
    book = get_book_text(path_to_file)
    word_count = count_words(book)
    char_count = count_chars(book)
    chars_sorted = sort_chars(char_count)
#    print(f"{word_count} words found in the document")
#    print(f"Characters in Book: {char_count}")
    print_report(path_to_file, word_count, chars_sorted)
    print(count_bigrams(book.lower()))
#    count_bigrams_quickly(book.lower())


main()
