"""
Inventory management system for tracking stock items.

This module provides functions to add, remove, and manage inventory items,
as well as load/save data to JSON files.
"""
import json
from datetime import datetime


class InventorySystem:
    """A class to manage inventory stock data."""

    def __init__(self):
        """Initialize the inventory system with empty stock data."""
        self.stock_data = {}

    def add_item(self, item="default", qty=0, logs=None):
        """Add an item to the inventory."""
        if logs is None:
            logs = []
        if not item:
            return
        self.stock_data[item] = self.stock_data.get(item, 0) + qty
        logs.append(f"{datetime.now()}: Added {qty} of {item}")

    def remove_item(self, item, qty):
        """Remove a specified quantity of an item from inventory."""
        try:
            self.stock_data[item] -= qty
            if self.stock_data[item] <= 0:
                del self.stock_data[item]
        except KeyError:
            pass

    def get_qty(self, item):
        """Get the current quantity of an item in inventory."""
        return self.stock_data[item]

    def load_data(self, file="inventory.json"):
        """Load inventory data from a JSON file."""
        with open(file, "r", encoding="utf-8") as f:
            self.stock_data = json.load(f)

    def save_data(self, file="inventory.json"):
        """Save inventory data to a JSON file."""
        with open(file, "w", encoding="utf-8") as f:
            json.dump(self.stock_data, f)

    def print_data(self):
        """Print a report of all items in inventory."""
        print("Items Report")
        for item in self.stock_data:
            print(item, "->", self.stock_data[item])

    def check_low_items(self, threshold=5):
        """Check for items below the specified threshold quantity."""
        result = []
        for item in self.stock_data:
            if self.stock_data[item] < threshold:
                result.append(item)
        return result


def main():
    """Execute main inventory operations for demonstration."""
    inventory = InventorySystem()
    inventory.add_item("apple", 10)
    inventory.add_item("banana", -2)
    inventory.add_item(123, "ten")
    inventory.remove_item("apple", 3)
    inventory.remove_item("orange", 1)
    print("Apple stock:", inventory.get_qty("apple"))
    print("Low items:", inventory.check_low_items())
    inventory.save_data()
    inventory.load_data()
    inventory.print_data()
    print('Direct print instead of eval')


main()
