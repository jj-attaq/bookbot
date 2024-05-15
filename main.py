def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = count_words(text)
    chars_dict = count_letters(text)
    chars_list = convert_to_list(chars_dict)

    chars_list.sort(reverse=True, key=sort_on)
    display(book_path, word_count, chars_list)


def get_book_text(path):
    with open(path) as f:
        return f.read()


def count_words(text):
    words = text.split()
    return len(words)


def count_letters(text):
    char_dict = {}
    for c in text:
        char = c.lower()
        if char not in char_dict:
            char_dict[char] = 1
        else:
            char_dict[char] += 1
    return char_dict


def convert_to_list(dict):
    list = []
    for el in dict:
        list.append({"char": el, "num": dict[el]})
    return list


def sort_on(dict):
    return dict["num"]


def display(file, words, dict_list):
    print(f"--- Begin report of {file} ---")
    print(f"{words} found in the document")
    print("")
    for el in dict_list:
        if not el["char"].isalpha():
            continue
        print(f"The {el["char"]} character was found {el["num"]} times")
    print("--- End report ---")


main()
