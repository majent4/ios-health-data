from csv import reader as csv_reader
from utils import print_exit

class CSVReader:
    def __init__(self, csv_file):
        try:
            with open(csv_file, 'r') as file:
                self.dict = {rows[0]: rows[1] for rows in csv_reader(file)}
        except IOError as e:
            print_exit(f'Error reading file: {e}')
