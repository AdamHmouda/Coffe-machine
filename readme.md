# Coffee Machine

This is a Python script for a basic coffee machine implemented using the `tkinter` module. The script allows the user to order coffee by choosing from a predefined menu, enter the amount of money, and process the payment. The coffee machine checks whether there are enough resources available to make the requested coffee and updates the resources' stock and profit after a successful order.

## Usage

1. Run the script in a Python environment.
2. Enter one of the following options:
    * `espresso`
    * `latte`
    * `cappuccino`
    * `off` to turn off the machine
    * `report` to print the `resources stock` and the `total profit`
    * `restock` to refill the machine's resources
3. If a valid choice is made, the program displays the price of the chosen drink.
4. Enter the amount of money (in USD) and press the `Process` button.
5. If the payment is insufficient, the machine refunds the money.
6. If the payment is sufficient, the machine dispenses the drink and updates the resources' stock and profit.

## Dependencies

This script requires the `tkinter` module, which is included in most Python distributions. No additional packages need to be installed.

## Menu and Resources

The menu and resources are defined at the beginning of the script as Python dictionaries. The menu consists of three drinks (`espresso`, `latte`, and `cappuccino`), each with its cost and required ingredients. The resources dictionary defines the initial stock of resources available to make the drinks. The `stock` dictionary is a copy of the `resources` dictionary used to refill the machine's resources on command.