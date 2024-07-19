# Author: Michael Russell
# GitHub username: Mike369
# Date: 07/18/2024
# Description: Write a class named SatData that reads a JSON file containing data on 2010 SAT results for New York City
# and writes the data to a text file in CSV format.

import json

class SatData:
    """
    A class to read SAT data from a JSON file and save selected data as a CSV file.
    
    Attributes
    ----------
    data : list
        A list to store the JSON data.
    """
    
    def __init__(self):
        """
        Initializes the SatData class by reading the 'sat.json' file and storing its data.
        
        Parameters
        ----------
        None
        
        Returns
        ----------
        None
        """
        with open('sat.json', 'r') as file:
            self.data = json.load(file)

    def save_as_csv(self, dbns):
        """
        Saves the SAT data for the specified DBNs to 'output.csv' in CSV format.
        
        Parameters
        ----------
        dbns : list[str]
            A list of DBNs (district bureau numbers) to include in the CSV file.
        
        Returns
        ----------
        None
        """
        # Sort the DBNs
        dbns = sorted(dbns)
        output_rows = []

        # Header row
        headers = ["DBN", "SCHOOL NAME", "Num of SAT Test Takers", 
                   "SAT Critical Reading Avg. Score", "SAT Math Avg. Score", 
                   "SAT Writing Avg. Score"]
        output_rows.append(headers)
        
        # Data rows
        for item in self.data:
            if item['DBN'] in dbns:  # Access the correct field name for the DBN
                school_name = f'"{item["SCHOOL NAME"]}"'  # Enclose in double quotes to handle commas in school names
                row = [
                    item['DBN'],  # Access the correct field name for DBN
                    school_name,  # School name enclosed in double quotes
                    str(item["Num of SAT Test Takers"]),  # Access the correct field name
                    str(item["SAT Critical Reading Avg. Score"]),  # Access the correct field name
                    str(item["SAT Math Avg. Score"]),  # Access the correct field name
                    str(item["SAT Writing Avg. Score"])  # Access the correct field name
                ]
                output_rows.append(row)
        
        # Write to CSV file
        with open('output.csv', 'w', newline='') as file:
            for row in output_rows:
                file.write(','.join(row) + '\n')
