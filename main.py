import calculator

if __name__ == '__main__':
    calc = calculator.Calculator()
    calc.add_vehicle(
        calculator.Vehicle("BMW 7 series",
                           45000, 14, 1200, 2500),
    )
    calc.add_vehicle(
        calculator.Vehicle("RR Sport",
                           50000, 10, 1800, 2500),
    )
    calc.add_vehicle(
        calculator.ElectricVehicle("Tesla Model 3",
                                   30000, 2000, 150),
    )

    calc.print_vehicles()
