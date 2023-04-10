import requests
import json

url = 'http://localhost:5000/json-to-xml'
data = {"fullname":"George","characteristics":{"sex":"male","age":27},"skills":["smart","strong"],"experience":[{"position":"developer","workplace":"netflix","salary":"7000"},{"position":"engineer","workplace":"facebook","id_card":56117,"Country":"Scotland"}]}
headers = {'Content-type': 'application/json'}

response = requests.post(url, data=json.dumps(data), headers=headers)

if response.ok:
    xml_data = response.text
    print(xml_data)
else:
    print('Ошибка:', response.status_code)


# <data>
#     <fullname>George</fullname>
#     <characteristics>{'sex': 'male', 'age': 27}</characteristics>
#     <skills>['smart', 'strong']</skills>
#     <experience>[{'position': 'developer', 'workplace': 'netflix', 'salary': '7000'}, 
#              {'position': 'engineer', 'workplace': 'facebook', 'id_card': 56117, 'Country': 'Scotland'}]</experience>
# </data>