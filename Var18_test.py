import pytest
from main import count_survivors, prepare_data

# Тест на правильное переименование пунктов посадки
def test_1():
    passenger_data = {
        'Пункт посадки': ['S', 'Q', 'C'],
        'Возраст пассажиров': [10, 5, 15],
        'Выжившие': [5, 2, 8]
    }
    result = prepare_data(passenger_data)
    assert result['Пункт посадки'] == ['Саутгемптон', 'Квинстаун', 'Шербур']

#Тест проверки правильного расчета доли выживших
def test_2():
    passenger_data = {
        'Пункт посадки': ['S', 'Q', 'C'],
        'Возраст пассажиров': [10, 5, 15],
        'Выжившие': [5, 2, 8]
    }
    result = prepare_data(passenger_data)
    assert result['Доля выживших'] == [50, 40, 53]

# Тест проверки обработки нулевых значений
def test_3():
    passenger_data = {
        'Пункт посадки': ['S', 'Q', 'C'],
        'Возраст пассажиров': [0, 0, 0],
        'Выжившие': [0, 0, 0]
    }
    result = prepare_data(passenger_data)
    assert result['Доля выживших'] == [0, 0, 0]
