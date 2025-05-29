import speech_to_text as stt
from openai import OpenAI
import pyttsx3
# using this coz its free(for a limited use)
apikey = ""
with open('C:/Users/DELL/Desktop/api-keys/gpt.txt','r') as f:
   apikey= f.read()
def talk(sentence:str):
    try:
        client = OpenAI(api_key='')
        response = client.responses.create(
                model="gpt-4o-mini",
                input=sentence
                
            )
        return response.output_text
    except Exception:
        return 'Sorry can not talk now'


# i learned this from its website seems like something intresting
if(__name__=='__main__'):
    user=''
    while(not user=="bye"):
        # user=input("what you want to say to my chatbot(enter bye to quit):")
        
        engine = pyttsx3.init() 
        user=stt.listen().strip()
        if(user.lower().strip()!='what?'):
            print(user)
            bot=talk(user)
            engine.say(bot)           
            engine.runAndWait()  
            print(bot)



