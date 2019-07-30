import telegram

class alarm():
    def __init__(self, grade, content):
        self.grade = grade
        self.content = content

    style = {
        "serious": 1,
        "intermediate": 2,
        "general": 3
    }

    grade = 0

    telegram_bot_token = '951515426:AAGS9jXDSszKLXXLlON37TTsuQkFL-UeuEY'
    channel_id = '-1001261640560'

    content = ''

    def telegram_info(self):
        bot = telegram.Bot(token=self.telegram_bot_token)
        bot.send_message(chat_id=self.channel_id, text=self.content)

    def email_info(self):
        pass

    def sing_call(self):
        pass

    def send_alarm(self):
        if self.grade == self.style["intermediate"]:
            self.telegram_info()
        else if self.grade == self.style["general"]:
            self.telegram_info()
            self.

if __name__ == '__main__':
    alarm(2, "fwf").send_alarm()
