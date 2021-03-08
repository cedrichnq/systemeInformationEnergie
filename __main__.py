import types

chargingTime = 10	# time to charge one item in a car (in minutes)


def main():
	aChargingStation = types.ChargingStation()
	print(aChargingStation.getChargingTime())

	aCar = types.Car()
	print(aCar.getCharge())


if __name__ == "__main__":
    # execute only if run as a script
    main()
