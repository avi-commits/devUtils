import requests
from bs4 import BeautifulSoup

# website to visit
url = "https://www.digminecraft.com/generators/summon_mob.php"

# specify which option to select from the drop-down menu
dropdown_value = "304"

# make a GET request to the website
response = requests.get(url)

# parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# find the drop-down menu element
dropdown = soup.find('select', {'name': 'mob'})
print(dropdown)

# find the option element with the specified value
option = dropdown.find('option', {'value': dropdown_value})
print(option)

# select the option by setting the "selected" attribute to "True"
option['selected'] = True

#find the generate command button by class and name
generate_command = soup.find('input', {'class': 'btn btn-success', 'name': 'Generate Command'})

# find the generate button element
#generate_button = soup.find('input', {'type': 'button', 'name': 'reset'})
print("found generate button: ", generate_command)

# extract the form data
form_data = {i['name']: i.get('value') for i in soup.find_all('input')}

# add the generate button name and value to the form data
form_data['generate_button'] = generate_command['value']

# add the selected option to the form data
form_data['dropdown_name'] = dropdown_value

# make a POST request to the website with the form data
response = requests.post(url, data=form_data)

# store the response in a variable
result = response.content

# print the result
print(result)
