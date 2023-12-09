"""1 -
Add json configuration to your framework. Change all your framework to use json config

2 -
class Human:
    def __init__(self, name, age, gender, birth_year):
        self.name = name
        self.age = age
        self.gender = gender
        self.birth_year = birth_year

    def convert_to_json(self):
        pass

    def convert_to_xml(self):
        pass

Implement provided methods. You need to convert the class instance to JSON or XML. When the user provides the command
json to cli, the program should call convert_to_json, when providing xml to cli program should convert the class
instance to xml string. And print it, or even better write it to a separate file.

You can use third parties libraries for this. If you use such a library please add it to requirenment.txt"""
import json
import xml.etree.ElementTree as ET
import argparse


class Human:
    def __init__(self, name, age, gender, birth_year):
        self.name = name
        self.age = age
        self.gender = gender
        self.birth_year = birth_year

    def convert_to_json(self):
        return json.dumps(self.__dict__)

    def convert_to_xml(self):
        human = ET.Element('Human')
        for key, value in self.__dict__.items():
            title = ET.SubElement(human, key)
            title.text = str(value)
        xml_string = ET.tostring(human, encoding='unicode')
        with open('human.xml', 'w') as file:
            file.write(xml_string)
        return xml_string

    def write_to_file(self, result, extension):
        with open(f"human_output.{extension}", "w") as file:
            file.write(result)

    def convert_and_save(self, output_format):
        if output_format == 'json':
            result = self.convert_to_json()
            extension = 'json'
        elif output_format == 'xml':
            result = self.convert_to_xml()
            extension = 'xml'
        else:
            print("Please provide a valid format: json or xml")
            return

        self.write_to_file(result, extension)
        print(f"Conversion successful. Output written to human_output.{extension}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser('My parser')
    parser.add_argument('format', choices=['json', 'xml'], default='json', help='Output format (json or xml)')
    args = parser.parse_args()

    hum = Human("Anya", 35, "woman", 1988)
    hum.convert_and_save(args.format)
