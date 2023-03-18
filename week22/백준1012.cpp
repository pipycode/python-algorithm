#include <iostream>
#include <queue>
#include <vector>
#include <algorithm>
using namespace std;

bool visited[50][50];
vector<pair<int, int>> list[50][50];

void dfs(int x, int y);

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int T;
    cin >> T;

    for (int i = 0; i < T; i++) { // M은 가로, N은 세로, K는 배추의 개수
        int M, N, K;
        cin >> M >> N >> K;
        int** land = new int* [N];
        for (int i = 0; i < N; i++) {
            land[i] = new int[M];
            for (int j = 0; j < M; j++)
                land[i][j] = 0;
        }

        for (int i = 0; i < K; i++) {
            int x, y;
            cin >> x >> y;
            land[y][x] = 1;
            
        }

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (land[i][j] == 1) {
                    if (i != 0)
                        if (land[i - 1][j] == 1)
                            list[i][j].push_back({ i - 1, j });
                    if (j != M - 1)
                        if (land[i][j + 1] == 1)
                            list[i][j].push_back({ i, j + 1 });
                    if (i != N - 1)
                        if (land[i + 1][j] == 1)
                            list[i][j].push_back({ i + 1, j });
                    if (j != 0)
                        if (land[i][j - 1] == 1)
                            list[i][j].push_back({ i, j - 1 });
                }
            }
        }

        int num = 0;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (land[i][j] == 1 && !visited[i][j]) {
                    dfs(i, j);
                    num++;
                }
            }
        }
        cout << num << endl;

        for (int i = 0; i < 50; i++) {
            for (int j = 0; j < 50; j++) {
                list[i][j].clear();
                visited[i][j] = false;
            }
        }

        for (int i = 0; i < N; i++)
            delete[] land[i];
        delete[] land;
    }
    return 0;
}

void dfs(int x, int y) {
    visited[x][y] = true;
    for (int i = 0; i < list[x][y].size(); i++) {
        pair<int, int> next_visit = list[x][y][i];
        if (!visited[next_visit.first][next_visit.second]) {
            visited[next_visit.first][next_visit.second] = true;
            dfs(next_visit.first, next_visit.second);
        }
    }
}