def capitalize_repeats(s):
    seen, repeats, result = set(), set(), []
    for char in s:
        repeats.add(char) if char in seen else seen.add(char)
    for char in s:
        result.append(char.upper() if char in repeats else char)
    print(f"Repeated letters: {', '.join(repeats) if repeats else 'None'}")
    return ''.join(result)
input_string = input("Enter a string: ")
print("Modified string:", capitalize_repeats(input_string))
