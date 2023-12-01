#include <iostream>
#include <iosfwd>
#include <fstream>
#include <string>

std::string strip_string(std::string str);

int main(int argc, char const *argv[])
{
    std::ifstream calibration_value("input.txt", std::ios::out);

    std::string str;
    std::string strip_str;
    int sum = 0;
    while (getline(calibration_value, str)) {
        strip_str = strip_string(str);
        sum += (int)(strip_str.at(0) - '0') * 10 + (int)(strip_str.at(strip_str.length() - 1) - '0');
    }

    std::cout << sum << '\n';

    return 0;
}

std::string strip_string(std::string str)
{
    std::string out;
    for (int i = 0; i < str.length(); i++) {
        if (isdigit(str[i])) {
            out += str[i];
        }
    }

    return out;
}
