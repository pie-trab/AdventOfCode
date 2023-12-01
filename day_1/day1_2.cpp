#include <iostream>
#include <iosfwd>
#include <fstream>
#include <string>
#include <vector>
#include <climits>

std::string strip_string(std::string str);
void strip_letteral_numbers(std::string& temp);

int main(int argc, char const* argv[])
{
    std::ifstream calibration_value("input.txt", std::ios::out);

    std::string str;
    std::string strip_str;
    int sum = 0;
    int i = 1;
    std::vector<int> first_;
    std::vector<int> second_;

    while (getline(calibration_value, str)) {
        strip_letteral_numbers(str);
        strip_str = strip_string(str);
        sum += (int)(strip_str.at(0) - '0') * 10 + (int)(strip_str.at(strip_str.length() - 1) - '0');
        i++;
    }

    calibration_value.close();

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

void strip_letteral_numbers(std::string& str)
{
    std::vector<std::string> s = {"one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};

    for (int i = 0; i < s.size(); i++) {
        while (str.find(s.at(i)) != std::string::npos) {
            str.replace(str.find(s.at(i)), s.at(i).length(), s.at(i).at(0) + std::to_string(i + 1) + s.at(i).at(s.at(i).length() - 1));
        }
    }

    /*
    for (int i = 0; i < s.size(); i++) {
        while (str.find(s.at(i)) != std::string::npos) {
            // td::cout << std::to_string(i + 1) + s.at(i).at(s.at(i).length() - 1) << '\n';

            str.replace(str.find(s.at(i)), s.at(i).length(), std::to_string(i + 1) + s.at(i).at(s.at(i).length() - 1));
        }
    }
    */

    std::cout << str << '\n';
}
