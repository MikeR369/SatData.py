# Author: Michael Russell
# GitHub username: Mike369
# Date: 07/18/2024
# Description: Write a class named SatData that reads a JSON file containing data on 2010 SAT results for New York City
# and writes the data to a text file in CSV format.

import json
import csv


class SatData:
    """
    A class to read SAT data from a JSON file and save selected data as a CSV file.

    Attributes:
    data (list): A list to store the JSON data.
    """

    def __init__(self):
        """
        Initializes the SatData class by reading the 'sat.json' file and storing its data.

        Parameters:
        None

        Returns:
        None
        """
        with open('sat.json', 'r') as file:
            self.data = json.load(file)

    def save_as_csv(self, dbns):
        """
        Saves the SAT data for the specified DBNs to 'output.csv' in CSV format.

        Parameters:
        dbns (List[str]): A list of DBNs (district bureau numbers) to include in the CSV file.

        Returns:
        None
        """
        # Sort the DBNs
        dbns = sorted(dbns)
        output_rows = []

        # Header row
        headers = ["DBN", "SCHOOL NAME", "NUM OF SAT TEST TAKERS", "SAT CRITICAL READING AVG. SCORE",
                   "SAT MATH AVG. SCORE", "SAT WRITING AVG. SCORE"]
        output_rows.append(headers)

        # Data rows
        for school in self.data:
            if school["DBN"] in dbns:
                row = [
                    school["DBN"],
                    f'"{school["SCHOOL NAME"]}"',  # Enclose in double quotes to handle commas in school names
                    school["NUM OF SAT TEST TAKERS"],
                    school["SAT CRITICAL READING AVG. SCORE"],
                    school["SAT MATH AVG. SCORE"],
                    school["SAT WRITING AVG. SCORE"]
                ]
                output_rows.append(row)

        # Write to CSV file
        with open('output.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(output_rows)
