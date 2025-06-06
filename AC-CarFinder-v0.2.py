# Allowed vehicles
def main():
    AllowedVehiclesList = ['Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck', 'Toyota Tundra', 'Nissan Titan']

    print('********************************')
    print('AutoCountry Vehicle Finder v0.2')
    print('********************************')

    while True:
        print('Please Enter the following number below from the following menu:')
        print('1. Print All Authorized Vehicles')
        print('search for Authorized Vehicle')
        print('3. Exit')

        user_input = input("Enter your choice: ")

        if user_input == "1":
            print("The AutoCountry sales manager has authorized the purchase and selling of the following vehicles:")
            for vehicle in AllowedVehiclesList:
                print(vehicle)
            print("********************************")
            print('AutoCountry Vehicle Finder v0.2')
            print('********************************')
        elif user_input == "2":
            search_vehicle = input("Please Enter the full Vehicle name: ")
            if search_vehicle in AllowedVehiclesList:
                print(f"{search_vehicle} is an authorized vehicle")
            else:
                print(f"{search_vehicle} is not an authorized vehicle, if you received this in error please check the spelling and try again")
            print("********************************")
            print('AutoCountry Vehicle Finder v0.2')
            print('********************************')
        elif user_input == "3":
            print("Thank you for using the AutoCountry Vehicle Finder, good-bye!")
            break
        else:
            print("Invalid input. Please enter 1, 2, or 3.")
if __name__ == "__main__":
        main()
