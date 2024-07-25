#include <iostream>
#include <iosfwd>
#include <fstream>
#include <string>
#include <vector>
#include <sstream>

void format_string(std::string&);
int count_red(std::string& str);
int count_green(std::string& str);
int count_blue(std::string& str);

int main(int argc, char const* argv[]) {
    std::ifstream game_list("input.txt", std::ios::out);
    std::string str;
    int count = 0;

    while (getline(game_list, str)) {
        format_string(str);
        str = str + ";";
        std::stringstream ss(str);
        std::string part;
        int red{1}, green{1}, blue{1};

        while (getline(ss, part, ';')) {
            count_red(part) >= red ? red = count_red(part) : red = red;
            count_green(part) >= green ? green = count_green(part) : green = green;
            count_blue(part) >= blue ? blue = count_blue(part) : blue = blue;
        }

        count += red * green * blue;
    }

    std::cout << count << std::endl;

    return 0;
}

void format_string(std::string& str) {
    str = str.substr(str.find(':') + 1, str.length() - 1);
}

int count_red(std::string& str) {
    if (str.find("red") != std::string::npos) {
        return stoi(str.substr(str.find("red") - 3, 2));
    }
    return 0;
}

int count_green(std::string& str) {
    if (str.find("green") != std::string::npos) {
        return stoi(str.substr(str.find("green") - 3, 2));
    }
    return 0;
}
int count_blue(std::string& str) {
    if (str.find("blue") != std::string::npos) {
        return stoi(str.substr(str.find("blue") - 3, 2));
    }
    return 0;
}
