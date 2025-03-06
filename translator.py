from googletrans import Translator

def translate_text(text, src_lang, dest_lang):
    translator = Translator()
    translation = translator.translate(text, src=src_lang, dest=dest_lang)
    return translation.text

if __name__ == "__main__":
    print("Simple Language Translator")
    text = input("Enter text to translate: ")
    src_lang = input("Enter source language (e.g., 'en' for English, 'fr' for French, 'auto' for auto-detection): ")
    dest_lang = input("Enter target language (e.g., 'es' for Spanish, 'de' for German): ")
    
    translated_text = translate_text(text, src_lang, dest_lang)
    print(f"Translated Text: {translated_text}")
