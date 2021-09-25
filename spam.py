from vk_api import VkApi
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.utils import get_random_id

print("Работает")

vk_session = VkApi(token='23a7826800b2561c59eae1be265ef2b71a87ba8de24717d57902517b25efb3d9098ec55af785f5825e312')
long_poll = VkBotLongPoll(vk_session, '196400814')
vk = vk_session.get_api()


def autosend(spam):
    for event in long_poll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW:
            peer_id = event.obj.message["peer_id"]
            message1 = event.obj.message["text"].lower()

            b = spam.isnumeric()
            if b == False:
                vk.messages.send(peer_id=peer_id, message='Ты клоун! Введи целевое число после autosend',
                                 random_id=get_random_id())
                return
            if int(spam) > 30:
                vk.messages.send(peer_id=peer_id, message='Ты слишком многого хочешь! Давай до 30-и сообщений!',
                                 random_id=get_random_id())
                return
            if message1 == "@all" or message1 == "@everyone" or message1 == "@here" or message1 == "@online":
                vk.messages.send(peer_id=peer_id, message='НЕ ТЕГАЙ!', random_id=get_random_id())
                return
            else:
                vk.messages.send(peer_id=peer_id, message='Начинаю фигачить ' + str(spam) + " раз!",random_id=get_random_id())

                for i in range(1, int(spam) + 1):
                    vk.messages.send(peer_id=peer_id, message=str(i) + str('. ' + message1), random_id=get_random_id())
            vk.messages.send(peer_id=peer_id, message="Моя работа окончена т.к задача выполнена!",random_id=get_random_id())
            return

for event in long_poll.listen():
    if event.type == VkBotEventType.MESSAGE_NEW:
        peer_id = event.obj.message["peer_id"]
        message = event.obj.message["text"].lower()

        if message == 'autosent':
            vk.messages.send(
                peer_id=peer_id,
                message='Баклажан! Пишется "autosenD" а не "autosenT"! Иди английский учить!',
                знrandom_id=get_random_id(),
            )

        if message.startswith('autosend'):
            intspam = message[9:]
            print(f'Я должен проспамить {intspam} раз')
            vk.messages.send(peer_id=peer_id, message="Введи сообщение!", random_id=get_random_id())
            autosend(intspam)

