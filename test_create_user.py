import vk_api
import unittest
import vk
session = vk.Session()
vkapi = vk.API(session)


class TestVkApiMethods(unittest.TestCase):

    def test_add_online_user(self):
        vk_api.create_user('100634762')
        data = vkapi.users.get(v=5.124, user_ids=100634762, fields='online, last_seen', access_token=vk_api.vktoken)[0]
        online = data['online']
        x=False
        if online==1:
            x=True
        self.assertEqual(vk_api.users[0], {'online': online, 'id': "100634762", 'time_in_vk': 0})


    def test_add_afk_user(self):
        vk_api.create_user('mezentzevv')
        data = vkapi.users.get(v=5.124, user_ids='mezentzevv', fields='online, last_seen', access_token=vk_api.vktoken)[0]
        online = data['online']
        x = False
        if online == 1:
            x = True
        self.assertEqual(vk_api.users[0], {'online': online, 'id': 'mezentzevv', 'time_in_vk': 0})



