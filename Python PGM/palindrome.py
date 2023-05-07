#palindrome
#tested under Python3
def process_text(text):
    text = text.lower()
    forbidden = (' ', '.', '?', '!', ':', ';', '-', '—', '(', ')', '[', ']', '’', '“', '”', '/', ',', '"')
    for i in forbidden:
        text = text.replace(i, '')
    return text

def reverse(text):
    return text[::-1]

def is_palindrome(text):
    new = process_text(text)
    return process_text(text) == reverse(process_text(text))

something = input('Enter text: ')
if (is_palindrome(something)):
    print("Yes, it is a palindrome")
else:
    print("No, it is not a palindrome")
