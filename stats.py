
def count_words(text):
    words = len(text.split())
    return(words)

def count_chars(text):
    chars_count = {}
    for char in text.lower():
        if char in chars_count:
            chars_count[char] += 1
        else:
            chars_count[char] = 1
    return chars_count

def sort_on(letters):
    return letters["count"]

def sort_chars(char_dict):
    characters = []
    for item in char_dict:
        characters.append({"char":item, "count":char_dict[item]})
    characters.sort(reverse=True, key=sort_on)
    return characters

def sort_bigs(letters):
    return letters["count"]

def count_bigrams(text):
    bigrams_count = {}
    for b in range(0, len(text)):
        if b + 1 <= len(text) - 1:
#            print(f"{b} / {len(text)}")
            if text[b] != " " and text[b+1] != " ":
                bigram = text[b:b+2]
                if bigram in bigrams_count:
                    bigrams_count[bigram] += 1
                else:
                    bigrams_count[bigram] = 1
#   Now sort
    bigs = []
    for letters in bigrams_count:
        bigs.append({"char":letters, "count":bigrams_count[letters]})
    bigs.sort(reverse=True, key=sort_bigs)
        
    return bigs

def count_bigrams_quickly(text):
    Counts = [[0 for x in range(128)] for y in range(128)]

# Perform the counting
    chars = 0
    R = ord(text[0])
    print(R)
    for i in range(1, len(text) - 1):
        chars += 1
        L = R
        R = ord(text[i+1])
#        print(L,R)
#        print(chars)
        if L<129 and R<129:
            Counts[L][R] += 1
#    print(Counts)
#    # Output the results
    print(Counts[1])
    for i in range(ord('!'), ord('~')):
#        if i < ord('[') or i >= ord('a'):
            for j in range(ord('!'), ord('~')):
                pass
#                if (j < ord('[') or j >= ord('a')) and Counts[i][j] > 0:
#                    print(chr(i) + chr(j), Counts[i][j], end=" ")   
