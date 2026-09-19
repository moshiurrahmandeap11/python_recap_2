# Task 14: Ekta function is_palindrome(text) likho jeta check korbe string ta palindrome kina (jemon "madam" ulta korleo "madam") — loop diye check koro, string slicing use na kore


def is_palindrome(text):
    reversed_text = ""

    for char in text:
        reversed_text = char + reversed_text
        print(reversed_text)

    if text == reversed_text:
        return True
    else:
        return False

print("Is 'moshiur' palindrome?:", is_palindrome("moshiur"))
print("Is 'madam' palindrome?:", is_palindrome("madam")) 