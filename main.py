with open("data.csv") as file:
    next(file)
    survival_rates = {}
    for line in file:
        data = line.strip().split(',')

            # Извлекаем информацию о возрасте и выживаемости пассажира
        age_str = f"{data[6]}"
        if age_str.isdigit():
            age = float(age_str)
        else:
            age = 0  # Присваиваем 0 для строковых значений возраста
        embarked = f"{data[12]}"
        survived = int(data[1])

            # человек входит в возрастной диапозон от 0,1 до 30 лет. Без возраста и 0 лет не учитываю
        if 0.1 <= age < 30:
        # обновляю данные по посадке
            if embarked in survival_rates:
                total, survivors = survival_rates[embarked]
                survival_rates[embarked] = (total + 1, survivors + survived)
        # добавляю пункт посадки
            else:
                survival_rates[embarked] = (1, survived)

        # доля выживших для посадки
    for embarked, (total, survivors) in survival_rates.items():
        survival_rates[embarked] = survivors / total

    print(survival_rates)