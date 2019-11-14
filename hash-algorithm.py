word = input("Enter the message")
output = ""
res = ''
def rotate_letter(letter,n):
    if letter.isupper():
        start = ord('A')
    elif letter.islower():
        start = ord('a')
    else:
        return letter
    c = ord(letter)-start
    i=(c+n)%26 + start
    #output = chr(i)
    return chr(i)
def rotate_word(word,n,res):
    for letter in word:
        res += rotate_letter(letter,n)
    return res
print(res)
print(rotate_word(word,7,res))
#print(rotate_word('melon',-10))
def rotate_letter_get_back(letter,n):
    c = ord(letter)-ord('a')
    i=(c+n)%26 + ord('a')
    return chr(i)
def get_back(hash,n):
    message = ''
    for letter in hash:
        message += rotate_letter_get_back(letter,n)
    return message
print(get_back(res,19))
#print(get_back('cubed',36))
