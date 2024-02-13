from reportlab.platypus import SimpleDocTemplate, Table, Paragraph, TableStyle
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet

# Function to get user input for a table row
def get_user_input():
    date = input("Enter Date: ")
    name = input("Enter Name: ")
    subscription = input("Enter Subscription: ")
    price = float(input("Enter Price (Rs.): "))  # Convert price to float
    return [date, name, subscription, price]

# Get the number of rows from the user
num_rows = int(input("Enter the number of rows to add to the receipt: "))

# Get user input for each row in the table
data_rows = []
subtotal = 0

for _ in range(num_rows):
    row_data = get_user_input()
    data_rows.append(row_data)
    subtotal += row_data[-1]  # Accumulate the prices for subtotal

discount = float(input("Enter Discount (Rs.): "))  # Get user input for discount

# Calculate total after applying discount
total = subtotal - discount

# Create the table data including subtotal, discount, and total
table_data = [
    ["Date", "Name", "Subscription", "Price (Rs.)"],
] + data_rows + [
    ["Sub Total", "", "", subtotal],
    ["Discount", "", "", discount],
    ["Total", "", "", total],
]

# Determine the number of columns based on the first row
num_columns = len(table_data[0])

# Creating a Base Document Template of page size A4
pdf = SimpleDocTemplate("receipt.pdf", pagesize=A4)

# Standard stylesheet defined within ReportLab itself
styles = getSampleStyleSheet()

# Fetching the style of Top-level heading (Heading1)
title_style = styles["Heading1"]
title_style.alignment = 1  # 0: left, 1: center, 2: right

# Creating the paragraph with the heading text and passing the styles
title = Paragraph("Receipt", title_style)

# Creates a Table Style object and defines the styles row-wise
style = TableStyle(
    [
        ("BOX", (0, 0), (-1, -1), 1, colors.black),
        ("GRID", (0, 0), (-1, -1), 1, colors.black),
        ("BACKGROUND", (0, 0), (num_columns - 1, 0), colors.gray),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ("BACKGROUND", (0, 1), (-1, -1), colors.beige),
    ]
)

# Creates a table object and passes the style to it
table = Table(table_data, style=style)

# Final step which builds the actual PDF putting together all the elements
pdf.build([title, table])
