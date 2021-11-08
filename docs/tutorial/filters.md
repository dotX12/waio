[comment]: <> (# Filters)

[comment]: <> (Для того чтобы хендлер ловил только нужные сообщения/другие ивенты нужны правила &#40;rules, рулзы - устоявшаяся транслитерация в комьюнити вкботла&#41;, в вкботле существует множество рулзов прямо из коробки, но в большинстве своем они подходят только для одного ивента - ивента сообщений)

[comment]: <> (Чтобы получить доступ к правилам из коробки вы можете поступить по-разному:)

[comment]: <> (1. Импортировать их из `vkbottle.bot.rules` и использовать, инициализируя прямо в декораторе или в любой другой части кода:)

[comment]: <> (    ```python)

[comment]: <> (    from vkbottle.bot import rules)

[comment]: <> (    from typing import Tuple)

[comment]: <> (    @bot.on.message&#40;rules.CommandRule&#40;"say", ["!", "/"], 1&#41;&#41;)

[comment]: <> (    async def say_handler&#40;message: Message, args: Tuple[str]&#41;:)

[comment]: <> (        await message.answer&#40;f"<<{args[0]}>>"&#41;)

[comment]: <> (    ```)

[comment]: <> (2. Использовать автораспаковщики рулзов из коробки, список с названиями можно найти [здесь]&#40;https://github.com/vkbottle/vkbottle/blob/master/vkbottle/framework/bot/labeler/default.py#L34&#41;, в этом случае некоторые второстепенные параметры контролировать будет нельзя)

[comment]: <> (    ```python)

[comment]: <> (    @bot.on.message&#40;command=&#40;"say", 1&#41;&#41;)

[comment]: <> (    async def say_handler&#40;message: Message, args: Tuple[str]&#41;:)

[comment]: <> (        await message.answer&#40;f"<<{args[0]}>>"&#41;)

[comment]: <> (    ```)

[comment]: <> (Правил может быть любое количество, как первого, так и второго метода распаковки)

[comment]: <> (## Создание собственных правил)

[comment]: <> (> Правило - это класс соответствующий интерфейсу `ABCRule`, который должен реализовать лишь один асинхронный метод `check`, принимающий ивент и возвращающий `False` если проверка пройдена не была и `True` либо словарь с аргументами, которые будут распакованы в хендлер как непозиционные аргументы)

[comment]: <> (### Создание правил напрямую)

[comment]: <> (Чтобы создать правила импортируем продолженный от `ABCRule` абстрактный интерфейс `ABCMessageRule` и имплементируем асинхронный метод `check`, еще стоит импортировать `Union` из `typing` для типизации вашего кода:)

[comment]: <> (```python)

[comment]: <> (from vkbottle.bot import rules)

[comment]: <> (from typing import Union)

[comment]: <> (class MyRule&#40;rules.ABCMessageRule&#41;:)

[comment]: <> (    async def check&#40;self, message: Message&#41; -> Union[dict, bool]:)

[comment]: <> (        ...)

[comment]: <> (```)

[comment]: <> (Теперь стоит имплементировать логику правила `MyRule`, пусть оно будет просто проверять что длина сообщения меньше ста символов:)

[comment]: <> (```python)

[comment]: <> (return len&#40;message.text&#41; < 100)

[comment]: <> (```)

[comment]: <> (Вот что получилось:)

[comment]: <> (> Union в данном правиле не понадобился поэтому его допустимо опустить по стандартам mypy, в любом случае на сигнатуру это не повлияет)

[comment]: <> (```python)

[comment]: <> (from vkbottle.bot import rules)

[comment]: <> (from typing import Union)

[comment]: <> (class MyRule&#40;rules.ABCMessageRule&#41;:)

[comment]: <> (    async def check&#40;self, message: Message&#41; -> bool:)

[comment]: <> (        return len&#40;message.text&#41; < 100)

[comment]: <> (```)

[comment]: <> (Теперь правило можно использовать как первым способом:)

[comment]: <> (```python)

[comment]: <> (@bot.on.message&#40;MyRule&#40;&#41;&#41;)

[comment]: <> (```)

[comment]: <> (Вторым способом рулзом `MyRule` в текущем состоянии воспользоваться не получится, из-за отсутствия каких-либо параметров правила, предлагается его кастомизировать с помощью метода `__init__`:)

[comment]: <> (```python)

[comment]: <> (# Новый вид правила)

[comment]: <> (class MyRule&#40;rules.ABCMessageRule&#41;:)

[comment]: <> (    def __init__&#40;self, lt: int = 100&#41;:)

[comment]: <> (        self.lt = lt)

[comment]: <> (    async def check&#40;self, message: Message&#41; -> bool:)

[comment]: <> (        return len&#40;message.text&#41; < self.lt)

[comment]: <> (```)

[comment]: <> (Теперь, если предварительно &#40;до объявления хендлеров&#41; зарегистрировать правило в локальный лейблер)

[comment]: <> (```python)

[comment]: <> (bot.labeler.custom_rules["my_rule"] = MyRule)

[comment]: <> (```)

[comment]: <> (его можно будет использовать и вторым способом:)

[comment]: <> (```python)

[comment]: <> (@bot.on.message&#40;my_rule=50&#41;)

[comment]: <> (```)

[comment]: <> (### Создание правил через правила-врапперы)

[comment]: <> (> Есть так называемые правила-врапперы, правила которые исполняют какой-то код который получают как параметры)

[comment]: <> (К правилам-врапперам из коробки можно отнести: `func`, шорткат `FuncRule`; `coro` или `coroutine`, шорткат `CoroutineRule`)

[comment]: <> (`FuncRule` принимает в качестве аргумента функцию &#40;которая может быть лямбдой&#41;. Созданное напрямую правило `MyRule` можно заменить вот так:)

[comment]: <> (```python)

[comment]: <> (@bot.on.message&#40;func=lambda message: len&#40;message.text&#41; < 100&#41;)

[comment]: <> (```)

[comment]: <> (`FuncRule` принимает корутину.)

[comment]: <> (> Еще существуют фильтры, они могут помочь контролировать какие-то множества рулзов которые могут исполняться выборочно. В vkbottle [существует]&#40;https://github.com/vkbottle/vkbottle/blob/master/vkbottle/tools/dev_tools/utils.py#L26&#41; автоматическая распаковка и трансформация некоторых инстансов в фильтры &#40;стоит заметить что рекурсивно это не работает&#41;, а именно:)

[comment]: <> (> * `Rule1&#40;&#41; & Rule2&#40;&#41;` конвертируется в фильтр `AndFilter`)

[comment]: <> (> * `Rule1&#40;&#41; | Rule2&#40;&#41;` конвертируется в фильтр `OrFilter`)

[comment]: <> (> * `~Rule2&#40;&#41;` конвертируется в фильтр `NotFilter`)

[comment]: <> (>)

[comment]: <> (> Вместо фильтров еще можно использовать несколько разных хендлеров &#40;это будет схоже с результатом использования `OrFilter`&#41;:)

[comment]: <> (> ```python)

[comment]: <> (> @bot.on.message&#40;some_rule=1&#41;)

[comment]: <> (> @bot.on.message&#40;some_rule=100&#41;)

[comment]: <> (> ```)

[comment]: <> (> Еще стоит заметить, что многие правила принимают в качестве аргумента итерабельный элемент для того чтобы самим имплементировать фильтр, как например `VBMLRule`, стоящий за `text`)


[comment]: <> (## Экзамплы по этой части туториала)

[comment]: <> (* [labeler-setup]&#40;https://github.com/vkbottle/vkbottle/tree/master/examples/high-level/labeler_setup.py&#41;)

[comment]: <> (* [filters-shortcuts]&#40;https://github.com/vkbottle/vkbottle/tree/master/examples/high-level/filters_shortcuts.py&#41;)