def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = count_words(text)
    character_count = get_character_count(text)
    #print(text)
    #print(word_count)
    #print(character_count)
    character_count_list = get_letter_values(character_count) 
    value_based_character_count = flip_dictionary_pairs(character_count)
    print_report(character_count_list, value_based_character_count, word_count)



def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    individual_words = text.split()
    return len(individual_words)

def get_character_count(text):
    character_dictionary = {}
    for letter in text:
        key = letter.lower()
        character_dictionary[key] = character_dictionary.get(key, 0) + 1
    return character_dictionary

def print_report(sorted_numbers, character_dictionary, word_count):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document\n\n")
    for key in sorted_numbers:
        print(f"The '{character_dictionary[key]}' character was found {key} times\n")
    print("--- End report ---")

def flip_dictionary_pairs(character_dictionary):
    result = {}
    for key in character_dictionary:
        if (key.isalpha()):
            result[character_dictionary[key]] = key
    return result

def get_letter_values(character_dictionary):
    letter_values = []
    for key in character_dictionary:
        if (key.isalpha()):
            letter_values.append(character_dictionary[key])
    letter_values.sort(reverse=True)
    return letter_values
main()
