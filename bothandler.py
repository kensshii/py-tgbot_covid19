# -*- coding: utf-8 -*-

import requests
from messagetypes import MessageType
from htmlparser import HtmlParser
import time 

class BotHandler:
    def __init__(self, token):
        self.data = ['https://api.telegram.org/bot' + token + '/', None]

    def _getRequest(self):
        response = requests.get(self.data[0] + 'getUpdates', {'timeout' : 150, 'offset' : self.data[1]})
        request  = response.json()['result']

        if (len(request) < 1):
            return None

        request = request[0]
        if request != None:
            if 'edited_message' in request:
                self.data[1] = request['update_id'] + 1
                return None
            if 'entities' in request['message']:
                if request['message']['entities'][0]['type'] == 'bot_command':
                    self.data[1] = request['update_id'] + 1
                    return MessageType.Command(request)
            else:
                self.data[1] = request['update_id'] + 1
                return MessageType.Message(request)
        else:
            return None

    def _sendMsg (self, userId, text):
        requests.post(self.data[0] + 'sendMessage', {'chat_id': userId, 'text':text})

    def _toString(self):
        htmlParser = HtmlParser('https://www.worldometers.info/coronavirus/')
        htmlParser.parse()

        timeStr = time.strftime("%d %b %Y %H:%M:%S", time.gmtime())
        text = "Статистика зараженных на " + timeStr + "\nЗараженных: " + htmlParser.getContent()[0] + "\nУмерших: " + htmlParser.getContent()[1] + "\nВыздоровевших: " + htmlParser.getContent()[2]

        return text

    def handle(self):
        while True:
            data = self._getRequest()
            if data != None:
                if (type(data) == MessageType.Message):
                    if(data.text == '!статистика'):
                        self._sendMsg(data.user["id"], self._toString())

                elif (type(data) == MessageType.Command): 
                    if(data.text == '/stats'):
                        self._sendMsg(data.user["id"], self._toString())
                    elif(data.text == "/помощь") or (data.text == "/help"):
                        self._sendMsg(data.user["id"], "Бот для получения информации о заболевших COVID-19\nЧтобы получить статистику о заболевших введите /stats\n\nИсходники в общем доступе:\nhttps://github.com/kensshii/py-tgbot_covid19")