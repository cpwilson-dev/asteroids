import sys
from stats import get_book_text, get_word_count, get_character_count, sort_character_count

def print_report(file_path):

    text = get_book_text(file_path)
    word_count = get_word_count(text)
    character_count = get_character_count(text)
    sorted_count = sort_character_count(character_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    for char in sorted_count:
        if char.isalpha():
            print(f"{char}: {sorted_count[char]}")

    print("============= END ===============")

def main():

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file_path = sys.argv[1]
    print_report(file_path)


main()

