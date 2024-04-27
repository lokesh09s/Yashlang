import arrr
from pyscript import document

# import ctypes  # An included library with Python install.
# import os


from time import *

def translate_english(event):
    input_text = document.querySelector("#english")
    lang = input_text.value
    dict = {
        'a': 'д',
        'b': 'ю',
        'c': 'ж',
        'd': 'к',
        'e': 'т',
        'f': 'г',
        'g': 'в',
        'h': 'й',
        'i': 'ч',
        'j': 'щ',
        'k': 'л',
        'l': 'з',
        'm': 'ф',
        'n': 'ы',
        'o': 'п',
        'p': 'ш',
        'q': 'я',
        'r': 'р',
        's': 'с',
        't': 'е',
        'u': 'у',
        'v': 'б',
        'w': 'х',
        'x': 'н',
        'y': 'о',
        'z': 'м'
    }


    class Software():
        def __init__(self, text, encoder):
            self.lang = text
            self.dict = encoder
            self.encode = self.Encoder()
            self.decode = self.Decode()
            self.run = self.Check()

        def Check(self):
            a = self.lang.split()
            if a[0] == "/encode":
                a.remove("/encode")
                self.lang = " ".join(a)
                return self.Encoder()
            elif a[0] == "/decode":
                a.remove("/decode")
                self.lang = " ".join(a)
                return self.Decode()
            else:

                print("Prompt error")

        def Encoder(self):
            encode = []
            for i in self.lang:
                if i in self.dict.keys():
                    encode.append(self.dict[i])
                else:
                    encode.append(i)
            encode = "".join(encode)

            return encode

        def Decode(self):
            text = []
            for i in self.lang:
                if i in self.dict.values():
                    text.append(list(dict.keys())[list(dict.values()).index(i)])
                else:
                    text.append(i)
            decode = "".join(text)

            return decode


    result = Software(lang, dict)
    n = result.run
    output_div = document.querySelector("#output")
    output_div.innerText = n
