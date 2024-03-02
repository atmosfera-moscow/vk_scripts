import vk_api
print('222')

TOKEN=""
# vk_session = vk_api.VkApi()
vk_session = vk_api.VkApi(token=TOKEN)
vk = vk_session.get_api()
# print(vk.users.get(
#     id=1,
#     access_token=TOKEN
#     ))

print(vk.messages.send(
    random_id=4113211,
    access_token=TOKEN,
    peer_id=2000000008,
    message=("""
7 часов до окончания народного Голосования
Успей выбрать лучших в #НоминацииПрофсоюза!
0. Инвайт
1. Пруфы
2. Голосование

Собрано 3406р. из необходимых 4000 на грамоты и подарки
Сбор в Сбере
Или Сбер/Тиньк, Дмитрий П.

До встречи на Слёте! @all

С любовью,
Ваш Профсоюз
"""),
    attachment="",
    dont_parse_links=1,
    # reply_to=3836314,
    ))
    