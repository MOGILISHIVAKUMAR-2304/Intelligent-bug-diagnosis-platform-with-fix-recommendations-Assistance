import csv

input_file = "data/raw/historical_defects.csv"
output_file = "cleaned_historical_defects.csv"

with open(input_file, "r", encoding="utf-8") as file:
    reader = csv.reader(file)
    rows = list(reader)

header = rows[0]
data = rows[1:]

cleaned_data = []
seen = set()

for row in data:
    row = [value.strip() for value in row]

    row_key = tuple(row)

    if row_key not in seen:
        seen.add(row_key)
        cleaned_data.append(row)
with open(output_file, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(header)
    writer.writerows(cleaned_data)

print("Dataset cleaned successfully!")
print("Records:", len(cleaned_data))