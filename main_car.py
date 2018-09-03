import car

def main():
    
    car_info=input().split()
    car_=car.Car(car_info[0], car_info[1], car_info[2])
    print(car_.get_year_model())
    print(car_.get_make())
    print(car_.get_speed())
    for i in range(5):
        car_.accelerate(car_info[2])
        print(car_.get_speed())
    for i in range(5):
        car_.brake(car_info[2])
        print(car_.get_speed())
main()
