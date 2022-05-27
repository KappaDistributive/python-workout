def pig_latin(word: str) -> str:
    if not word:
        return ""
    if word[0] in "aeiou":
        return word + "way"
    return word[1:] + word[0] + "ay"


def pl_sentence(text: str) -> str:
    return " ".join(pig_latin(word) for word in text.split(" "))
