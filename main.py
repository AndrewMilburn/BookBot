def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    path_to_file = "books/frankenstein.txt"
    book = get_book_text(path_to_file)
    count = count_words(book)
    print(f"{count} words found in the document")

def count_words(text):
    words = len(text.split())
    return(words)

main()
