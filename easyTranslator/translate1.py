from translatepy.translators.google import GoogleTranslateV2

class Translate_event(GoogleTranslateV2):
    def __init__(self):
        super().__init__()
        self.translator=GoogleTranslateV2()

    def translate_to(self,data,destination_langue):
        trans = self.translator.translate(data, destination_language=destination_langue)
        return trans.result



# t=Translate_event()
# text=t.translate_to(data='你好',destination_langue='German')
# print(text)



