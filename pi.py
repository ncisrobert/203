import twitter, datetime, time
import serial

ser = serial.Serial('/dev/ttyACM0',9600)
tweet = ""
while True


    input = ser.readline().strip()
    
    file = open("twiterfile.txt")
    cred = file.readline().strip().split(',')

    api = twitter.Api(consumer_key=cred[0],consumer_secret=cred[1],access_token_key=cred[2],access_token_secret=cred[3])

    tweet = input
    
    post = tweet 

    reponse = api.PostUpdate( post )
    time.sleep(500)# 
