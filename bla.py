import requests
import yaml

# Example data in Python dictionary format
data = {
    'name': 'John Doe',
    'age': 30,
    'city': 'Example City',
    'skills': ['Python', 'JavaScript', 'SQL']
}

# Dumping Python data to a YAML file
with open('example.yaml', 'w') as yaml_file:
    yaml.dump(data, yaml_file, default_flow_style=False)

# Loading YAML data from a file
with open('example.yaml', 'r') as yaml_file:
    loaded_data = yaml.load(yaml_file, Loader=yaml.FullLoader)

# Displaying the loaded data
print("Loaded Data:")
print(loaded_data)

# Modifying the loaded data
loaded_data['age'] = 31
loaded_data['skills'].append('React')

# Dumping the modified data back to the YAML file
with open('example.yaml', 'w') as yaml_file:
    yaml.dump(loaded_data, yaml_file, default_flow_style=False)

# Displaying the modified data
print("\nModified Data:")
print(loaded_data)
