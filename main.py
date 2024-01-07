import calculator

if __name__ == '__main__':
    calc = calculator.Calculator()
    calc.add_car(
        calculator.Car("Range Rover Velar",
                       35000,
                       25,
                       1200,
                       2500),
    )
    calc.add_car(
        calculator.Car("Range Rover Sport",
                       50000,
                       18,
                       1800,
                       2500),
    )
    calc.add_car(
        calculator.ElectricCar("Tesla Model 3",
                               30000,
                               2000,
                               150),
    )

    calc.print_cars()
