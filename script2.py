letters = "abcdefghijklmnopqrstuvwxyz"
c_letters = "cbjtvmazlqdxyifopnwghuresk"

def crypt(text):
  rez = ""
  for ch in text:
    rez += c_letters[letters.find(ch)] if ch in letters else ch
  return rez
def decrypt(text):
  rez = ""
  for ch in text:
    rez += letters[c_letters.find(ch)] if ch in letters else ch
  return rez

text = "hello world"
print(text)
print(crypt(text))
print(decrypt(crypt(text)))