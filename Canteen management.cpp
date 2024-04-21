#include <iostream>
#include <string>
#include <vector>

using namespace std;

// Define a struct for menu items
struct MenuItem {
    string name;
    double price;
    int quantity;
};

// Define a class for the canteen management system
class CanteenManager {
private:
    vector<MenuItem> menu;

public:
    // Constructor to initialize the menu
    CanteenManager() {
        // Add some initial menu items
        menu.push_back({"Coffee", 1.5, 10});
        menu.push_back({"Sandwich", 3.0, 15});
        menu.push_back({"Pizza", 5.0, 20});
    }

    // Function to display the menu
    void displayMenu() {
        cout << "Menu:\n";
        for (const auto& item : menu) {
            cout << item.name << " - $" << item.price << " (" << item.quantity << " available)\n";
        }
    }

    // Function to process an order
    void processOrder(const string& itemName, int quantity) {
        for (auto& item : menu) {
            if (item.name == itemName) {
                if (item.quantity >= quantity) {
                    cout << "Order placed: " << quantity << " x " << itemName << "\n";
                    item.quantity -= quantity;
                    return;
                } else {
                    cout << "Insufficient quantity of " << itemName << " available.\n";
                    return;
                }
            }
        }
        cout << "Item not found in the menu.\n";
    }
};

int main() {
    CanteenManager canteen;

    // Display the menu
    canteen.displayMenu();

    // Example orders
    canteen.processOrder("Coffee", 2);
    canteen.processOrder("Sandwich", 1);
    canteen.processOrder("Pizza", 3);

    // Display the updated menu
    canteen.displayMenu();

    return 0;
}