import string

def ispangram(str1, alphabet=string.ascii_lowercase):
    str1=str1.replace(' ','').lower()
    chars = list(alphabet)
    for char in str1:
        if char in chars:
            print(char)
            chars.remove(char)
    print(chars)
    return len(chars)==0


print(ispangram("The quick brown fox jumps over the lazy dog"))