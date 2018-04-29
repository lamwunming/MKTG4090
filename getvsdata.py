
# coding: utf-8

# In[ ]:


from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import tweepy
import pandas as pd
import numpy as np
import thread
from multiprocessing.dummy import Pool as ThreadPool 


# In[ ]:


df = pd.read_csv('/Users/Lwmformula/Desktop/2017.csv')
tweetid = []
err = []
try:
    ori_tweet = df['ori_tweet'].tolist()
    another0 = []
    for i in ori_tweet:
        try:
            if np.isnan(i) == True: continue
            else: another0.append(i)
        except:
            another0.append(i)

    another1_ = df['conti'].tolist()
    another1 = []
    for i in another1_:
        try:
            if np.isnan(i) == True: continue
            else: another1.append(i)
        except:
            another1.append(i)

    another2_ = df['Unnamed: 2'].tolist()
    another2 = []
    for i in another2_:
        try:
            if np.isnan(i) == True: continue
            else: another2.append(i)
        except:
            another2.append(i)

    another3_ = df['Unnamed: 3'].tolist()
    another3 = []
    for i in another3_:
        try:
            if np.isnan(i) == True: continue
            else: anothe3.append(i)
        except:
            another3.append(i)

    another4_ = df['Unnamed: 4'].tolist()
    another4 = []
    for i in another4_:
        try:
            if np.isnan(i) == True: continue
            else: another4.append(i)
        except:
            another4.append(i)

    another5_ = df['Unnamed: 5'].tolist()
    another5 = []
    for i in another5_:
        try:
            if np.isnan(i) == True: continue
            else: another5.append(i)
        except:
            another5.append(i)


    another6_ = df['Unnamed: 6'].tolist()
    another6 = []
    for i in another6_:
        try:
            if np.isnan(i) == True: continue
            else: another6.append(i)
        except:
            another6.append(i)

    another7_ = df['Unnamed: 7'].tolist()
    another7 = []
    for i in another7_:
        try:
            if np.isnan(i) == True: continue
            else: another7.append(i)
        except:
            another7.append(i)

    another8_ = df['Unnamed: 8'].tolist()
    another8 = []
    for i in another8_:
        try:
            if np.isnan(i) == True: continue
            else: another8.append(i)
        except:
            another8.append(i)
except: pass


# In[ ]:


print len(tweetid)
for i in another3:
    if i.find('/status/') != -1 :
        tweetid.append(int(i.split('/status/')[-1]))
    else: continue
print len(tweetid)


# In[ ]:


import random
backup = tweetid
random.shuffle(tweetid)
err2 = []


# In[ ]:


import random
import string
import pickle
import os

err3 = []
access_token = "983268473169051648-9k8AR2f74kVoQTqlSI8NfmmqnTBSeEV"
access_token_secret = "g1QA5LiRETX3SgqpFRQ4d6HP7xfv47oTGAXBm7AOV1gsH"
consumer_key = "4WnAUjpDfHGq7xe1I1fJZfwft"
consumer_secret = "vXxE6fo818PcGf22QNuaSK7nZ7CLA4zWpPa7WoA0N4ON9QykHA"

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

def retrieve(goid):
    return api.get_status(goid).in_reply_to_status_id

def retext(goid):
    fuck = api.get_status(goid)
    sname = str(fuck.author._json[u'screen_name'])
    if sname == 'Aerie': return None
    else: return [sname,fuck.created_at.strftime("%Y-%m-%d"),str(fuck.text)]
    
def threadfunc(idpass):
    goid = idpass
    tmp = []
    try:
        while (True):
            if (retrieve(goid)):
                tmp.append(retrieve(goid))
                goid = retrieve(goid)
            else: 
                break
        for i in tmp:
            abc  = retext(i)
            ranstr = ''.join([random.choice(string.ascii_letters + string.digits) for n in xrange(32)])
            with open("/Users/Lwmformula/Desktop/2017/{}.pkl".format(ranstr),"wb") as f:
                pickle.dump(abc,f)
                    
    except:
        err2.append(idpass)
    
