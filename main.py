def main ():
    book_path = "books/frankenstein.txt"
    book_text = grab_book_text(book_path)
    num_of_words = get_word_count(book_text)
    char_count = get_chars_count(book_text)
    print_book_report(num_of_words, char_count, book_path)


def print_book_report(num_of_words, char_count, book_path):
    # collection of character count (dictionary) and word count (number of occurences) featured in the text
    char_sorted_list = convert_char_count_to_list(char_count)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_of_words} words found in document\n")
    for char_count in char_sorted_list:
        if char_count["char"].isalpha():
            print(f"The '{char_count["char"]}' character was found {char_count["num"]} times")
    print("--- End report ---")


def convert_char_count_to_list(char_count):
    # returns a sorted list of a char (key) and number of occurence from char dicitonary(value)
    char_sort_list = []

    for char in char_count:
        char_sort_list.append(
                {"char": char, "num": char_count[char]}
                )
        
    char_sort_list.sort(reverse=True, key=sort_on)
    return char_sort_list

def sort_on(dict):
    # gets the dictionary and returns the value of the "num" key
    return dict["num"]


def get_chars_count(text):
    # returns the count of each character in the text and the number of occurences in a dictionary
    char_dict = {}

    for char in text:
        lower_case_char = char.lower()
        if lower_case_char in char_dict:
            char_dict[lower_case_char] += 1
        else:
            char_dict[lower_case_char] = 1
    return char_dict

def get_word_count(text):
    # returns the number of words in the text
    return len(text.split())

def grab_book_text(path):
    # reads the file and returns the text as a string
    with open(path) as f:
        return f.read()

main()