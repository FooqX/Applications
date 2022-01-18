#include <iostream>
#include <string>
using namespace std;

int main() {
    cout << "How many cars do you have?\n";

    unsigned int carCount;
    cin >> carCount;

    if(cin.fail()) {
        cout << "\nError: Failed to get integer from input.\n";
        cin.clear();
        cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');

        cout << "Press ENTER key to exit the program.";
        getchar();
        exit(0);
    }

    if(carCount == 0) {
        cout << "\nNo cars found.\n";

        cout << "Press ENTER key to exit the program.";
        getchar();
        exit(0);
    }
    string *garage = new string[carCount];

    cin.ignore();
    cout << "\n";

    // Assigning cars to garage
    for(unsigned int i = 0; i < carCount; i++) {
        cout << "Enter car #" << i + 1 << ": ";
        getline(cin, garage[i]);
    }

    // Outputing cars
    cout << "\n--- Garage ---" << endl;
    for(unsigned int i = 0; i < carCount; i++) {
        cout << "Car #" << i + 1 << ": " << garage[i] << '\n';
    }
    cout << "--------------\n";

    // Exiting program
    cout << "Press ENTER key to exit the program.";
    getchar();


    return 0;
}
