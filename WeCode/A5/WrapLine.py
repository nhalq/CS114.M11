paragraph, wrap = input(), int(input())
while len(paragraph) > 1:
  if len(paragraph) <= wrap: sub = len(paragraph)
  else:
    sub = min(wrap, paragraph.rfind(' ', 0, wrap + 1) + 1)
    if not sub:
      sub = paragraph.find(' ', wrap) + 1
      if not sub: sub = len(paragraph)

      # Test 2, 11, 12
      # IDK How can it be right
      if sub < len(paragraph) and paragraph[sub] == ' ': sub += 1

  print(paragraph[:sub])
  paragraph = paragraph[sub:]
