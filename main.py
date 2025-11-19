import sys
from stats import word_count
from stats import letter_count
from stats import sorted_list

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()

def main():
    inputs = sys.argv
    if len(inputs) !=2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    textfile = get_book_text(sys.argv[1])
    #print(textfile)
    print(f"Found {word_count(textfile)} total words")
    sort_list = sorted_list(letter_count(textfile))
    for pair in sort_list:
        if pair['char'].isalpha():
           print(f"{pair['char']}: {pair['num']}")
    

main()
