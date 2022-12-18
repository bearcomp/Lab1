letters = "abcdefghijklmnopqrstuvwxyz"
shift = 3

def crypt(text):
  rez = ""
  for ch in text:
    rez += letters[(letters.find(ch)+shift)%len(letters)] if ch in letters else ch
  return rez
def decrypt(text):
  rez = ""
  for ch in text:
    rez += letters[(letters.find(ch)-shift)%len(letters)] if ch in letters else ch
  return rez

text = "hello world"
print(text)
print(crypt(text))
print(decrypt(crypt(text)))