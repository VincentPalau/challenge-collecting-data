"""
Main program follow to work flow.

"""
import csv
import os

def createCSV(path: str):
    try:
        with open(path, "w+") as file:
            cols = ["Locality", "Price", "Bedrooms", "Living area", "Kitchen type", "Furnished", "Terrace surface", "Garden surface", "Surface of the plot", "Number of frontages", "Swimming pool", "Building condition","Type of property"]
            j = csv.DictWriter(file, fieldnames=cols)
            j.writeheader()
            file.close()
    except FileNotFoundError:
            print("Output file not present", path)
            print("Current dir: ", os.getcwd())
            report_message = "File not found"
            raise FileNotFoundError
    except IOError:
            report_message = "The file can not open/read."
            raise IOError
    else:
            report_message = "Row has been written successfuly."
    
    return report_message


def saveToCSV(property: dict, path: str) -> str:
        report_message = ""
        cols = ["Locality", "Price", "Bedrooms", "Living area", "Kitchen type", "Furnished", "Terrace surface", "Garden surface", "Surface of the plot", "Number of frontages", "Swimming pool", "Building condition","Type of property"]
        try:
            with open(path, 'a', newline="") as csv_file:
                j = csv.DictWriter(csv_file, fieldnames=cols)
                clean_dict = cleanDictionary(property)
                j.writerow(clean_dict)
                csv_file.close()
        except FileNotFoundError:
            print("Output file not present", path)
            print("Current dir: ", os.getcwd())
            report_message = "File not found"
            raise FileNotFoundError
        except IOError:
            report_message = "The file can not open/read."
            raise IOError
        else:
            report_message = "Row has been written successfuly."
        
        return report_message

def cleanDictionary(property: dict) -> dict:
    try:
        cols = ["Locality", "Price", "Bedrooms", "Living area", "Kitchen type", "Furnished", "Terrace surface", "Garden surface", "Surface of the plot", "Number of frontages", "Swimming pool", "Building condition"]
        clean_dict = property
        for col in cols:
            if col not in clean_dict.keys():
                clean_dict[col] = "None"
            if clean_dict[col] == "Yes":
                clean_dict[col] = 1
            elif clean_dict[col] == "No":
                clean_dict[col] = 0

    except:
        print("Data can not clean")
        
    return clean_dict


p1 = {'Building condition': "Good", 'Number of frontages': '3', 'Living area': '101', 'Kitchen type': 'Installed', 'Bedrooms': '2', 'Furnished': 'No', 'Price': '296,000'}
p2 = {'Building condition': 'To renovate', 'Number of frontages': '2', 'Living area': '176', 'Kitchen type': 'Semi equipped', 'Bedrooms': '3', 'Furnished': 'No', 'Surface of the plot': None, 'Garden surface': None, 'Price': '369,000'}
p3 = {'Living area': '87', 'Kitchen type': 'Installed', 'Bedrooms': '2', 'Furnished': 'No', 'Price': '157,500', 'Type of property': 'apartment', 'Locality': 'morlanwelz'}
p4 = {'Building condition': 'To be done up', 'Number of frontages': '4', 'Living area': '220', 'Kitchen type': 'Installed', 'Bedrooms': '4', 'Furnished': 'No', 'Surface of the plot': None, 'Price': '950,000', 'Type of property': 'villa', 'Neighbourhood or locality': 'uccle'}
p5 = {'Building condition': 'Good', 'Number of frontages': '2', 'Living area': '130', 'Kitchen type': 'Semi equipped', 'Bedrooms': '3', 'Furnished': 'No', 'Terrace surface': None, 'Swimming pool': 'No', 'Price': '339,500', 'Type of property': 'apartment', 'Neighbourhood or locality': 'bruxelles'}
p6 = {'Building condition': 'To be done up', 'Number of frontages': '4', 'Living area': '220', 'Kitchen type': 'Installed', 'Bedrooms': '4', 'Furnished': 'No', 'Surface of the plot': '2030', 'Price': '950,000', 'Type of property': 'villa', 'Locality': 'linkebeek'}
p7 = {'Building condition': 'As new', 'Number of frontages': '3', 'Living area': '355', 'Kitchen type': 'Hyper equipped', 'Bedrooms': '3', 'Furnished': 'No', 'Surface of the plot': '500', 'Garden surface': '80', 'Terrace surface': '20', 'Swimming pool': 'No', 'Price': '390,000', 'Type of property': 'house', 'Locality': 'lubbeek'}
#createCSV("./utils/properties.csv")
saveToCSV(p7,"./utils/properties.csv")
