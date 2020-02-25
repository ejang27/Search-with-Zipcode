

#Tite: searchZipcode.py
#Written by: Eunsoo Jang
#Date: 02/25/2020

import urllib.request
import re

def main():
    open_url = urllib.request.urlopen('http://cs.brynmawr.edu/Courses/cs330/spring2020/uszipcodes.csv').read().decode('utf-8')
    data = open_url.split('\n')
    first_line = data[0].split(',')
    data = data[1:]
    data_dict = createDictionary(data)

    print("There are ", first_line[0], "entries in this database.")
    zipcode_input = input("Input a zip code: ")
    printOut(zipcode_input, search(zipcode_input, data_dict))


def createDictionary(data_file):
    data_dict = {}
    for d in data_file:
        entry = d.split(',')
        data_dict[entry[0]] = entry[1:]

    return data_dict


def search (zipcode, data_dict):
    if zipcode in data_dict:
        return data_dict.get(zipcode)
    else:
        return ""


def printOut(input, output):
    if output == "":
        print("The zip code", input, "is not in the database")
    else:
        address = ','.join(output[0:2])
        print("The zip code", input, "belongs to", address)


if __name__ == "__main__":
    main()
