# -*- coding: utf-8 -*-

class MessageType:

    class Message:
        def __init__(self, data):
            self.messageID = data['message']['message_id']
            self.user = {
                'id'       : data['message']['from']['id'],
                'name'     : data['message']['from']['first_name'],
                'lastName' : data['message']['from']['last_name'],
                'userName' : data['message']['from']['username']
            }
            self.text = data['message']['text']

    class Command:
        def __init__(self, data):
            self.messageID = data['message']['message_id']
            self.user = {
                'id'       : data['message']['from']['id'],
                'name'     : data['message']['from']['first_name'],
                'lastName' : data['message']['from']['last_name'],
                'userName' : data['message']['from']['username']
            }
            self.text = data['message']['text']