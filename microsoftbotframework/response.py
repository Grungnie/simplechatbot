import requests, datetime
from microsoftbotframework.helpers import ConfigSectionMap

class Response:
    def __init__(self, data):
        self.config = ConfigSectionMap('CORE')
        if self.config['mode'] == 'test':
            self.config = ConfigSectionMap(['CORE', 'TEST'])
        else:
            self.config = ConfigSectionMap(['CORE', 'PROD'])
        self.data = data

    def __getitem__(self, key):
        try:return self.data[key]
        except:raise KeyError(key)

    def __setitem__(self, key, val):
        self.data[key] = val

    def update(self, *args, **kwargs):
        for k, v in dict(*args, **kwargs).items():
            self[k] = v

    def __delitem__(self, key):
        self.data.pop(key, None)

    def __contains__(self, key):
        return True if key in self.data else False

    def authenticate(self):
        data = {"grant_type": "client_credentials",
                "client_id": self.config['app_client_id'],
                "client_secret": self.config['app_client_secret'],
                "scope": "https://api.botframework.com/.default"
               }
        response = requests.post(self.config['response_auth_url'],data)
        resData = response.json()

        self.headers = {"Authorization": "{} {}".format(resData["token_type"],resData["access_token"])}

    def reply_to_activity(self, message, serviceUrl=None,channelId=None,replyToId=None,fromInfo=None,
                recipient=None,type=None,conversation=None):
        if self.config['mode'] == 'prod':
            self.authenticate()
            print(self.headers)
        else:
            self.headers = None

        conversation_id = self['conversation']["id"] if conversation is None else conversation['id']
        replyToId = self['id'] if replyToId is None else replyToId

        responseURL = "{}v3/conversations/{}/activities/{}".format(self["serviceUrl"], conversation_id, replyToId)

        response_json = {
            "from": self["recipient"] if fromInfo is None else fromInfo,
            "type": 'message' if type is None else type,
            "timestamp": datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f%zZ"),
            "conversation": self['conversation'] if conversation is None else conversation,
            "recipient": self["from"] if recipient is None else recipient,
            "text": message,
            "replyToId": replyToId
        }

        print('responseURL:', responseURL)
        print('response_json:', response_json)

        result = requests.post(responseURL, json=response_json, headers=self.headers)

        print('result:', result)
        print('result.text:', result.text)
        print('result.headers:', result.headers)
