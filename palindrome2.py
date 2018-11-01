text = input('Type a sentence to verify if it is a palindrome: ')

def clean_text(text_we_want_to_clean):
    """ Given text, return the text with no spaces or punctuation and all lowercased."""

    # new_text = ""
    # # text = text.lower()
    # # text = text.replace(" ", "")
    # for char in text.lower():
    #     if char.isalpha():
    #         new_text = new_text + char
    # return new_text
    # print(new_text)

    new_text = ""
    text_we_want_to_clean = text_we_want_to_clean.lower()
    text_we_want_to_clean = text_we_want_to_clean.replace(" ", "")
    for char in text_we_want_to_clean:
        if char.isalpha():
            new_text = new_text + char
    print(new_text)
    return new_text

def no_numbers(words_only):
    for character in words_only:
        if character.isdigit():
            return False

    

def inner(new_text):
    """
    Do the first and last letters match? If yes, reassess the inner letters; do the first and last match? repeat.
    """
    if no_numbers(text) == False:
        print("Invalid Input.")
    

    new_text = clean_text(new_text)
    print(new_text)
    if len(new_text) == 0:
        return True
    elif new_text[0] != new_text[-1]:
        return False
    elif len(new_text)>1:
        inner(new_text[1:-1])
        return True


#now you have to call the functions....

if inner(text) == True:
    print(text + " is a palindrome.")
else:
    print(text + " is NOT a palindrome.")