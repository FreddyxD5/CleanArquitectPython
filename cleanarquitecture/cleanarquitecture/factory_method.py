class French:
    def __init__(self) -> None:
        self.translations = {'car':'voiture', 'bike':'bicyclette', 'cycle':'cyclette'}
    
    def localize(self, msg):
        return self.translations[msg]
        
class Spanish:
    def __init__(self) -> None:
        self.translations = {'car':'Carro', 'bike':'Bicicleta', 'cycle':'Motocicleta'}
    
    def localize(self, msg):
        return self.translations[msg]
        
class English:
    def __init__(self) -> None:
        self.translations = {'car':'car', 'bike':'bike', 'cycle':'cycle'}
    
    def localize(self, msg):
        return self.translations[msg]
    

# class Factory:
#     def __init__(self, language="English"):
#         self.idioma = language

#     def factory_method(self, language):   
#         print(*args)     
#         idioma = language.lower()
#         languages = {
#             "french":French(),
#             "spanish":Spanish(),
#             "english":English()
#         }
        
#         return languages[idioma]
    
def Factory(language="English"):
    available_languages = {
        "French":French(),
        "Spanish":Spanish(),
        "English":English()
    }
    return available_languages[language]

if __name__ == '__main__':
    list_items = ['car','bike','cycle']
    fren = Factory("French")
    esp = Factory("Spanish")
    eng = Factory("English")
    print('-----------------------------------')
    for x in list_items:
        print(fren.localize(x))
    print('-----------------------------------')
    for y in list_items:
        print(esp.localize(y))
    print('-----------------------------------')
    for e in list_items:
        print(eng.localize(e))
    print('-----------------------------------')
