import pytest
# from main import add, sub, mul, div

# def test_add():
#     assert add(10,2) == 12

# def test_mul():
#     assert mul(10, 2) == 20

# def test_sub():
#     assert sub(10, 2) == 8

# def test_div():
#     assert div(10, 2) == 5
#     with pytest.raises(ValueError):
#         div(10, 0)

from main import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_start(client):
    res = client.get('/')
    assert res.data == b"hii, welcome"
    assert res.status_code == 200
    
def test_add(client):
    res = client.get('/add', query_string={'x':3, 'y':5})
    # json_data = res.get_json()
    # assert json_data['ans'] == 8
    assert res.data == b'8'
    assert res.status_code == 200
    
def test_sub(client):
    res = client.get('/sub', query_string={'x':10, 'y':5})
    # json_data = res.get_json()
    # assert json_data['ans'] == 5
    assert res.data == b'5'
    assert res.status_code == 200
    
def test_sub_invalid(client):
    res = client.get('/sub', query_string={'x':'a', 'y':5})
    json_data = res.get_json()
    assert res.status_code == 500