pool = ThreadPool(10) 
pool.map(lambda x: threadfunc(x), tweetid[0:200])
         #tweetid[0:])
         #err2[0:])
         #tweetid[2851:])
pool.close() 
pool.join()

filelist = os.listdir("/Users/Lwmformula/Desktop/2017")
numfile = len(filelist)
print numfile - 1


# In[ ]:


access_token = "983268473169051648-9k8AR2f74kVoQTqlSI8NfmmqnTBSeEV"
access_token_secret = "g1QA5LiRETX3SgqpFRQ4d6HP7xfv47oTGAXBm7AOV1gsH"
consumer_key = "4WnAUjpDfHGq7xe1I1fJZfwft"
consumer_secret = "vXxE6fo818PcGf22QNuaSK7nZ7CLA4zWpPa7WoA0N4ON9QykHA"

access_token = "983268473169051648-RxDmTqFNmKhrmWk6zJPhWeXCzO6yjQi"
access_token_secret = "IlPiOYbdHty9X6m1YNPLuxUL9Ttt7GWNvLxzXFuy4wU6k"
consumer_key = "CMurEKjVDhbEepic7ciTcN15C"
consumer_secret = "XfwUSjyEerPey1L3j8nD1wBaqvST5V8hJIzrr5SPaFi9YqwD1Q"

access_token = "983268473169051648-OYY1fGlJ5DgBFCwoSgl7f02sQLo1WIo"
access_token_secret = "sV8YXbsuX5vAzCD1uI1oYVyNtNgyjxPOJqPxbEintWdgj"
consumer_key = "3xUNIvYYIzJQS95T6LsQJmvzb"
consumer_secret = "Emyb2foB9qz8y4w8vfAQibBoaFAOJRsDKwRbqAvs3tnqilQiWo"

access_token = "983268473169051648-w6mZdZveRVw42PCsZdo5Wbt2bpSRXx8"
access_token_secret = "73JpFaQOd2T2HzvdFAThI3Vp5VzapVsOg9KqVU4mr5tf4"
consumer_key = "7K4rxxOLjYEvjahiJdeKL42C9"
consumer_secret = "E0XGcUWipcYCroP7uzk9kRkhcdNXKKHjMuHiCbq3D1veMpqXCS"

access_token = "983597575923154945-eGBjHeb35bWqrS8prYKYyM3IhnFGKNT"
access_token_secret = "MrviMBDsGHsQIA58JwmZh2p6Y0lEjVKxvtPTSemvjWu7w"
consumer_key = "QUmZt5A6Cv26rg4yDtK7ybOqu"
consumer_secret = "ZWhMj6pb24P8Tt0NDJPBiqhnh2m2XbvR6sZd03i8I5v5yURw9m"

access_token = "983597575923154945-mA466onXHQdDCWsUof7v7verAM7Ex0r"
access_token_secret = "ZgxE3rTGEV7VniKZKlusrFYVNijYQoTb9FKeYCTY1AOuG"
consumer_key = "IxYsfMBBba0yLvNRMy8C57Cx3"
consumer_secret = "XPShP3s3Ta1qy4DP0NyTc7S2FXk6fXOuHQtypMgQFJBp3bw6GG"

access_token = "983597575923154945-GU3gqbcWjULcZtBmNRENZTPhtIgUCLO"
access_token_secret = "BwOX0ShXpYUVye4vXBUdofQsogZvSSEYjtugTM2e3gkIn"
consumer_key = "ggROj2ooRKunAwjF0U9KC1YLl"
consumer_secret = "b5y7kBzkU5qvWB3W2mjX2RazpFEEdxHKonzCDvb58oD9eJdedh"

access_token = "983600113158307841-WZvDAmq3CL9iSdkT3jRBN1g0ZN7RPhZ"
access_token_secret = "4aJwSM8VrG4lVebHnrTmqXP0agCkW34b1jGu0U2Nd22Rd"
consumer_key = "v9Rl9csNAUsyHJCEkkzFXR1nr"
consumer_secret = "A5k1HrzvhR4pEPgK0B57luVA1YJDTjFqC6DTAE377K0lW7s0qL"

