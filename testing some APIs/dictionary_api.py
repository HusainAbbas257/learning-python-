import requests
def get_meaning(word:str):
    try:
        url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
        data = requests.get(url).json()
        return data[0]['meanings'][0]['definitions'][0]['definition']
    except Exception:
        return 'Sorry we cant help with that now!'
if(__name__=='__main__'):
    word=''
    while word!='end':
        word = input('enter a word(end to quit):')
        print(get_meaning(word))

    
