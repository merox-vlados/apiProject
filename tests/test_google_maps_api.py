import json
import allure
from utils.api import Google_maps_api
from utils.cheking import Checking

"""Создание, изменение и удаление новой локации"""
@allure.epic("Test create place")
class Test_create_place():

    @allure.description("Test create, update, delete new place")
    def test_create_new_place(self):

        print("\n" + "Метод POST")
        result_post = Google_maps_api.create_new_place()
        check_post = result_post.json()
        place_id = check_post.get("place_id")
        Checking.check_status_code(result_post, 200)
        token = json.loads(result_post.text)
        Checking.check_json_token(result_post, list(token))
        Checking.check_json_value(result_post, 'status', 'OK')

        print("\n" + "Метод GET POST")
        result_get = Google_maps_api.get_new_place(place_id)
        Checking.check_status_code(result_get, 200)
        token = json.loads(result_get.text)
        Checking.check_json_token(result_get, list(token))
        Checking.check_json_value(result_get, 'address', '29, side layout, cohen 09')

        print("\n" + "Метод PUT")
        result_put = Google_maps_api.put_new_place(place_id)
        Checking.check_status_code(result_put, 200)
        token = json.loads(result_put.text)
        Checking.check_json_token(result_put, list(token))
        Checking.check_json_value(result_put, 'msg', 'Address successfully updated')

        print("\n" + "Метод GET PUT")
        result_get = Google_maps_api.get_new_place(place_id)
        Checking.check_status_code(result_get, 200)
        token = json.loads(result_get.text)
        Checking.check_json_token(result_get, list(token))
        Checking.check_json_value(result_get, 'address', '100 Lenina street, RU')

        print("\n" + "Метод DELETE")
        result_delete = Google_maps_api.delete_new_place(place_id)
        Checking.check_status_code(result_delete, 200)
        token = json.loads(result_delete.text)
        Checking.check_json_token(result_delete, list(token))
        Checking.check_json_value(result_delete, 'status', 'OK')

        print("\n" + "Метод GET DELETE")
        result_get = Google_maps_api.get_new_place(place_id)
        Checking.check_status_code(result_get, 404)
        token = json.loads(result_get.text)
        Checking.check_json_token(result_get, list(token))
        print(token)
        Checking.check_json_value(result_get, 'msg', "Get operation failed, looks like place_id  doesn't exists")
        Checking.check_json_search_word_in_value(result_get, 'msg', 'failed')


