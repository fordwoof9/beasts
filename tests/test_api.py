import pytest
import requests

url = "http://forddeza2545.pythonanywhere.com"

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
    assert response_body["Niffler"]["name"] == "Niffler"