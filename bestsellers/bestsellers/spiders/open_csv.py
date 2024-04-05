import csv
import re
from collections import defaultdict

csv_file_path = 'ozon.csv'

pattern = re.compile(r'(iOS|Android) (\S+)')

results_dict = defaultdict(lambda: defaultdict(int))


with open(csv_file_path, 'r', newline='', encoding='utf-8') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    for row in csv_reader:
        row_string = ' '.join(row)
        matches = pattern.findall(row_string)
        if matches:
            for match in matches:
                key, value = match
                results_dict[key][value] += 1


for os_name, values_dict in results_dict.items():
    for value, count in values_dict.items():
        value = value.replace("'>,",'')
        print(f'{os_name} {value} — {count}')