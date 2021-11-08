import pytest
import requests

url = "http://forddeza2545.pythonanywhere.com"
niffler_id = 1
fairy_id = 3

def test_connection():
    response = requests.get(url)
    assert response.status_code == 200

def test_checkdb():
    response = requests.get(url + '/v1/checkdb')
    response_body = response.json()
    assert response_body["Database connection"] [0] ["1"] == 1

def test_retrieve_all():
    response = requests.get(url + '/v1/beast')
    assert response.status_code == 200

def test_retrieve_count_all():
    response = requests.get(url + '/v1/beast')
    response_body = response.json()
    assert len(response_body) == 3

def test_retrieve_all_niffler():
    response = requests.get(url + '/v1/beast')
    response_body = response.json()
    assert response_body[0]["name"] == "niffler"

def test_update_niffler():
    niffler_data = {"name": "niffler"}
    response = requests.put(url + '/v1/beast/' + str(niffler_id),json = niffler_data)
    response_body = response.json()
    assert response_body["name"] == "niffler"

def test_update_beast_not_exist():
    niffler_data = {"name": "niffler"}
    response = requests.put(url + '/v1/beast/99999999',json = niffler_data)
    assert response.status_code == 404

def test_update_beast_not_match():
    niffler_data = {"name": "niffler"}
    response = requests.put(url + '/v1/beast/' + str(fairy_id),json = niffler_data)
    assert response.status_code == 409



