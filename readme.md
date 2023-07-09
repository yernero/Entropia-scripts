# Entropia Universe Profit Calculator

## GPT v1.0.4

This program is a simple GUI-based application that calculates the maximum quantity of a given material to sell in the game Entropia Universe, given the lowest markup, amount in inventory, and total PED value of the material. The intention is to help users make decisions about the selling strategy for their materials to stay under the given markup price and maximize their profits.

## Dependencies

This program requires Python 3.x and utilizes the following standard Python libraries:
- `tkinter` for creating the GUI.
- `shelve` for persistent dictionary-like data storage.
- `datetime` for adding timestamps to each data entry.

## Usage

1. Launch the program. A window will open prompting you to input the following:
    - Material Name
    - Lowest Markup (as a percentage)
    - Amount in Inventory
    - Total PED Value

2. After inputting your data, press the 'Calculate' button. 

3. A message box will pop up displaying the maximum quantity of the given material to sell in order to stay under the provided lowest markup price. This message will also provide a detailed explanation of the calculations, including the average material price, the target selling price under the given markup, and the maximum quantity to sell.

4. The program will also record your entry, including a timestamp, in a persistent data storage for future reference. This data is loaded each time the program is launched.

## Limitations

- This is a rudimentary script and does not interact with any real-world or in-game APIs or databases. The accuracy of its calculations is wholly dependent on the accuracy of the data you input.
- The data storage uses Python's `shelve` module, which creates a binary file ('data.db') and is not meant to be easily readable. This program does not provide a method for viewing past entries within the GUI. If you wish to view or process this data, you will need to create a separate script to extract ('load') the data from the file using `shelve`.
- This program does not perform extensive error checking or input validation. It expects inputs in a correct and expected format.

## Changes

### GPT v1.0.4
- Added a detailed explanation of calculations in the output message. Now the program provides the average material price, the target selling price under the given markup, and the maximum quantity to sell. This helps to clarify the calculations being done within the program.

### GPT v1.0.3
- Updated the quantity calculation logic to correctly take into account the total PED value of the materials.

### GPT v1.0.2
- Created a GUI interface to take user inputs and display the maximum quantity of a material to sell.

### GPT v1.0.1
- The initial version of the script that calculated the maximum quantity of a material to sell given the lowest markup, amount in inventory, and total PED value of the material.

---
