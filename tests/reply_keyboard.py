import pytest
from waio.keyboard.reply import QuickReply, QuickReplyContentText, KeyboardButton, QuickReplyContentImage


def test_reply_keyboard_text():
    kb_content = QuickReplyContentText(
        header="this is the header",
        text="this is the body",
        caption="this is the footer"
    )
    kb = QuickReply(callback_data="callback_keyboard_123", content=kb_content)

    kb.add(KeyboardButton(title='keyboard1')).add(KeyboardButton(title='keyboard2'))

    assert kb.dict() == {
        "type": "quick_reply",
        "msgid": "callback_keyboard_123",
        "content": {
            "type": "text",
            "header": "this is the header",
            "text": "this is the body",
            "caption": "this is the footer"
        },
        "options": [
            {
                "type": "text",
                "title": "keyboard1"
            },
            {
                "type": "text",
                "title": "keyboard2"
            }
        ]
    }


def test_reply_keyboard_image():
    kb_content = QuickReplyContentImage(
        text="this is the body",
        caption="this is the footer",
        url="https://www.buildquickbots.com/whatsapp/media/sample/jpg/sample01.jpg"
    )
    kb = QuickReply(callback_data="callback_keyboard_123_img", content=kb_content)

    kb.add(KeyboardButton(title='keyboard1')).add(KeyboardButton(title='keyboard2'))

    assert kb.dict() == {
        "type": "quick_reply",
        "msgid": "callback_keyboard_123_img",
        "content": {
            "type": "image",
            "url": "https://www.buildquickbots.com/whatsapp/media/sample/jpg/sample01.jpg",
            "text": "this is the body",
            "caption": "this is the footer"
        },
        "options": [
            {
                "type": "text",
                "title": "keyboard1"
            },
            {
                "type": "text",
                "title": "keyboard2"
            }
        ]
    }
