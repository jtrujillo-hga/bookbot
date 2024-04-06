def run_report(file_contents):
    word_count = count_words(file_contents)
    char_count_dict = count_letters(file_contents)
    char_count_dict.sort(reverse=True, key=sort_on)

    print('--- Begin report of books/frankenstein.txt ---')
    print(f'{word_count} words found in the document')
    for x in char_count_dict:
        if x["char"].isalpha():
            print(f'The {x["char"]} character was found {x["count"]} times')

    print("--- End report ---")


def sort_on(dict):
    return dict["count"]


def count_letters(file_contents):
    tbr = {}
    for letter in file_contents:
        letter = letter.lower()
        if letter in tbr:
            tbr[letter] += 1
        else:
            tbr[letter] = 1
    tbr = [{"char": x, "count": y} for (x, y) in tbr.items()]
    return tbr


def count_words(file_contents):
    return len(file_contents.split())


def read_book(path):
    file_contents = ""
    with open("./books/frankenstein.text") as f:
        file_contents = f.read()
    return file_contents


def main():
    file_contents = read_book("./books/frankenstein.text")
    run_report(file_contents)


if __name__ == '__main__':
    main()
