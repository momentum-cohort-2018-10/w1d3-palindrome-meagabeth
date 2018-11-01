


def is_palindrome(text):
    """
    Based on user input, determines if a word, phrase, sentence, etc is a palindrome. A palindrome is read the same backwards and forwards.
    """

    # if text == "" or len(text) == 0 or text[0]==text[1]:
    #     print (text + " is a palindrome.")
# elif inner(text):
#     print (text + " is a palindrome.")
    # else:
    #     print (text + " is not a palindrome.")

# print(is_palindrome(text)) 

#     return False

def clean_text(text):
    """ Given text, return the text with no spaces or punctuation and all lowercased."""

    new_text = ""
    text = text.lower()
    text = text.replace(" ", "")
    for char in text:
        if char.isalpha():
            new_text = new_text + char
    return new_text


def inner(new_text):
    print(new_text)
    if len(new_text) == 0 or 1:
        return True
    elif new_text[0] != new_text[-1]:
        return False
    elif len(new_text) > 1:    
        inner(new_text[0:-1])
        return True
    # else:
    #     return False
# # print(text + "!")


text = input("Enter a word, phrase, sentence or multiple sentences to find out if it's a palindrome: ")
text = clean_text(text)
print(is_palindrome(inner(text)))



# inner(text)

# if (is_palindrome(text)):
#     print(text + "is a palindrome")
# else:
#     print("is not a palindrome")
# input_reverse = text[::-1]

   
