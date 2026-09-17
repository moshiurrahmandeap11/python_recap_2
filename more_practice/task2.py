# Task 2: Ekta function count_vowels(text) likho jeta ekta string nibe, loop diye check korbe koyta vowel (a,e,i,o,u) ache, count return korbe

def count_vowels(text):
    vowel_count = 0
    vowels = ["a", "e", "i", "o", "u"]

    for tex in text:
        if tex in vowels:
            vowel_count = vowel_count + 1
    return vowel_count

print("total vowels count :", count_vowels("moshiur"))