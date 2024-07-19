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
        
        # Ensure that data is a list of dictionaries
        if not isinstance(self.data, list) or not all(isinstance(item, dict) for item in self.data):
            raise ValueError("JSON data must be a list of dictionaries.")
        
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
            if item.get('DBN') in dbns:  # Use .get() to safely access keys
                school_name = f'"{item.get("SCHOOL NAME", "")}"'  # Enclose in double quotes to handle commas in school names
                row = [
                    item.get('DBN', ""),  # Use .get() to safely access keys
                    school_name,  # School name enclosed in double quotes
                    str(item.get("Num of SAT Test Takers", "")),  # Use .get() to safely access keys
                    str(item.get("SAT Critical Reading Avg. Score", "")),  # Use .get() to safely access keys
                    str(item.get("SAT Math Avg. Score", "")),  # Use .get() to safely access keys
                    str(item.get("SAT Writing Avg. Score", ""))  # Use .get() to safely access keys
                ]
                output_rows.append(row)
        
        # Write to CSV file
        with open('output.csv', 'w', newline='') as file:
            for row in output_rows:
                file.write(','.join(row) + '\n')
