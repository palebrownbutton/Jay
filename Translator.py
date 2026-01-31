import asyncio
from googletrans import Translator

def translate(text, language):
    async def main():
        translator = Translator()
        translated = await translator.translate(text, dest=lang)
        print(translated.text)

    lang = None
    
    match language.lower():
        case "afrikaans":
            lang = "af"
        case "albanian":
            lang = "sq"
        case "amharic":
            lang = "am"
        case "arabic":
            lang = "ar"
        case "armenian":
            lang = "hy"
        case "azerbaijani":
            lang = "az"
        case "basque":
            lang = "eu"
        case "belarusian":
            lang = "be"
        case "bengali":
            lang = "bn"
        case "bosnian":
            lang = "bs"
        case "bulgarian":
            lang = "bg"
        case "catalan":
            lang = "ca"
        case "chinese":
            lang = "zh"
        case "corsican":
            lang = "co"
        case "croatian":
            lang = "hr"
        case "czech":
            lang = "cs"
        case "danish":
            lang = "da"
        case "dutch":
            lang = "nl"
        case "english":
            lang = "en"
        case "esperanto":
            lang = "eo"
        case "estonian":
            lang = "et"
        case "filipino":
            lang = "tl"
        case "finnish":
            lang = "fi"
        case "french":
            lang = "fr"
        case "galician":
            lang = "gl"
        case "georgian":
            lang = "ka"
        case "german":
            lang = "de"
        case "greek":
            lang = "el"
        case "gujarati":
            lang = "gu"
        case "haitian creole":
            lang = "ht"
        case "hebrew":
            lang = "iw"
        case "hindi":
            lang = "hi"
        case "hungarian":
            lang = "hu"
        case "icelandic":
            lang = "is"
        case "indonesian":
            lang = "id"
        case "irish":
            lang = "ga"
        case "italian":
            lang = "it"
        case "japanese":
            lang = "ja"
        case "javanese":
            lang = "jw"
        case "kannada":
            lang = "kn"
        case "kazakh":
            lang = "kk"
        case "khmer":
            lang = "km"
        case "korean":
            lang = "ko"
        case "kurdish":
            lang = "ku"
        case "kyrgyz":
            lang = "ky"
        case "lao":
            lang = "lo"
        case "latin":
            lang = "la"
        case "latvian":
            lang = "lv"
        case "lithuanian":
            lang = "lt"
        case "luxembourgish":
            lang = "lb"
        case "macedonian":
            lang = "mk"
        case "malagasy":
            lang = "mg"
        case "malay":
            lang = "ms"
        case "malayalam":
            lang = "ml"
        case "maltese":
            lang = "mt"
        case "maori":
            lang = "mi"
        case "marathi":
            lang = "mr"
        case "mongolian":
            lang = "mn"
        case "myanmar":
            lang = "my"
        case "nepali":
            lang = "ne"
        case "norwegian":
            lang = "no"
        case "pashto":
            lang = "ps"
        case "persian":
            lang = "fa"
        case "polish":
            lang = "pl"
        case "portuguese":
            lang = "pt"
        case "punjabi":
            lang = "pa"
        case "romanian":
            lang = "ro"
        case "russian":
            lang = "ru"
        case "samoan":
            lang = "sm"
        case "scots gaelic":
            lang = "gd"
        case "serbian":
            lang = "sr"
        case "sesotho":
            lang = "st"
        case "shona":
            lang = "sn"
        case "sindhi":
            lang = "sd"
        case "sinhala":
            lang = "si"
        case "slovak":
            lang = "sk"
        case "slovenian":
            lang = "sl"
        case "somali":
            lang = "so"
        case "spanish":
            lang = "es"
        case "sundanese":
            lang = "su"
        case "swahili":
            lang = "sw"
        case "swedish":
            lang = "sv"
        case "tajik":
            lang = "tg"
        case "tamil":
            lang = "ta"
        case "telugu":
            lang = "te"
        case "thai":
            lang = "th"
        case "turkish":
            lang = "tr"
        case "ukrainian":
            lang = "uk"
        case "urdu":
            lang = "ur"
        case "uzbek":
            lang = "uz"
        case "vietnamese":
            lang = "vi"
        case "welsh":
            lang = "cy"
        case "xhosa":
            lang = "xh"
        case "yiddish":
            lang = "yi"
        case "yoruba":
            lang = "yo"
        case "zulu":
            lang = "zu"
        case _:
            print("That language is not recognized.")
            return

    if lang:
        asyncio.run(main())