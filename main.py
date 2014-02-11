__author__ = 'spencertank'
import datetime
from bs4 import BeautifulSoup
import urllib2
import time
from threading import Timer
from twilio.rest import TwilioRestClient


def Soupify(url):
    response = urllib2.urlopen(url)
    source = response.read()
    soup = BeautifulSoup(source)
    return soup

def getRedditHeadline():
    url = "http://www.reddit.com/"
    soup = Soupify(url)
    siteTable = soup.find(id="siteTable")
    headerDiv = siteTable.div
    links = headerDiv.find_all('a')
    headline = ''
    for link in links:
        if 'class' in link.attrs.keys():
            if link['class'][0] == 'title':
                headline = link.text

    return sanitizeHeadline(headline)

def sanitizeHeadline(headline):
    headline = headline.replace('/', ' slash ')
    headline = headline.replace('(', 'open parenthesis ')
    headline = headline.replace(')', ' close parenthesis ')
    headline = headline.replace('"', ' double quote ')
    headline = headline.replace('\'', ' single quote ')
    headline = headline.replace('%', ' percent')
    headline = headline.replace('<', 'less than')
    headline = headline.replace('=', 'equals')
    headline = headline.replace('>', 'greater than')
    headline = headline.replace('@', ' at ')
    headline = headline.replace('?', ' question mark')
    headline = headline.replace(' ', '%20')
    return headline

def makePhoneCall():
    account_sid = "ACc593f66f0b7dd76aefcc8dba0ad31361"
    auth_token  = "96aa5dffecbd672bfa957570da84d43b"
    headline = getRedditHeadline()

    client = TwilioRestClient(account_sid, auth_token)
    server_url = "https://341b598f.ngrok.com/"
    call_url = server_url + headline
    print call_url
    call = client.calls.create(to="+16095715366",  # Any phone number
        from_="2153757024", # Must be a valid Twilio number
        url=call_url)
    print call.sid


whenToCall = datetime.datetime(2013,11,1,17,0)
secondsTillCall = (whenToCall - datetime.datetime.utcnow()).total_seconds()
#Timer(secondsTillCall, makePhoneCall, ()).start()
makePhoneCall()