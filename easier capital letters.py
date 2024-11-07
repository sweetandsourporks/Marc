def capitalize_repeats(s):
    seen_letters = set()   
    repeated_letters = set()

    for letter in s:
        if letter in seen_letters:
            repeated_letters.add(letter)

        else:
            seen_letters.add(letter)

    result=""
    for letter in s:
            result += letter.upper() if letter in repeated_letters else letter

    print ("repeated letters:", ", ".join(repeated_letters) if repeated_letters else "none")

    return result
input_string = input("enter a string: ")
print("modified string", capitalize_repeats(input_string))
