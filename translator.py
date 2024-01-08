from googletrans import Translator
# uses googletrans API as our translation tool

translator = Translator()

def eng_to_fr(arr):
    text = ''
    for word in arr:
        text = text + word + ' '

    translation = translator.translate(text, dest='fr')

    return translation


def fr_to_eng(arr):
    text = ''
    for word in arr:
        text = text + word + ' '

    translation = translator.translate(text, dest='en')

    return translation

