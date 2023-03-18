#include <iostream>
#include <algorithm>
using namespace std;

int broken[10];
int normal[10];

int map[500][500];
bool visited[500][500];

int nx[4] = { -1, 0, 1, 0 };
int ny[4] = { 0, 1, 0, -1 };

int dfs(int x, int y, int n, int m, int count) {
    count++;
    if (count == 4)
        return map[x][y];
    visited[x][y] = true;

    int result = map[x][y], temp = 0;
    int nr, nc;
    for (int i = 0; i < 4; i++) {
        nr = x + nx[i];
        nc = y + ny[i];
        if (nr >= 0 && nr < n && nc >= 0 && nc < m)
            if (!visited[nr][nc])
                temp = max(temp, dfs(nr, nc, n, m, count));
    }
    visited[x][y] = false;
    result += temp;
    return result;
}

int p(int x, int y, int n, int m) {
    if ((x == 0 && y == 0) || (x == 0 && y == m - 1) || (x == n - 1 && y == 0) || (x == n - 1 && y == m - 1))
        return 0;
    else if (x == 0)
        return map[x][y - 1] + map[x][y] + map[x][y + 1] + map[x + 1][y];
    else if (y == 0)
        return map[x - 1][y] + map[x][y] + map[x + 1][y] + map[x][y + 1];
    else if (x == n - 1)
        return map[x][y - 1] + map[x][y] + map[x][y + 1] + map[x - 1][y];
    else if (y == m - 1)
        return map[x - 1][y] + map[x][y] + map[x + 1][y] + map[x][y - 1];
    else {
        int temp = map[x - 1][y] + map[x][y] + map[x + 1][y] + map[x][y - 1] + map[x][y + 1];
        int minimum = min(map[x - 1][y], min(map[x + 1][y], min(map[x][y - 1], map[x][y + 1])));
        return temp - minimum;
    }
}

int main() {
    int n, m; cin >> n >> m;
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++)
            cin >> map[i][j];

    int maximum = 0, temp;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            temp = max(p(i, j, n, m), dfs(i, j, n, m, 0));
            maximum = max(temp, maximum);
        }
    }

    cout << maximum << endl;
    return 0;
}