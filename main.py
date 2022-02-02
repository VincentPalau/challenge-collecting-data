"""
Main program follow to work flow.

"""

def createCSV(path: str):
    with open(path, "w+") as file:
        cols = ["Neighbourhood or locality", "Price", "Bedrooms", "Living area", "Kitchen type", "Furnished", "Terrace surface", "Garden surface", "Surface of the plot", "Number of frontages", "Swimming pool", "Building condition"]
        j = csv.DictWriter(file, fieldnames=cols)
        j.writeheader()
        file.close()

def saveToCSV(property: dict, path: str) -> str:
        cols = ["Neighbourhood or locality", "Price", "Bedrooms", "Living area", "Kitchen type", "Furnished", "Terrace surface", "Garden surface", "Surface of the plot", "Number of frontages", "Swimming pool", "Building condition"]
        with open(path, 'a', newline="") as csv_file:
            j = csv.DictWriter(csv_file, fieldnames=cols)
            for col in cols:
                if not bool(property[col]):
                    property[col] = None
            j.writerow(property)
            csv_file.close()