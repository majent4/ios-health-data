from xml.etree.ElementTree import parse as xml_parse, ParseError as xml_error
from utils import print_exit

class XMLParser:
    def __init__(self, xml_file):
        try:
            self.root = xml_parse(xml_file).getroot()
        except xml_error as e:
            print_exit(f'Error parsing file: {e}')
