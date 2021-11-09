from waio.keyboard.list import ListGroup, ListGroupItem, ListMessage
from examples.list_keyboard.callbacks import callback_list_restaurant, callback_element_restaurant


def generate_button():
    list_group_fastfood = ListGroup(title='Fast Food', subtitle='Not used in docs.')
    kfc = ListGroupItem(title='KFC', callback_data=callback_element_restaurant.new(name='kfc'))  # 1 Variant
    mak = ListGroupItem(title='MAC', callback_data='list:mac')  # 2 Variant

    list_group_rest = ListGroup(title='Restrains', subtitle='Not used in docs.')
    onegin_dacha = ListGroupItem(title='Onegin Dacha', callback_data='list:onegin')
    caffe_pey = ListGroupItem(title='Coffee Pey', callback_data='list_caffe')

    list_group_fastfood.add(kfc).add(mak)
    list_group_rest.add(onegin_dacha).add(caffe_pey)

    data = ListMessage(
        title="В какой ресторан вы пойдете сегодня?",
        body="Тело сообщения",
        callback_data=callback_list_restaurant.new(id='1337'),
        button_title="Click on me!!!",
        items=[list_group_fastfood, list_group_rest]
    )
    return data
