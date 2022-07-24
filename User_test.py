import pytest
import json

from common import Common


# pytest 的class名称必须以 Test 开头，方法以 test_开头
class TestUser:
    comm = None

    def setup(self):
        print('setup')
        # 实例化自己的Common
        comm = Common('http://127.0.0.1:8080')
        self.comm = comm

    def test_createUser(self):
        print('createUser start...')

        payload = {"name": "loomz", "age": 36, "sex": "男", "birth": "1986-05-11"}

        response = self.comm.post_json("/user", params=payload)

        print('Response内容：' + response.text)

        # 通过返回值的code判断是否成功，0为成功，非0则抛出异常
        responseJson = json.loads(response.text)

        print("user id=%s" % responseJson["data"])

        assert responseJson['code'] == 0

    def test_getUser(self):
        id = 1
        response = self.comm.get("/user/%s" % 1)
        print('Response内容：' + response.text)

    def test_updateUser(self):
        payload = {"name": "loomz1", "birth": "1986-05-12"}

        response = self.comm.put_json("/user/%s" % 1, params=payload)

        print('Response内容：' + response.text)

        # 通过返回值的code判断是否成功，0为成功，非0则抛出异常
        responseJson = json.loads(response.text)

        print("user id=%s" % responseJson["data"])

    def test_deleteUser(self):
        response = self.comm.delete("/user", 1)

        print('Response内容：' + response.text)

        # 通过返回值的code判断是否成功，0为成功，非0则抛出异常
        responseJson = json.loads(response.text)

