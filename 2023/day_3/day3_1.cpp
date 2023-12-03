#include <iostream>
#include <fstream>
#include <string>
#include <vector>

std::vector<std::string> matrix;

bool is_valid_char(int line, const int column)
{
    if (matrix.at(line).at(column) == '.' || isdigit(matrix.at(line).at(column))) {
        return false;
    }
    return true;
}

bool check_valid(int line, int colum)
{
    bool is_adj = false;

    // up left//
    if (line - 1 > 0 && colum + 1 < matrix.size() - 1) {
        if (is_valid_char(line - 1, colum + 1)) {
            return true;
        }
    }

    // center left
    if (line - 1 > 0) {
        if (is_valid_char(line - 1, colum)) {
            return true;
        }
    }

    // bottom left
    if (line - 1 > 0 && colum - 1 > 0) {
        if (is_valid_char(line - 1, colum - 1)) {
            return true;
        }
    }

    if (line + 1 < matrix.size() - 1 && colum + 1 < matrix.size() - 1) {
        if (is_valid_char(line + 1, colum + 1)) {
            return true;
        }
    }

    if (line + 1 < matrix.size() - 1) {
        if (is_valid_char(line + 1, colum)) {
            return true;
        }
    }

    if (line + 1 < matrix.size() - 1 && colum - 1 > 0) {
        if (is_valid_char(line + 1, colum - 1)) {
            return true;
        }
    }

    if (colum + 1 < matrix.size() - 1) {
        if (is_valid_char(line, colum + 1)) {
            return true;
        }
    }

    if (colum - 1 < matrix.size() - 1) {
        if (is_valid_char(line, colum - 1)) {
            return true;
        }
    }

    return false;
}

int main(int argc, char const* argv[])
{
    std::ifstream engine_scheme("input.txt", std::ios::out);

    std::string str;
    while (getline(engine_scheme, str)) {
        matrix.push_back(str);
    }

    int total_sum = 0;

    for (int i = 0; i < matrix.size(); i++) {
        for (int j = 0; j < matrix[i].size(); j++) {
            int count = 0, num = 0;
            bool is_valid = false;
            while (isdigit(matrix[i][j])) {
                num *= 10;
                num = num + (matrix[i][j] - '0');
                count++;

                if (check_valid(i, j)) {
                    is_valid = true;
                }
                j++;
            }
            if (is_valid) {
                total_sum += num;
            }
        }
    }

    std::cout << total_sum << std::endl;

    return 0;
}
