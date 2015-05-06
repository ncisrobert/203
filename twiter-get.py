import twitter, datetime, time
user = 3131272077
txtfile = open("data.txt", "w")

file = open("twiterfile.txt")
cred = file.readline().strip().split(',')


while  True :
    api = twitter.Api(consumer_key=cred[0],consumer_secret=cred[1],access_token_key=cred[2],access_token_secret=cred[3])

    statuses = api.GetUserTimeline(user)
    data = (statuses[0].text)
    if 'Good' in data:
        print("on ")
        txtfile.write("good")
        txtfile.close()
    elif "Ok" in data: 
        txtfile.write("ok")
        txtfile.close()
    elif "Bad" in data: 
        txtfile.write("bad")
        txtfile.close()
    elif "Death" in data: 
        txtfile.write("death")
        txtfile.close()
    elif "Dead" in data: 
        txtfile.write("dead")
        txtfile.close()     
    print("on a brake")
    time.sleep(900)


