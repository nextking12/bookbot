from stats import word_count


def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    
    # Print the number of words
    num_words = word_count(file_contents)
    print(f"{num_words} words found in the document")

main()
