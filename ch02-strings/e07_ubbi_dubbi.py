def ubbi_dubbi(word: str) -> str:
  parts = []
  for character in word:
    if character in "aeiou":
      parts.append("ub")
    parts.append(character)
  return "".join(parts)
