
import requests
BITLY_TOKEN = "053b4d129486c2ebba389f9cba6e19a3fc8b6f70"


class BitlyHelper:
    def shorten_url(self, longurl):
        try:
            payload = {'access_token': BITLY_TOKEN , 'longUrl': longurl}
            response = requests.get('https://api-ssl.bitly.com/v3/shorten', 
                                    params=payload).json()
            if response['status_code'] == 200:
                return response['data']['url']    
        except Exception as e:
            print(e)
            return None
        
        
