'''This prog. is to send a text message daily at 7PM about chennai trends in twitter'''
from twilio.rest import Client
import tweepy
import time
import json
import schedule

def job():
    auth = tweepy.OAuthHandler('**********','*********')#Enter your 'Consumer_key' and 'Consumer_secret'inplace of '******'
    auth.set_access_token('*******','******')#Enter your 'access_token' and 'access_token_secret'inplace of '******'

    api = tweepy.API(auth)     
    trends =  api.trends_place('23424848')
    trends_json = json.loads(json.dumps(trends,indent=4))
    txt = "Today's 6PM India trends:"
    count = 0
    for trend in trends_json[0]["trends"]:
        txt = txt + '\n' + trend["name"] 
        count += 1
        if count == 10: break        
    trends =  api.trends_place('2295424')  
    trends_json = json.loads(json.dumps(trends,indent=4))
    txt = txt+'\n\n\n'+"Today's 6PM Chennai trends:"
    count = 0
    for trend in trends_json[0]["trends"]:
        txt = txt + '\n' + trend["name"] 
        count += 1
        if count == 10: break

    #print(txt)

    account_sid = '******'#your Twilio accound_sid number
    auth_token = '*******'#your Twilio auth_token
    client = Client(account_sid, auth_token)
    message = client.messages \
                    .create(
                        body=txt,
                        from_='******',#your Twilio mobile number(given by Twilio website)
                        to='********'#your mobile number 
                        )

    print(message.sid)           

#schedule.every(10).seconds.do(job)
#schedule.every().hour.do(job)
schedule.every().day.at("18:00").do(job)
#schedule.every(5).to(10).seconds.do(job)
#schedule.every().monday.do(job)
#schedule.every().wednesday.at("13:15").do(job)
#schedule.every().minute.at(":17").do(job)
while True:
    schedule.run_pending()
    time.sleep(72000)

