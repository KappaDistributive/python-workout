def hex_output() -> None:
    hex_string = input("Enter a hex number to convert: ")
    result = 0
    for index, character in enumerate(reversed(hex_string)):
        result += int(character, 16) * (16**index)
    print(result)
