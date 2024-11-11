import configuration
import requests
import data

def create_order(body):
    return requests.post(url=configuration.URL_SERVICE + configuration.CREATE_ORDER,
                         json=body)

def get_track_create_order():
    response = create_order(body=data.create_order_body)
    track = response.json()["track"]
    return track

def get_order_by_number(t):
    params = {"t": t}
    get_response = requests.get(url=configuration.URL_SERVICE + configuration.GET_ORDER_BY_NUMBER,
                        params=params)
    return get_response



