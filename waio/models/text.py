
class MessageText:
    def __init__(self, text: str):
        self.type = 'text'
        self.text = text

    def json(self):
        return {"type": self.type, "text": self.text}