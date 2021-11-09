from waio.keyboard.reply import QuickReplyContentText, QuickReply, KeyboardButton
from callback import callback_reply_keyboard


def generate_keyboard():
    kb_content = QuickReplyContentText(
        header="this is the header",
        text="this is the body",
        caption="this is the footer"
    )
    kb = QuickReply(callback_data=callback_reply_keyboard.new(type="start", id="1"), content=kb_content)
    kb.add(KeyboardButton(title='Сменить ресторан')).add(KeyboardButton(title='Новый ресторан'))

    return kb
