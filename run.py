from flask import Flask
from flask import render_template
from twilio.rest import TwilioRestClient
import twilio.twiml
from flask import request


app = Flask(__name__)

def makePhoneCall():
    account_sid = "ACc593f66f0b7dd76aefcc8dba0ad31361"
    auth_token  = "96aa5dffecbd672bfa957570da84d43b"
    client = TwilioRestClient(account_sid, auth_token)
    server_url = "https://341b598f.ngrok.com/"
    call = client.calls.create(to="+16095715366",  # Any phone number
        from_="2153757024", # Must be a valid Twilio number
        url=server_url)
    print call.sid


@app.route("/", methods=['GET', 'POST'])
@app.route("/<headline>", methods=['GET', 'POST'])
def hello(headline=None):
    return render_template('message.html', headline=headline)


@app.route("/monkey", methods=['GET', 'POST'])
def hello_monkey():
    """Respond to incoming calls with a simple text message."""
#    import pdb
#    pdb.set_trace()
    body = request.values['Body']
    print body
    resp = twilio.twiml.Response()
#    makePhoneCall()
    resp.message("You said, " + body)
    return str(resp)


if __name__ == "__main__":
    app.run(debug=True)
