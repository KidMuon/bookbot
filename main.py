def main():
    book_path = "books/frankenstein.txt"
    with open(book_path) as f:
        file_contents = f.read()

    words = file_contents.split()
    number_words_in_book = len(words)

    letter_counts_in_book = count_letters(file_contents)

    print_report(book_path, number_words_in_book, letter_counts_in_book)


def count_letters(text):
    letter_counts = {}
    text = text.lower()
    for char in text:
        if char not in letter_counts and char.isalpha():
            letter_counts[char] = 1
        elif char.isalpha():
            letter_counts[char] += 1
    return sort_dict_by_value(letter_counts)


def sort_dict_by_value(dictionary):
    sorted_list = sorted(dictionary.items(), key=lambda x: x[1], reverse=True)
    return dict(sorted_list)


def print_report(book_path, word_count, letter_count):
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document")
    for letter in letter_count:
        print(f"The '{letter}' character was found {letter_count[letter]} times")
    print("--- End report ---")


if __name__ == "__main__":
    main()
