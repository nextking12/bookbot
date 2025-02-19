def word_count(text):
    words = text.split()
    return len(words)

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    
    # Print the number of words
    num_words = word_count(file_contents)
    print(f"\nNumber of words in the book: {num_words}")

main()