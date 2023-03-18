#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
using namespace std;

int a[1000];
int b[1000];

int main() {
	int N; cin >> N;

	vector<int> v;
	fill(a, a + 1000, 1);
	for (int i = 0; i < N; i++) {
		int x; cin >> x;
		v.push_back(x);
	}

	for (int i = 0; i < N; i++)
		for (int j = 0; j < i; j++)
			if (v[i] > v[j])
				a[i] = max(a[i], a[j] + 1);

	reverse(v.begin(), v.end());
	fill(b, b + 1000, 1);
	for (int i = 0; i < N; i++)
		for (int j = 0; j < i; j++) 
			if (v[i] > v[j])
				b[i] = max(b[i], b[j] + 1);

	int result = 0;
	for (int i = 0; i < N; i++) {
		int temp = a[i] + b[N - 1 - i] - 1;
		if (result < temp)
			result = temp;
	}
	cout << result;

	return 0;
}