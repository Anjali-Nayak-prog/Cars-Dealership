from .models import CarMake, CarModel


def initiate():
    car_make_data = [
        {"name": "NISSAN", "description": "Great cars. Japanese technology"},
        {"name": "Mercedes", "description": "Great cars. German technology"},
        {"name": "Audi", "description": "Great cars. German technology"},
        {"name": "Kia", "description": "Great cars. Korean technology"},
        {"name": "Toyota", "description": "Great cars. Japanese technology"},
    ]

    car_make_instances = []

    for data in car_make_data:
        car_make_instances.append(
            CarMake.objects.create(
                name=data['name'],
                description=data['description']
            )
        )

    car_model_data = [
        {"name": "Pathfinder", "type": "SUV", "year": 2023, "car_make": car_make_instances[0]},
        {"name": "Qashqai", "type": "SUV", "year": 2023, "car_make": car_make_instances[0]},
        {"name": "X5", "type": "SUV", "year": 2023, "car_make": car_make_instances[1]},
        {"name": "A4", "type": "SEDAN", "year": 2023, "car_make": car_make_instances[2]},
        {"name": "Q7", "type": "SUV", "year": 2023, "car_make": car_make_instances[2]},
        {"name": "Sorento", "type": "SUV", "year": 2023, "car_make": car_make_instances[3]},
        {"name": "Sportage", "type": "SUV", "year": 2023, "car_make": car_make_instances[3]},
        {"name": "Camry", "type": "SEDAN", "year": 2023, "car_make": car_make_instances[4]},
        {"name": "Corolla", "type": "SEDAN", "year": 2023, "car_make": car_make_instances[4]},
    ]

    for data in car_model_data:
        CarModel.objects.create(
            name=data['name'],
            type=data['type'],
            year=data['year'],
            car_make=data['car_make']
        )