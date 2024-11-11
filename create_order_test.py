# Гречнева Екатерина, 23-я когорта — Финальный проект. Инженер по тестированию плюс
import sender_stand_request

def test_create_order_and_get_status_code():
    track = sender_stand_request.get_track_create_order()
    get_response = sender_stand_request.get_order_by_number(t=track)

    assert get_response.status_code == 200




