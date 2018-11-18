from slugify import slugify

def prepare_words(file_name):
  print('preparing ', file_name)

  words = set()
  with open(file_name) as file:
    for word in file.readlines():
      word = word.split('/')[0]
      word = slugify(word)
      word = ''.join(word.split('-'))

      words.add(word)

  return set(words)

pt_words = prepare_words('../dictionaries/pt-BR/index.dic')
en_words = prepare_words('../dictionaries/en-US/index.dic')
es_words = prepare_words('../dictionaries/es/index.dic')

print('PT', len(pt_words))
print('EN', len(en_words))
print('ES', len(es_words))

universal_words = []

for word in en_words:
  if word in pt_words and word in es_words:
    universal_words.append(word)

print('UNIVERSAL', len(universal_words))

universal_words = sorted(universal_words)

with open('universal.dic','w+') as file:
  file.write('{}'.format(len(universal_words)))
  file.write('\n')

  for word in universal_words:
    file.write(word)
    file.write('\n')
