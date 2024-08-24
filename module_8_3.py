class IncorrectVinNumber(Exception):
    def __init__(self, vin_message):
        self.vin_message = vin_message


class IncorrectCarNumbers(Exception):
    def __init__(self, car_num_message):
        self.car_num_message = car_num_message


class Car:
    def __init__(self, model, vin, numbers):
        self.model = model
        self.__vin = vin
        self.__numbers = numbers
        self.__is_valid_vin(vin)
        self.__is_valid_numbers(numbers)

    def __is_valid_vin(self, vin_number):
        if not isinstance(vin_number, int):
            raise IncorrectVinNumber('Некорректный тип vin номер')
        elif vin_number not in range(1000000, 9999999 + 1):
            raise IncorrectVinNumber('Неверный диапазон для vin номера')
        else:
            return True

    def __is_valid_numbers(self, numbers):
        if not isinstance(numbers, str):
            raise IncorrectVinNumber('Некорректный тип данных для номеров')
        elif len(numbers) != 6:
            raise IncorrectVinNumber('Неверная длина номера')
        else:
            return True


try:
    mazda = Car('Mazda', 1123940, 'f123gg')
except IncorrectVinNumber as e_1:
    print(e_1.vin_message)
except IncorrectCarNumbers as e_2:
    print(e_2.car_num_message)
else:
    print(f'{mazda.model} успешно создан!')

try:
    c2 = Car('FastCar', 1123940, 'o54dd')
except IncorrectVinNumber as e_1:
    print(e_1.vin_message)
except IncorrectCarNumbers as e_2:
    print(e_2.car_num_message)
else:
    print(f'{c2.model} успешно создан!')

try:
    c3 = Car('BestMotors', 'wow', 'o132xx')
except IncorrectVinNumber as e_1:
    print(e_1.vin_message)
except IncorrectCarNumbers as e_2:
    print(e_2.car_num_message)
else:
    print(f'{c3.model} успешно создан!')