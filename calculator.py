import api


class Calculator:
    def __init__(self, mileage=12000, years=3, depreciation_oer_year=19):
        self.mileage = mileage
        self.years = years
        self.depreciation_per_year = depreciation_oer_year / 100
        self.vehicles = {}  # Vehicle : Annual_cost

    def add_vehicle(self, vehicle):
        year_cost = vehicle.total_annual_cost(self.mileage)
        price_per_year = vehicle.price / self.years
        price_after_depreciation = self.get_price_after_depreciation(vehicle) / self.years
        self.vehicles[vehicle] = year_cost + price_per_year - price_after_depreciation

    def get_price_after_depreciation(self, vehicle):
        initial_price = vehicle.price
        for i in range(self.years):
            initial_price -= initial_price * self.depreciation_per_year
        return initial_price

    def print_vehicles(self):
        for vehicle, total_annual_cost in self.vehicle.items():
            print(f"{vehicle.name}:    {total_annual_cost}:")


class Vehicle:
    def __init__(self,
                 name: str,
                 price: int,
                 fuel_economy: float,
                 maintenance_cost: int,
                 insurance_cost: int):
        self.name = name
        self.price = price
        self.fuel_economy = fuel_economy
        self.maintenance_cost = maintenance_cost
        self.insurance_cost = insurance_cost

    def static_annual_cost(self):
        return self.maintenance_cost + self.insurance_cost

    def dynamic_annual_cost(self, mileage: int):
        return self.fuel_economy * mileage / 100 * api.get_gas_price()

    def total_annual_cost(self, mileage: int):
        return self.static_annual_cost + self.dynamic_annual_cost(mileage)


class ElectricVehicle(Vehicle):
    def __init__(self,
                 name: str,
                 price: int,
                 insurance_cost: int,
                 power_consumption: int):
        super().__init__(name=name, price=price, fuel_economy=0, maintenance_cost=0, insurance_cost=insurance_cost)
        self.power_consumption = power_consumption

    def dynamic_annual_cost(self, mileage: int):
        return self.power_consumption * mileage / 1000 * api.get_kwt_price()
