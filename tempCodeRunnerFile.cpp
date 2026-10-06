#include <iostream>
#include <string> // Required for std::string
using namespace std;

int main() {
    std::string txt = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    
    // Using .length()
    std::cout << "The length of the string is: " << [txt.length()](https://www.w3schools.com/cpp/cpp_strings_length.asp) << std::endl;
    
    // Using .size() (alias for length())
    std::cout << "The size of the string is: " << [txt.size()](https://www.w3schools.com/cpp/cpp_strings_length.asp) << std::endl;
    
    return 0;
}
