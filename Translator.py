def translator(phrase):
    translation = ""
    for letter in phrase:
        if letter in "aeiouAEIOU":
            if letter in "AEIOU":
                translation = translation + "F"
            else:
                translation = translation + "f"
        else:
            translation = translation + letter

    return translation


print(translator(input("Enter a phrase: ")))