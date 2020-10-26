import vk

vktoken = "46e50d8c46e50d8c46e50d8c8a46917fc2446e546e50d8c196fd185478ce57d33254a43"
users=[]
session = vk.Session()
vkapi = vk.API(session)
#сделать функцию трекающую фремя vk
#реализовать бд и работу с ней
def create_user(id):
    data=vkapi.users.get(v=5.124, user_ids=str(id), fields='online, last_seen', access_token=vktoken)[0]
    online=data['online']
    if online==1:
        users.append({'online':True,'id':id,'time_in_vk':0})
    else:
        users.append({'online':False,'id':id,'time_in_vk':0})
    print(users)


def track(id):
    data=vkapi.users.get(v=5.124, user_ids=str(id), fields='online, last_seen', access_token=vktoken)[0]






