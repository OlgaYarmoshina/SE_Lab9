import matplotlib.pyplot as plt
import streamlit as st
import csv


def count_survivors(filter):
    with open("data.csv") as file:
        csv_file = csv.reader(file)
        next(csv_file)
        result = {
            'Пункт посадки': [],
            'Возраст пассажиров': [],
            'Выжившие': [],
        }
        for line in csv_file:
            age_str = line[5]
            if age_str.isdigit():
                age = int(age_str)
            else:
                age = 0
            embarked = line[11]
            survived = int(line[1])
            if embarked:

                if age > filter:
                    continue
                if embarked in result['Пункт посадки']:
                    indx = result['Пункт посадки'].index(embarked)
                    result['Возраст пассажиров'][indx] += 1
                    if survived:
                        result['Выжившие'][indx] += 1
                else:
                    result['Пункт посадки'].append(embarked)
                    result['Возраст пассажиров'].append(1)
                    result['Выжившие'].append(1 if survived else 0)
    return result


def prepare_data(passenger_data):
    passenger_data['Доля выживших'] = []
    for v1, v2 in zip(passenger_data['Возраст пассажиров'], passenger_data['Выжившие']):
        passenger_data['Доля выживших'].append(
            round(v2 / v1 * 100)
        )
    passenger_data.pop('Возраст пассажиров')
    passenger_data.pop('Выжившие')
    passenger_data['Пункт посадки'][passenger_data['Пункт посадки'].index('S')] = 'Саутгемптон'
    passenger_data['Пункт посадки'][passenger_data['Пункт посадки'].index('Q')] = 'Квинстаун'
    passenger_data['Пункт посадки'][passenger_data['Пункт посадки'].index('C')] = 'Шербур'
    return passenger_data


def main():
    st.image('titaniс.jpg')
    st.subheader('Максимальный возрат выживших по пунктам посадки пассажиров Титаника')
    slider = st.slider(
        'максимальный возраст',
        min_value=0,
        max_value=100,
        value=100
    )
    data = prepare_data(count_survivors(slider))
    st.table(data)

    fig = plt.figure(figsize=(10, 5))

    embarked = data['Пункт посадки']
    survival_rate = data['Доля выживших']

    plt.bar(embarked, survival_rate, width=0.3, label='Доля выживших')
    plt.xlabel('Место посадки')

    plt.ylabel('Доля выживших (%)')
    plt.title('Доля выживших пассажиров')
    plt.legend()
    st.pyplot(fig)
main()