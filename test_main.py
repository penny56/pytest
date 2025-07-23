'''
1. Add the function module like func.py
2. import the test target, like get_weather
3. add the test_***() method, with the test_ as the prefix
   with the assert command inside the method
'''

from main import get_weather

def test_get_weather():
    assert get_weather(21) == "hot"