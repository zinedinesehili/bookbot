from stats import count_words

def get_book_text(filepath):
    text = ""
    with open(filepath) as f:
        text = f.read()
    return text

def main():
    book_text = get_book_text("books/frankenstein.txt")
    count_words(book_text)

main()