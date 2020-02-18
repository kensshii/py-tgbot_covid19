# -*- coding: utf-8 -*-

from bothandler import BotHandler

def main():
    botHandler = BotHandler('Введите ваш токен')
    botHandler.handle()

if __name__ == "__main__":
    main()