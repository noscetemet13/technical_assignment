import json
import xml.etree.ElementTree as ET
from flask import Flask, request

app = Flask(__name__)

@app.route('/json-to-xml', methods=['POST'])
def json_to_xml():
    json_data = request.get_json()
    root = ET.Element('data')
    for key, value in json_data.items():
        child = ET.SubElement(root, key)
        child.text = str(value)
    xml_data = ET.tostring(root, encoding='unicode')
    return xml_data

if __name__ == '__main__':
    app.run(debug=True)