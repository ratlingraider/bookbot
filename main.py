'''def main():
    with open("/Users/ratlingraider/workspace/github.com/ratlingraider/bookbot/books/frankenstein.txt") as f:
        file_contents = f.read()
        words = file_contents.split()
        count_of_words = len(words)
        print(count_of_words)

main()
'''
def main():
    book_path = "/Users/ratlingraider/workspace/github.com/ratlingraider/bookbot/books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_letters = get_num_letters(text)
    report_list = create_report(num_letters)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()

    for item in report_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")
def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_num_letters(text):
    all_freq = {}
    words = text.split()
    characters = ''.join(words)
    lower_characters = characters.lower()
    for i in lower_characters:
        if i in all_freq:
            all_freq[i] += 1
        else:
            all_freq[i] = 1
    return all_freq

def create_report(num_letters):
    report_list = []
    for letter in num_letters:
        report_list.append({"char": letter, "num": num_letters[letter]})
    report_list.sort(reverse=True, key=sort_on)
    return report_list

def sort_on(d):
    return d["num"]
main()