def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    words = count_words(text)
    characters = count_characters(text)
    characters_sorted = sorted_dict(characters)
    print(characters_sorted)
    #output = report(book_path, words, characters)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    characters = {}
    words = text.split()
    for word in words:
        string = word.lower()
        for c in string:
            if c in characters:
                characters[c] += 1
            else:
                characters[c] = 1
    return characters

def sort_on(d):
    return d["num"]

def sorted_dict(dict):
    sorted_list = []
    print(dict)
    for c in dict:
        sorted_list.append({"char": c, "num": dict[c]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def report(path, words):
    print(f"--- Begin report of {path} ---")
    print(f"{words} words are found in the document")

main()
