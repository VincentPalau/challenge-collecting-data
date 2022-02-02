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



