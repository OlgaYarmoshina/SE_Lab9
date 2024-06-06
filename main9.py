import csv
import matplotlib.pyplot as plt
import streamlit as st


def calculate_survival_rates(data, max_age=None):
    survival_count = {}
    total_count = {}

    # Обработка данных
    for row in data:
        age = float(row['Age']) if row['Age'] else 0
        survived = int(row['Survived'])
        embarked = row['Embarked']

        # Условие для максимального возраста
        if max_age is None or age <= max_age:
            if embarked not in survival_count:
                survival_count[embarked] = 0
                total_count[embarked] = 0

            total_count[embarked] += 1
            if survived == 1:
                survival_count[embarked] += 1

    # Расчет доли выживших
    survival_rate = {
        embarked: (survival_count[embarked] / total_count[embarked]) * 100
        if total_count[embarked] > 0 else 0
        for embarked in survival_count
    }

    return survival_rate


data_file = "data.csv"
with open(data_file, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    data = list(reader)


def do_var18():
    st.header('Максимальный возраст выживших по пунктам посадки пассажиров Титаника')
    max_age = st.slider(
        'Выберите максимальный возраст для анализа выживаемости',
        min_value=0, max_value=100, value=30
    )

    survival_rate_age = calculate_survival_rates(data, max_age=max_age)
    prepared_data = [
        {'Пункт посадки': embarked, 'Доля выживших': rate}
        for embarked, rate in survival_rate_age.items() if rate != 100.00
    ]

    st.subheader('Доля выживших пассажиров по пунктам посадки и выбранному возрасту:')
    st.table(prepared_data)

    # Создание графика
    fig, ax = plt.subplots(figsize=(10, 5))
    embarked = [row['Пункт посадки'] for row in prepared_data]
    survival_rate = [row['Доля выживших'] for row in prepared_data]

    plt.bar(embarked, survival_rate, width=0.3, label='Доля выживших')
    plt.xlabel('Пункт посадки')
    plt.ylabel('Доля выживших (%)')
    plt.title('Доля выживших пассажиров Титаника по пунктам посадки')
    plt.legend()

    st.pyplot(fig)


do_var18()
