import yaml

data = {'one': [1, 2, 3], 'two': 5, 'three': {'1&': '1', '2$': '2'}}
with open('file.yaml', 'w') as f:
    yaml.dump(data, f, default_flow_style=False, allow_unicode=True)
