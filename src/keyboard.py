from src.item import Item



class MixinLang:

    def __init__(self):
        super().__init__()
        self.__language = "EN"

    @property
    def language(self):
        return self.__language

    @language.setter
    def language(self, lang):
        if lang == "RU" or lang == "EN":
            self.__language = lang
        else:
            raise AttributeError ("property 'language' of 'KeyBoard' object has no setter")

    def change_lang(self):
        if self.language == "RU":
            self.language = "EN"
        elif self.language == "EN":
            self.language = "RU"
        return self




class Keyboard(Item, MixinLang):
    pass





