from src.item import Item


class MixinLanguage:
    def __init__(self, name: str, price: float, quantity: int, language: str = "EN") -> None:
        """Keyboard class Initialization """
        super().__init__(name, price, quantity)
        self.__language = language

    @property
    def language(self):
        """Returning Language"""
        return self.__language

    @language.setter
    def language(self, change_language):
        """Setting up  language"""
        if change_language in ["EN", "RU"]:
            self.__language = change_language
        else:
            raise AttributeError("property 'language' of 'KeyBoard' object has no setter!!!")

    def change_lang(self):
        """Changing language  to EN or RU"""
        if self.language == "EN":
            self.language = "RU"
            return self
        self.language = "EN"
        return self


class Keyboard(MixinLanguage, Item):
    pass
