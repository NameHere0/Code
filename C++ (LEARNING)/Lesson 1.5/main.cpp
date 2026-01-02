#include <iostream>
#include <string>

int main()
{
    double z{5.13};
    std::string name{}; // INNITIALLIZE VARIABLE
    int x{};
    int y{};

    std::cout << "X is: " << z /*It works yipeee, and if i do: */ << std::endl;
    std::cout << "Newline yay" << std::endl; // isnt std::endl just \n?

    // After reading sum of the tutorial, i have decided to \n

    std::cout
        << "i have decided to \\n"
        << '\n';

    std::cout << "also, pick a name: (1 word)" << '\n';
    std::cin >> name;

    std::cout << "thank you, " << name << ", i will use this against you" << '\n';

    std::cout << "also insert two numbers separated by a space for sum reason" << '\n';
    std::cin >> x >> y;

    std::cout
        << "thank you for inserting " << x << " and " << y << " into me" << '\n';
}