access_token = "983600113158307841-GsyOzLMIfBDcPKPnnd2Ycn7UQu0oHQ0"
access_token_secret = "MgAUKuq4vb6DQIu2fzNUJfhCso8nchjnZiwgbeIOdYmUb"
consumer_key = "os0psiXjnzU6CkOlHxtQDgwAZ"
consumer_secret = "WIiVqLl7CCNJquXZmYCMZeJCrLgF50L3zMHzELzPnSpOkjrGQ8"

access_token = "983600113158307841-vuv7a3j1pKemFCH8FW5Q3QIUpHvHg01"
access_token_secret = "fmQimKF0F3OiANuaeufSsT765rq8z2N87zP9YHhtVeR0p"
consumer_key = "tpj3BnKKkF1RfApaXD58BFldG"
consumer_secret = "77kjlZT8PnYEjn7i1hoHho628lvZSOYCPdXJUod2fnvDoYpeuH"

access_token = "983605577849819137-At38nKM3myaNlxJet1DtF7KpjI7nL3O"
access_token_secret = "ixHg6LJwH818ZxTllyPsPh56CcVsVtll4M01R3wbWM0Q6"
consumer_key = "d1n7zcFKUeoSQWl5MGSTO6S0d"
consumer_secret = "qBv3iyogDGtyNG2UgKL4TEcbxMIPY9xdR9GuVnEGNMnJtzD8kt"

access_token = "983605577849819137-tFIPfijkNEeElwZfGeoDzi7yyP7Fy6M"
access_token_secret = "3DxDBXS5gaXuoiLcQlC2joVLCYsVbBzPX7u4onWrKEJH9"
consumer_key = "fcnZorYEwgMBFhi8htNxogV1X"
consumer_secret = "Ra9u83L9rzOQlvl1B0Gj4EyRAdkxJYeogjtyu3PzMIKNj0cZfZ"

access_token = "983605577849819137-PtySGG8jYlsL74mQwDKkhBJv3xkcglm"
access_token_secret = "nPVGTyOKJqoGtz2GRxH2MvfiiIvq9HmCOANGzNaLDIjIn"
consumer_key = "nrqX4lsIML7KY1ntLWzSI7AmT"
consumer_secret = "oXsMMxR4NtM5us4TZGYnahq8wlOwdLGrXMkywfdMZQALDGSpLL"


# In[ ]:


textncreate = []
filelist = os.listdir("/Users/Lwmformula/Desktop/2017")
filelist_ = [i for i in filelist if i != '.DS_Store']
for i in filelist_:
    with open("/Users/Lwmformula/Desktop/2017/{}".format(i),"rb") as f:
        textncreate.append(pickle.load(f))
print len(textncreate)
text_create = [i for i in textncreate if i != None]
with open('/Users/Lwmformula/Desktop/2017.pkl', 'wb') as f:
    pickle.dump(text_create, f)
print len(text_create)


# In[ ]:


_sname_ = [i[0] for i in text_create]
_create_ = [i[1] for i in text_create]
_comments_ = [i[2] for i in text_create]
savedf = pd.DataFrame()
savedf['screen_name'] = _sname_
savedf['created_at'] = _create_
savedf['comment'] = _comments_
savedf.to_csv('/Users/Lwmformula/Desktop/2017_.csv')


# In[ ]:


print len(err2[-450:-301])
text_create = [i for i in textncreate if i != None]
print len(text_create)


# In[ ]:


access_token = "983268473169051648-9k8AR2f74kVoQTqlSI8NfmmqnTBSeEV"
access_token_secret = "g1QA5LiRETX3SgqpFRQ4d6HP7xfv47oTGAXBm7AOV1gsH"
consumer_key = "4WnAUjpDfHGq7xe1I1fJZfwft"
consumer_secret = "vXxE6fo818PcGf22QNuaSK7nZ7CLA4zWpPa7WoA0N4ON9QykHA"

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

print api.get_status(tweetid[0])

