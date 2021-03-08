import types

def main():
	aChargingStation = types.ChargingStation()
	print(aChargingStation.getCategory())

	aCar = types.Car()
	print(aCar.getCharge())


if __name__ == "__main__":
    # execute only if run as a script
    main()
