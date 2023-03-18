#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;

vector<int> rule[1001]; // cost, 도착지
int time_cost[1001];
int final_time_cost[1001];

bool non_rute[1001];

int bfs(int start, int success) {
    queue<int> q;
    q.push(start);
    int size1, size2, cost;
    while (!q.empty()) {
        size1 = q.size();
        for (int i = 0; i < size1; i++) {
            int f = q.front();
            q.pop();
            size2 = rule[f].size();
            for (int j = 0; j < size2; j++) {
                int n = rule[f][j];
                int cost = final_time_cost[f] + time_cost[n];
                if (final_time_cost[n] < cost) {
                    final_time_cost[n] = cost;
                    q.push(n);
                }
            }
        }
    }
    return final_time_cost[success];
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int T;
    int n, k, x, y, success;
    cin >> T;
    while (T--) {
        cin >> n >> k;
        for (int i = 1; i <= n; i++)
            cin >> time_cost[i];
        for (int i = 0; i < k; i++) {
            cin >> x >> y;
            rule[x].push_back(y);
            non_rute[y] = true;
        }
        cin >> success;
        for (int i = 1; i <= n; i++)
            if (!non_rute[i])
                rule[0].push_back(i);

        cout << bfs(0, success) << "\n";

        for (int i = 0; i <= 1000; i++) {
            rule[i].clear();
            time_cost[i] = 0;
            final_time_cost[i] = 0;
            non_rute[i] = false;
        }
    }
    return 0;
}