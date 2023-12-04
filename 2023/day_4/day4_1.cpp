#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <cmath>
#include <vector>

std::vector<std::string> get_ticket(std::string str);
std::vector<std::string> get_nums(std::string str);
int compare_arr(std::string a, std::string b);

int main(int argc, char const *argv[])
{
    std::ifstream lottery_tickets("input.txt", std::ios::out);
    std::string str;
    std::vector<std::string> winning_nums;
    std::vector<std::string> elf_nums;
    int count = 0;

    while (getline(lottery_tickets, str)) {
        winning_nums.push_back(get_ticket(str)[0]);
        elf_nums.push_back(get_ticket(str)[1]);
        count++;
    }
    int tot_sum = 0;

    for (int i = 0; i < count; i++) {
        tot_sum += compare_arr(winning_nums.at(i), elf_nums.at(i));
    }

    std::cout << tot_sum << std::endl;

    return 0;
}

int compare_arr(std::string win, std::string num)
{
    int count = 0;
    bool is_first = true;

    std::vector<std::string> win_s = get_nums(win);
    std::vector<std::string> num_s = get_nums(num);
    std::string str1, str2;
    for (std::string str1 : win_s) {
        for (std::string str2 : num_s) {
            if (str1 == str2) {
                if (is_first) {
                    count = 1;
                    is_first = false;
                } else {
                    count *= 2;
                }
            }
        }
    }

    return count;
}

std::vector<std::string> get_nums(std::string str)
{
    std::vector<std::string> nums;
    std::stringstream sstr(str);
    std::string temp;
    while (getline(sstr, temp, ' ')) {
        if (!(temp.empty())) {
            nums.push_back(temp);
        }
    }

    return nums;
}

std::vector<std::string> get_ticket(std::string str)
{
    std::string temp = str.substr(10, str.size() - 1);
    bool is_winning_num = true;
    std::vector<std::string> ticket;
    std::stringstream number_set(temp);
    while (getline(number_set, temp, '|')) {
        ticket.push_back(temp);
    }

    return ticket;
}
