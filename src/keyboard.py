from src.item import Item



class MixinLang:

    __language = "EN"

    @property
    def language(self):
        return self.__language


    def change_lang(self):
        if self.language == "RU":
            self.__language = "EN"
        elif self.language == "EN":
            self.__language = "RU"
        return self


class Keyboard(Item, MixinLang):
    pass





