# py-tgbot_covid19
Coronavirus (COVID 19) Бот для Телеграмма, написанный на Python3. Является базовым примером написания бота и на данный момент не рассчитан на большой функционал.

## Использованные библиотеки:
**_BeautifulSoup_** - для парсинга *html* страниц

**_requests_** - для обработки json запросов

Стандартная библиотека **_time_** для получения текущего времени

##### Все нестандартные библиотеки можете получить через pip:

    pip3 install BeautifulSoup4
    pip3 install requests
    

Код прописывается в bothandler.py в методе handle:
```python
      def handle(self):
        while True:
            data = self._getRequest()
            if data != None:
                # something...
```

## Обработка request
На данный момент есть два MessageType, их можете посмотреть и изменить в messagetypes.py:

        MessageType.Message
        MessageType.Command
        
Примерный код для работы:
```python
      def handle(self):
        while True:
            data = self._getRequest()
            if data != None:
                if (type(data) == MessageType.Message):
                    self._sendMsg(data.user["id"], "Вы ввели текст")
                elif (type(data) == MessageType.Command): 
                    self._sendMsg(data.user["id"], "Вы ввели команду")
```
Стоит заметить, что бот обрабатывает команды лишь латинницей, команды типа /команда будут рассмотрены как **Message**

## Заключение
Так как бот рассчитан только на вывод информации, функционал у него узкий. В дальнейшем возможно бот будет дорабатываться, добавится возможность отправлять/обрабатывать стикеры, меню и прочее.
