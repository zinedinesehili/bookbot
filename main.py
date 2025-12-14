from stats import count_words, num_characters, sort_dictionary

def get_book_text(filepath):
    text = ""
    with open(filepath) as f:
        text = f.read()
    return text

def main():
    book_text = get_book_text("books/frankenstein.txt")
    word_count = count_words(book_text)
    character_count = num_characters(book_text)
    print(character_count)
    
    sorted_chars = sort_dictionary(character_count)
    
    print("============ BOOKBOT ============\n")
    print(f"Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    for char in sorted_chars:
        if char["char"].isalpha():
            print(f"{char["char"]}: {char["num"]}")

main()