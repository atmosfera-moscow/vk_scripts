import vk_api
print('222')

TOKEN = ""
# vk_session = vk_api.VkApi()
vk_session = vk_api.VkApi(token=TOKEN)
vk = vk_session.get_api()
# print(vk.users.get(
#     id=1,
#     access_token=TOKEN
#     ))

keyboard = """{
 "one_time":false,
 "buttons":[
 [
 {
 "action":{
 "type":"text",
 "label":"Да здравствует Марина @id320375113"
 },
 "color":"negative"
 }
 ],
 [
 {
 "action":{
 "type":"text",
 "label":"Да здравствует Вероника @vvvv_002"
 },
 "color":"positive"
 }
 ],
 [
 {
 "action":{
 "type":"text",
 "label":"Спасибо, Дима @theawwesome 💖"
 },
 "color":"primary"
 }
 ],
 [
 {
 "action":{
 "type":"text",
 "label":"Спасибо,Саша @khomoch_kaa  💜"
 },
 "color":"secondary"
 }
 ]
 ]}"""

# keyboard = """{
# "one_time":false,
# "buttons":[
# [
# {
# "action":{
# "type":"text",
# "label":"Да здравствует Глеб @id166147232 😎"
# },
# "color":"negative"
# }
# ],
# [
# {
# "action":{
# "type":"text",
# "label":"Глеб @id166147232 как ты это вывозишь😲"
# },
# "color":"negative"
# }
# ],
# [
# {
# "action":{
# "type":"text",
# "label":"Да здравствует Жанна @segedushka💘"
# },
# "color":"positive"
# }
# ],
# [
# {
# "action":{
# "type":"text",
# "label":"В этот раз не прое...Жанна @segedushka😶"
# },
# "color":"positive"
# }
# ]
# ]}"""

keyboard = """{"buttons":[],"one_time":true}"""

# keyboard = """{ "one_time":false, "buttons":[ [ { "action":{ 
# "type":"text", "label":"С новым годом, Атмосфера"
# },
# "color":"negative"
# }]]}"""

print(vk.messages.send( random_id=4365232382, access_token=TOKEN, 
    peer_id=2000000001, message=(""" Да здравствует Атмосфера! Да 
    здравствует ещё один продуктивный год!!  """), dont_parse_links=1, 
    keyboard=keyboard,
 ))
