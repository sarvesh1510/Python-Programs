def main():
    user_string = input("Enter a string: ")
    
    vowels = 0
    consonants = 0
    blanks = 0
    
    for each_character in user_string.lower():
        if each_character in 'aeiou':
            vowels += 1
        elif each_character.isalpha():
            consonants += 1
        elif each_character == " ":
            blanks += 1
    
    print(f"Total number of Vowels in the user-entered string: {vowels}")
    print(f"Total number of Consonants in the user-entered string: {consonants}")
    print(f"Total number of Blanks in the user-entered string: {blanks}")

if __name__ == "__main__":
    main()

print("THIS PROGRAM IS WRITTEN BY SARVESH BHARDWAJ ERP :- 0221BCA062")