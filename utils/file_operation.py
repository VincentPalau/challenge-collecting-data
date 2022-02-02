import csv
import os
from threading import Thread, RLock

lock = RLock()

class DictToCSV(Thread):
    """
    This class implements, using threads, the writing of the different properties' informations to a csv file.
    """
    def __init__(self, dictionary: dict) -> None:
        Thread.__init__(self)
        self.dictionary = dictionary

    def run(self, path_to_file: str) -> str:
        with lock:
            saveToCSV(self.dictionary, path_to_file)


def createCSV(path: str) -> str:
    """
    The function that will create a file to paramater's directory. It will create csv file format. if the function catch the error,
    it will be return string message.
    :Param path: The string that will used as a saving directory.
    :Return: The string that will give report message as current issue from function.

    """
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
        """
        The function that will save the property paramater to path paramater as a csv file. It will call the cleanDirectory().
        And then it will write the paramater to csv file as a row.
        :param property: The dictionary that has a property attributes what user wants to save.
        :param path: The string that user wants to save
        """
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
