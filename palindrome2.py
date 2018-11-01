text = input('Type a sentence to verify if it is a palindrome: ')

def clean_text(text):
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
    text = text.lower()
    text = text.replace(" ", "")
    for char in text:
        if char.isalpha():
            new_text = new_text + char
    return new_text
    

def inner(new_text):
    """
    Do the first and last letters match? If yes, reassess the inner letters; do the first and last match? repeat.
    """
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