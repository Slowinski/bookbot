def main():
    book_path = "books/frankenstein.txt"
    text = get_book_path(book_path)
    #print(text)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words(text)} words found in the document")
    charnums = num_of_characters(text)
    char_num_print(charnums)


def get_book_path(path):
    with open(path) as f:
        return f.read()
    
def num_words(text):
    return len(text.split())

def num_of_characters(text):
    charnums = {}
    for char in text:
        low = char.lower()
        if low in charnums:
            charnums[low] += 1
        else:
            charnums[low] = 1
    return charnums
def char_num_print(charnums):
    for char, num in charnums.items():
        if char.isalpha():
            print(f"The '{char}' character was found {num} times")

main()