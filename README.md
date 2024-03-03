# PythonPrograms
# 1. Receipt Generator

This Python script generates a receipt in PDF format using ReportLab library. It prompts the user to input data for each row of the receipt, including date, name, subscription, and price for multiple items. It then calculates subtotal, applies discount provided by the user, and calculates the total amount.

## Description of the Code

The script consists of the following key components:

1. **User Input**: It prompts the user to input data for each row of the receipt, such as date, name, subscription, and price for multiple items. It also prompts for the discount amount.

2. **Table Creation**: It creates a table with the entered data, including date, name, subscription, and price for each item. It also calculates the subtotal, applies the discount, and calculates the total amount.

3. **PDF Generation**: Using ReportLab library, it generates a PDF document containing the receipt information in tabular format. The PDF includes headings, table borders, and styling for better presentation.

4. **Output**: The generated PDF is saved as "receipt.pdf".

# 2. Password Generator

This Python program generates a strong password based on user-defined criteria. It prompts the user to specify the number of characters they want in their password, ensuring it's at least 8 characters long. Then, it creates a password consisting of lowercase letters, uppercase letters, digits, and punctuation marks. 

## Description of the Program

The program performs the following steps:

1. **User Input**: It prompts the user to enter the number of characters they want in their password.

2. **Validation**: It validates the user input to ensure it's a number and at least 8 characters long. If the input is invalid, it prompts the user to enter the number again.

3. **Password Generation**: It generates a strong password using a combination of lowercase letters, uppercase letters, digits, and punctuation marks. The password contains 60% letters and 40% digits/punctuations.

4. **Output**: It prints the generated strong password to the console.

# 3. Meal Order System (Simple)

This Python program is a Meal Ordering App that allows users to create a menu, select items to order, and generate a bill with a QR code for payment. 

## Description of the Program

The program includes the following functionalities:

1. **Menu Submission**: Users can submit menu items and their prices. The menu is stored as a dictionary.

2. **Country Selection**: Users can select their country, and the program will determine the currency based on the country code entered using ISO 3166-1 alpha-2 standard.

3. **Ordering Process**: Users can select items from the menu to order. The program validates the user's input and adds the selected items to the order.

4. **Bill Generation**: After completing the order, the program generates a bill with order details, including item names, prices, and the total amount in the selected currency.

5. **QR Code Generation**: The program generates a QR code for the bill, enabling easy payment processing.

6. **Execution**: The main function orchestrates the flow of the program, prompting users for inputs and displaying outputs accordingly.
