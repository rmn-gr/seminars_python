import re


def is_there_rhythm(poem: str) -> bool:
    pattern = r'[уеыаоэяиюeuioa]'
    rhythm_status = True
    phrases = poem.split()
    syllable_count = len(re.findall(pattern, phrases[0]))
    for phrase in phrases[1:]:
        if syllable_count != len(re.findall(pattern, phrase)):
            rhythm_status = False
    return rhythm_status


poem = 'пара-ра-рам рам-пам-папам па-ра-па-да'
if is_there_rhythm(poem):
    print('Парам пам-пам')
else:
    print('Пам парам')