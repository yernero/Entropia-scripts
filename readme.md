GPT 1.0.2
---

# Entropia Universe Profit Calculator

This program is a simple GUI-based application that calculates the best quantity of a given material to sell in the game Entropia Universe, given the lowest markup, amount in inventory, and total PED value of the material. The intention is to help users make decisions about the selling strategy for their materials to stay under the given markup price.

## Dependencies

This program requires Python 3.x and utilizes the following standard Python libraries:
- `tkinter` for creating the GUI.
- `pickle` for data serialization.
- `datetime` for adding timestamps to each data entry.

## Usage

1. Launch the program. A window will open prompting you to input the following:
    - Material Name
    - Lowest Markup (as a percentage)
    - Amount in Inventory
    - Total PED Value

2. After inputting your data, press the 'Calculate' button. 

3. A message box will pop up displaying the best quantity of the given material to sell in order to stay under the provided lowest markup price. 

4. The program will also record your entry, including a timestamp, in a serialized data file ('data.pkl') for future reference. This data is loaded each time the program is launched.

## Limitations

- This is a rudimentary script and does not interact with any real-world or in-game APIs or databases. The accuracy of its calculations is wholly dependent on the accuracy of the data you input.
- The file 'data.pkl' is a binary file and is not meant to be easily readable. This program does not provide a method for viewing past entries within the GUI. If you wish to view or process this data, you will need to create a separate script to deserialize ('load') the data from the file using `pickle`.
- This program does not perform extensive error checking or input validation. It expects inputs in a correct and expected format.

---