SUFFIX = ["lios", "etr", "initis", "liala", "etra", "inites"]

# Parts of speech
SUFFIX_ADJT = ["lios"  , "liala" ]
SUFFIX_NOUN = ["etr"   , "etra"  ]
SUFFIX_VERB = ["initis", "inites"]

# Gender
SUFFIX_MEN = ["lios" , "etr" , "initis"]
SUFFIX_WON = ["liala", "etra", "inites"]

# Group of suffixes
SUFFIX_PoS = [SUFFIX_ADJT, SUFFIX_NOUN, SUFFIX_VERB]
SUFFIX_GENDER = [SUFFIX_MEN, SUFFIX_WON]

def applyFilter(words, suffixes_group):
  result = list()
  for word in words:
    for (i, suffixes) in enumerate(suffixes_group):
      if any([word.endswith(suffix) for suffix in suffixes]):
        result.append(i)
  return result

# Valid language
def validL(words):
  return all([any([word.endswith(suffix) for suffix in SUFFIX]) for word in words])

# Valid gender
def validG(words):
  gender = applyFilter(words, SUFFIX_GENDER)
  return len(set(gender)) == 1

# Valid parts of speech
def validP(words):
  pos = applyFilter(words, SUFFIX_PoS)
  if len(pos) > 1 and pos.count(1) != 1: return False
  return all(pos[i] <= pos[i + 1] for i in range(len(pos) - 1))

if __name__ == '__main__':
  words = input().split()
  print('YES' if
    validL(words) and
    validG(words) and
    validP(words) else 'NO')
