__author__ = 'spencertank'

from twilio.rest import TwilioRestClient


def makePhoneCall():
    account_sid = "ACc593f66f0b7dd76aefcc8dba0ad31361"
    auth_token  = "96aa5dffecbd672bfa957570da84d43b"
#    headline = getRedditHeadline()

    client = TwilioRestClient(account_sid, auth_token)
    server_url = "http://56640420.ngrok.com/"
#    call_url = server_url + headline
#    print call_url
    call = client.calls.create(to="+16095716251",  # Any phone number
        from_="2153757024", # Must be a valid Twilio number
        url=server_url)
    print call.sid


#whenToCall = datetime.datetime(2013,11,1,17,0)
#secondsTillCall = (whenToCall - datetime.datetime.utcnow()).total_seconds()
#Timer(secondsTillCall, makePhoneCall, ()).start()
makePhoneCall()