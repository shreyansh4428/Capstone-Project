import csv

data = []

# Step 1: Read CSV file
try:
    with open("sales_capstone_dataset.csv", "r",
              encoding="utf-8-sig", newline="") as file:

        reader = csv.DictReader(file)

        print("CSV Columns:", reader.fieldnames)

        for row in reader:
            data.append(row)

except FileNotFoundError:
    print("CSV file not found! Check file location.")
    exit()

# Step 2: Check records
print("\nDataset loaded successfully!")
print("Total records:", len(data))

if len(data) == 0:
    print("Error: CSV file has no data records.")
    exit()

# Step 3: Display first 5 records
print("\nFirst 5 Records:")

for row in data[:5]:
    print(row)

# Step 4: Calculate sales
sales = [float(row["Sales"]) for row in data]

total_sales = sum(sales)
average_sales = total_sales / len(sales)
highest_sales = max(sales)

print("\n--- Sales Analysis ---")
print("Total Sales:", total_sales)
print("Average Sales:", average_sales)
print("Highest Sales:", highest_sales)

# Step 5: Simple Linear Regression
x = [float(row["Website_Visitors"]) for row in data]
y = sales

mean_x = sum(x) / len(x)
mean_y = sum(y) / len(y)

numerator = sum(
    (a - mean_x) * (b - mean_y)
    for a, b in zip(x, y)
)

denominator = sum((a - mean_x) ** 2 for a in x)

if denominator != 0:
    slope = numerator / denominator
    intercept = mean_y - slope * mean_x

    visitors = float(input("\nEnter expected website visitors: "))

    prediction = intercept + slope * visitors

    print("\n--- Sales Prediction ---")
    print("Predicted Sales:", round(prediction, 2))
else:
    print("Cannot calculate prediction.")