# 2a3908c50f3048f189785032252805
import requests as r
def get_weather(location):
    try:
        url=f'http://api.weatherapi.com/v1/current.json?key=2a3908c50f3048f189785032252805&q={location}&aqi=no'
        res=r.get(url)
        js=res.json()
        raw_weather=js['current']
        weather=f'''
        At {raw_weather['last_updated']} updated last;\n
        current temperature in celcius:{raw_weather['temp_c']};\n
        current temperature in fahrenhiet:{raw_weather['temp_f']};\n
        current wind speed :{raw_weather['wind_kph']} km/hr in {raw_weather['wind_dir']} direction;\n
        and overall condition is :{raw_weather['condition']['text']};
        '''
        return weather
    except Exception as e:
        return 'error occured in get_weather():\t'+e

if(__name__=='__main__'):
    lo=input(('enter location:'))
    print(get_weather(lo))