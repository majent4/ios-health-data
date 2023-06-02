from sys import argv as sys_argv, exit as sys_exit
from os.path import isfile
from utils import print_exit
from sqlite_database import SQLiteDatabase

def main():
    if len(sys_argv) == 3 and isfile(sys_argv[1]):
        xml_file = sys_argv[1]
        db_file = sys_argv[2]
    else:
        print_exit('Invalid or missing argument(s)')
    db_exists = isfile(db_file)
    db = SQLiteDatabase(db_file)
    if not db_exists:
        db.commit()
    db.close()
    return 0

if __name__ == '__main__':
    sys_exit(main())
