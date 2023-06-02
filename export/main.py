from sys import argv as sys_argv, exit as sys_exit
from os.path import isfile, dirname, abspath
from utils import print_exit
from sqlite_database import SQLiteDatabase
from xml_parser import XMLParser
from csv_reader import CSVReader

def main():
    if len(sys_argv) == 3 and isfile(sys_argv[1]):
        xml_file = sys_argv[1]
        db_file = sys_argv[2]
    else:
        print_exit('Invalid or missing argument(s)')
    db_exists = isfile(db_file)
    db = SQLiteDatabase(db_file)
    if not db_exists:
        records = CSVReader(f'{dirname(abspath(__file__))}/activities.csv').dict
        parser = XMLParser(xml_file)
        records_found = []
        for record in parser.root.iter('Record'):
            record_type = record.attrib['type']
            if record_type not in records_found and record_type in records:
                records_found.append(record_type)
        for record_type in records_found:
            db.create_table_if_not_exists(record_type,
                f'''id INTEGER PRIMARY KEY,
                startDate DATE,
                endDate DATE,
                value {records[record_type]}''')
        for record in parser.root.iter('Record'):
            record_type = record.attrib['type']
            record_start_date = record.attrib['startDate']
            record_end_date = record.attrib['endDate']
            record_value = 1 if record_type == 'HKCategoryTypeIdentifierSleepAnalysis' \
                else record.attrib['value']
            db.execute(f'''INSERT INTO {record_type} (startDate, endDate, value)
                VALUES (?, ?, ?)''', (record_start_date, record_end_date, record_value))
        db.commit()
    db.close()
    return 0

if __name__ == '__main__':
    sys_exit(main())
