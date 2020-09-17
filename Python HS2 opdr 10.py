StandardAmountOfCookies = 48
CupsOfSugarFor48 = 1.5
CupsOfButterFor48 = 1
CupsOfFlourFor48 = 2.75

ChosenAmountOfCookies = float(input("How many cookies do you want to make?: "))

CupsOfSugarForChosenCookies = ChosenAmountOfCookies / StandardAmountOfCookies * CupsOfSugarFor48

CupsOfButterForChosenCookies = ChosenAmountOfCookies / StandardAmountOfCookies * CupsOfButterFor48

CupsOfFlourForChosenCookies = ChosenAmountOfCookies / StandardAmountOfCookies * CupsOfFlourFor48

print("To make " + str(ChosenAmountOfCookies) + " cookies you'll need: " +
      str(CupsOfSugarForChosenCookies) + " cups of sugar, " +
      str(CupsOfButterForChosenCookies) + " cups of butter and " + 
      str(CupsOfFlourForChosenCookies) + " cups of flour.")


