from deep_translator import MyMemoryTranslator

def english_to_french(englishText):
    """translates english to french"""
    french_text = MyMemoryTranslator(source='en', target='fr').translate(englishText)
    return french_text


def french_to_english(frenchText):
    """translates french to english"""
    english_text = MyMemoryTranslator(source='fr', target='en').translate(frenchText)
    return english_text
