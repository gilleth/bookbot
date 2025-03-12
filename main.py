import sys
from stats import get_words, count_chars, sort_chars

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def main():
    arguments = sys.argv
    if len(arguments) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        script_name = sys.argv[0]
        book_path = sys.argv[1]
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {book_path}...")
        print("----------- Word Count ----------")
        count = get_words(get_book_text(book_path))
        print(f"Found {count} total words")
        print("--------- Character Count -------")
        sorted_chars = sort_chars(count_chars(get_book_text(book_path)))
        for char_dict in sorted_chars:
            if char_dict["char"].isalpha():
                print(f"{char_dict['char']}: {char_dict['count']}")
        print("============= END ===============")
if __name__ == "__main__":
    main()

