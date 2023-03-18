#include <iostream>
#include <string.h>
#include <algorithm>
#include <queue>
#include <vector>
#include <limits.h>
using namespace std;

void calculation(int oper_index, vector<int>& num, vector<char>& oper) {
	int num1 = num[oper_index];
	int num2 = num[oper_index + 1];
	if (oper[oper_index] == '+')
		num[oper_index] = num1 + num2;
	else if (oper[oper_index] == '-')
		num[oper_index] = num1 - num2;
	else
		num[oper_index] = num1 * num2;
	oper.erase(oper.begin() + oper_index);
	num.erase(num.begin() + oper_index + 1);
}

int calcualtion_all(vector<int>& num, vector<char>& oper) {
	while (!oper.empty())
		calculation(0, num, oper);
	return num[0];
}

int main() {
	std::ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int N; cin >> N;
	vector<int> num;
	vector<char> oper;
	for (int i = 0; i < N; i++) {
		char x; cin >> x;
		if (i % 2 == 0) {
			int temp = x - '0';
			num.push_back(temp);
		}
		else
			oper.push_back(x);
	}

	int result = INT_MIN;
	for (int one = 0; one <= oper.size(); one++) {
		if (one == oper.size()) {
			vector<int> num_temp(num);
			vector<char>oper_temp(oper);
			int temp = calcualtion_all(num_temp, oper_temp);
			if (result < temp)
				result = temp;
		}
		for (int two = one + 2; two <= oper.size() + 1; two++) {
			if (two >= oper.size()) {
				vector<int> num_temp(num);
				vector<char>oper_temp(oper);
				calculation(one, num_temp, oper_temp);
				int temp = calcualtion_all(num_temp, oper_temp);
				if (result < temp)
					result = temp;
			}
			else {
				for (int three = two + 2; three <= oper.size() + 1; three++) {
					if (three >= oper.size()) {
						vector<int> num_temp(num);
						vector<char>oper_temp(oper);
						calculation(two, num_temp, oper_temp);
						calculation(one, num_temp, oper_temp);
						int temp = calcualtion_all(num_temp, oper_temp);
						if (result < temp)
							result = temp;
					}
					else {
						for (int four = three + 2; four <= oper.size() + 1; four++) {
							if (four >= oper.size()) {
								vector<int> num_temp(num);
								vector<char>oper_temp(oper);
								calculation(three, num_temp, oper_temp); calculation(two, num_temp, oper_temp);
								calculation(one, num_temp, oper_temp);
								int temp = calcualtion_all(num_temp, oper_temp);
								if (result < temp)
									result = temp;
							}
							else {
								for (int five = four + 2; five <= oper.size() + 1; five++) {
									if (five >= oper.size()) {
										vector<int> num_temp(num);
										vector<char>oper_temp(oper);
										calculation(four, num_temp, oper_temp); calculation(three, num_temp, oper_temp);
										calculation(two, num_temp, oper_temp); calculation(one, num_temp, oper_temp);
										int temp = calcualtion_all(num_temp, oper_temp);
										if (result < temp)
											result = temp;
									}
								}
							}
						}
					}
				}
			}
		}
	}
	cout << result;

	return 0;
}