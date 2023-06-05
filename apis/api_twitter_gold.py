from bottle import post
import requests

@post("/api-send-sms")

def _():
    try:

        user_api_key = "bbace6224d4f4bf69103bdd226c78210"
        sms_message = "Hello world"
        sms_to_phone = "71819940"

        payload = {'user_api_key': user_api_key,
                    'sms_message': sms_message,
                    'sms_to_phone':sms_to_phone}

        res = requests.get('127.0.0.1:4444/', data=payload)
        print(res)
        print(res.text)
        return "ok"
    except Exception as e:
        print(e)
        return {"info":str(e)}
    finally:
        pass