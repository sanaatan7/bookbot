
from stats import get_num_words, get_num_char, get_file_contents
import sys


def main():
    print("=========================== BOOKBOT ======================")
    print("Analyzing book found at books/frankenstein.txt...")
    if len(sys.argv) != 2 :
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)
    resource_path = sys.argv[1]

    print("---------------------------- Word Count ---------------------")
    contents = get_file_contents(resource_path)
    words = get_num_words(contents)
    print(f"Found {words} total words")

    print("------------------------ Character Count -----------------------")

    get_num_char(contents)



main()

print("============================== END ==============================")
