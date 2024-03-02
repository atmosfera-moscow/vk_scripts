import vk_api

TOKEN=""

vk_session = vk_api.VkApi(token=TOKEN)
vk = vk_session.get_api()

for id_s in range(1,100):
    id = id_s + 2000000000
    try:
        info = vk.messages.getConversationsById(peer_ids=str(id))["items"]
        if not len(info):
            print(id, "no_info")
        else:
            print(id, info[0]["chat_settings"]["title"], info[0]["chat_settings"]["members_count"])
    except Exception as e:
        print(id, e)