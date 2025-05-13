import sys
from stats import word_count, unique_char_count, sort_by_most

def getbooktext (book_path):
    with open(book_path) as f:
        book_content = f.read()
    return book_content

def filter_punctuation(char_list):
    filtered = []
    for char in char_list:
        if char["char"].isalpha():
            filtered.append(char)
    return filtered

def tidy(dict_list):
    tidy_list = []
    for dict in dict_list:
        tidy_list.append(f"{dict["char"]}: {dict["count"]}")
    return tidy_list

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count(getbooktext(book_path))} total words")
    print("--------- Character Count -------")
    for item in tidy(filter_punctuation(sort_by_most(unique_char_count(getbooktext(book_path))))):
        print(item)
    print("============= END ===============")

main()