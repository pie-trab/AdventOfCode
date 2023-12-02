#include <iostream>
#include <iosfwd>
#include <fstream>
#include <string>
#include <vector>
#include <sstream>

const int MAX_RED = 12, MAX_GREEN = 13, MAX_BLUE = 14;
void format_string(std::string&);
bool count_cubes(std::string& str);

int main(int argc, char const* argv[])
{
    std::ifstream game_list("input.txt", std::ios::out);
    std::string str;
    int count = 0, i = 1;
    bool is_valid = false;

    while (getline(game_list, str)) {
        format_string(str);
        str = str + ";";
        std::stringstream ss(str);
        std::string part;
        is_valid = true;

        while (getline(ss, part, ';') && is_valid) {
            is_valid = count_cubes(part);
        }

        if (is_valid) {
            std::cout << "i: " << i << '\n';
            count += i;
        }
        i++;
    }

    std::cout << count << std::endl;

    return 0;
}

void format_string(std::string& str)
{
    str = str.substr(str.find(':') + 1, str.length() - 1);
}

bool count_cubes(std::string& str)
{
    int red{0}, green{0}, blue{0};
    if (str.find("red") != std::string::npos) {
        red = stoi(str.substr(str.find("red") - 3, 2));
    }

    if (str.find("green") != std::string::npos) {
        green = stoi(str.substr(str.find("green") - 3, 2));
    }

    if (str.find("blue") != std::string::npos) {
        blue = stoi(str.substr(str.find("blue") - 3, 2));
    }

    return (red <= MAX_RED && green <= MAX_GREEN && blue <= MAX_BLUE);
}
