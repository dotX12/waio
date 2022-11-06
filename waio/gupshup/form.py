import json

from waio.utils.form_data import CustomFormData


def generate_message_form(source, receiver, app_name, message: json) -> CustomFormData:
    form = CustomFormData()
    form.add_www_form(name="channel", value="whatsapp")
    form.add_www_form(name="source", value=source)
    form.add_www_form(name="destination", value=receiver)
    form.add_www_form(name="src.name", value=app_name)
    form.add_www_form(name="message", value=message)

    return form
