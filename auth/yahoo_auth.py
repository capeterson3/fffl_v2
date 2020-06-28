from yahoo_oauth import OAuth2
import json

# Yahoo Keys
with open("./auth/oauth2yahoo.json") as json_yahoo_file:
    auths = json.load(json_yahoo_file)
yahoo_consumer_key = auths["consumer_key"]
yahoo_consumer_secret = auths["consumer_secret"]
yahoo_access_key = auths["access_token"]
json_yahoo_file.close()


class Yahoo_Api:
    def __init__(self, consumer_key, consumer_secret, access_key):
        self._consumer_key = consumer_key
        self._consumer_secret = consumer_secret
        self._access_key = access_key
        self._authorization = None

    def _login(self):
        global oauth
        oauth = OAuth2(None, None, from_file="./auth/oauth2yahoo.json")
        if not oauth.token_is_valid():
            oauth.refresh_access_token()


class Authorize:
    def AuthorizeLeague(self):
        # UPDATE LEAGUE GAME ID
        yahoo_api._login()
        url = "https://fantasysports.yahooapis.com/fantasy/v2/league/380.l.258645/transactions"
        response = oauth.session.get(url, params={"format": "json"})
        r = response.json()


# global yahoo_api
# yahoo_api = Yahoo_Api(yahoo_consumer_key,
#                       yahoo_consumer_secret, yahoo_access_key)
# yahoo_api._login()
