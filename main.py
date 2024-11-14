def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    print(file_contents)

# Function to count the number of words in the file 
def count_words():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    return len(file_contents.split())

# Function to count the number of times each character appears in the file
def count_letters():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read().lower()  # Convert text to lowercase
    letter_count = {}
    for char in file_contents:
        if char.isalpha():  # Consider only alphabetic characters
            if char in letter_count:
                letter_count[char] += 1
            else:
                letter_count[char] = 1
    return letter_count

# Function to print a report of word and character counts
def print_report():
    word_count = count_words()
    letter_counts = count_letters()
    
    print(f"Number of words: {word_count}")
    print("Character counts:")
    for char, count in sorted(letter_counts.items()):
        print(f"{char}: {count}")

# Call the report function to print the data
print_report()