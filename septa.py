import requests
import pprint
import pandas as pd 
import html 

url = 'https://www3.septa.org/api/TrainView/index.php'
headers = {
    'accept': 'application/json'
}

try:
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    data = response.json()
    print(f"Retrieved {len(data)} records.")
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")

df = pd.DataFrame(data)

def location_url(lat, lon):
    url = f"https://www.google.com/maps/search/?api=1&query={lat},{lon}"
    link_text = "View on Google Maps"
    return f'<a href="{url}" target="_blank">{link_text}</a>'

def count_cars(car_list):
    car_count = car_list.split(",")
    return len(car_count) if isinstance(car_count, list) else 0

df['count_cars'] = df['consist'].apply(count_cars)
df['location_url'] = df.apply(lambda row: location_url(row['lat'], row['lon']), axis=1)

lat = df.iloc[0]['lat']
lon = df.iloc[0]['lon']

cols = ['SOURCE', 'currentstop',  'nextstop', 'dest', 'trainno', 'line', 'late', 'count_cars', 'location_url']

df = df[cols]
data_table = df.to_html(table_id="trains", index=False)
data_table = html.unescape(data_table)

page_template = "septa_table_template.html"
with open(page_template, 'r') as template_file:
    template_content = template_file.read()

html_content = template_content.replace("train_table_goes_here", data_table)

file = "result2.html"
with open(file, "w") as file:
    file.write(html_content)
