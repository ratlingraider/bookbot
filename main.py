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
    print(f"{num_words} words found in the document")
    print(f"{num_letters} letters found in the document") 


def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_num_letters(text):
    all_freq = {}
    words = text.split()
    letters = ''.join(words)
    lower_letters = letters.lower()
    for i in lower_letters:
        if i in all_freq:
            all_freq[i] += 1
        else:
            all_freq[i] = 1
    return all_freq

main()