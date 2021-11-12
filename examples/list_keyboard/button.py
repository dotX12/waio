from waio.keyboard.list import ListGroup, ListGroupItem, ListMessage
from examples.list_keyboard.callbacks import callback_list_dish, callback_element_potato, callback_element_rice


def generate_button():
    list_group_mashed_potatoes = ListGroup(title='Картофельное пюре', subtitle='Not used in docs.')
    mashed_potatoes_cutlets = ListGroupItem(title='Пюре с котлетками',
                                            callback_data=callback_element_potato.new(name="cutlets", id="1"))
    mashed_potatoes_chicken = ListGroupItem(title='Пюре с курочкой',
                                            callback_data=callback_element_potato.new(name="chicken", id="2"))

    list_group_rice = ListGroup(title='Рис', subtitle='Not used in docs.')
    rice_cutlets = ListGroupItem(title='Рис с котлетками',
                                 callback_data=callback_element_rice.new(name="cutlets", id="3"))
    rice_chicken = ListGroupItem(title='Рис с курочкой',
                                 callback_data=callback_element_rice.new(name="chicken", id="4"))

    list_group_mashed_potatoes.add(mashed_potatoes_cutlets).add(mashed_potatoes_chicken)
    list_group_rice.add(rice_cutlets).add(rice_chicken)

    data = ListMessage(
        title="Что Вы сегодня хотите на ужин?",
        body="Выберите из предложенного списка",
        callback_data=callback_list_dish.new(id='1234'),
        button_title="Нажмите для выбора",
        items=[list_group_mashed_potatoes, list_group_rice]
    )
    return data
