def resolve_palindrome(phrase):
    phrase = phrase.replace(" ", "").lower()
    for i in enumerate(phrase):
        if i[1] != phrase[len(phrase)-i[0]-1]:
            return False
        if (i[0] == len(phrase)/2):
            break
    return True


print("Ab b a: ", resolve_palindrome('Ab b a'))
print("Ab b b: ", resolve_palindrome("Ab b b"))
