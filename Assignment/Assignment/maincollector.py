import requests
from  bs4 import BeautifulSoup
import matplotlib.pyplot as plt

#import the web data first
url = 'https://scedc.caltech.edu/recent/Quakes/quakes0.html'
response = requests.get(url)
response.raise_for_status()

#use BeautifulSoup to get the data
soup = BeautifulSoup(response.text, 'html.parser')

table = soup.find('table')

#ensure the amount of data I need and create two empty list for x and y
n = 0
max_n = 50
x_list = []
y_list = []

#In the obtained table, to get the second and fifth column of data and append them
if table:
    for row in table.find_all('tr')[1:]:
        cells = row.find_all('td')
        if len(cells) >0:
            column_1 = cells[1].get_text(strip=True)
            column_3 = cells[5].get_text(strip=True)
            x_list.append(column_3)
            y_list.append(column_1)
            n += 1
            if n > max_n:
                break

float_x_list = []
float_y_list = []

#convert every data to float and sort them
for i in range(len(x_list)):
    float_x_list.append(float(x_list[i]))

for i in range(len(y_list)):
    float_y_list.append(float(y_list[i]))

sorted_y_data=sorted(float_y_list,reverse=True)
sorted_x_data = sorted(float_x_list,reverse=True)

#create the graph
plt.figure(figsize=(20,5))
plt.plot(sorted_x_data, sorted_y_data, marker='o', linestyle='-', color='b')

plt.title('Earthquake Magnitude and Depth')
plt.xlabel('Depth')
plt.ylabel('Magnitude')
plt.show()








