from waio.keyboard.reply import QuickReplyContentText, QuickReply, KeyboardButton, QuickReplyContentImage
from callback import callback_reply_keyboard


def generate_keyboard_place():
    kb_content = QuickReplyContentText(
        header="Куда вы сегодня хотите сходить?",
        text="Выберите из предложенного списка",
        caption=""
    )
    kb = QuickReply(callback_data=callback_reply_keyboard.new(name="place", id="1"), content=kb_content)
    kb.add(KeyboardButton(title='Кинотеатр')).add(KeyboardButton(title='Ресторан'))

    return kb


def generate_keyboard_cinema_time():
    kb_content = QuickReplyContentText(
        header="Кинотеатр",
        text="Выберите удобное для Вас время",
        caption=""
    )
    kb = QuickReply(callback_data=callback_reply_keyboard.new(name="cinema_time", id="2"), content=kb_content)
    kb.add(KeyboardButton(title='18:00')).add(KeyboardButton(title='20:00'))

    return kb


def generate_keyboard_restaurant_time():
    kb_content = QuickReplyContentText(
        header="Ресторан",
        text="Выберите удобное для Вас время",
        caption="",
    )
    kb = QuickReply(callback_data=callback_reply_keyboard.new(name="restaurant_time", id="2"), content=kb_content)
    kb.add(KeyboardButton(title='18:30')).add(KeyboardButton(title='21:00'))

    return kb


def generate_keyboard_image():  # Можно отправить клавиатуру с изображением, вместо заголовка. В примере не использовалось
    kb_content = QuickReplyContentImage(
        url="https://www.buildquickbots.com/whatsapp/media/sample/jpg/sample01.jpg",
        text="this is the body",
        caption="this is the footer"
    )
    kb = QuickReply(callback_data=callback_reply_keyboard.new(type="start", id="1"), content=kb_content)
    kb.add(KeyboardButton(title='Сменить ресторан')).add(KeyboardButton(title='Новый ресторан'))

    return kb
