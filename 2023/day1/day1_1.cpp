#include <iostream>
#include <iosfwd>
#include <fstream>
#include <string>

std::string strip_string(std::string);

int main(int argc, char const *argv[]) {
    std::ifstream calibration_value("input.txt", std::ios::out);

    std::string str;
    std::string stripped_str;
    int final_sum = 0;
    while (getline(calibration_value, str)) {
        stripped_str = strip_string(str);
        final_sum += (int)(stripped_str.front() - '0') * 10 + (int)(stripped_str.back() - '0');
    }

    std::cout << final_sum << std::endl;

    return 0;
}

// strips out all non digit character
std::string strip_string(std::string str) {
    std::string out;
    for (int i = 0; i < str.length(); i++) {
        if (isdigit(str[i])) {
            out += str[i];
        }
    }

    return out;
}