#include <iostream>
#include <string.h>
#include <algorithm>
#include <queue>
#include <vector>
using namespace std;

#define INF 1e18

vector<pair<int, int>> v[501];
long long int Node_time[501];

bool bellman(int start, int Node_num) {
	Node_time[start] = 0;
	bool check;
	for (int i = 1; i <= Node_num; i++) {
		check = false;
		for (int Node = 1; Node <= Node_num; Node++) {
			// 선택한 노드까지의 최소거리를 측정할 수 없으면 일단 넘어감
			//if (Node_time[Node] == INF)
			//	continue;
			// 최소거리가 갱신되어 있을 경우 연결된 노드들에 대해 모두 갱신해줌
			for (int edge = 0; edge < v[Node].size(); edge++) {
				int next_Node = v[Node][edge].second;
				int now_next_cost = v[Node][edge].first;
				if (Node_time[next_Node] > Node_time[Node] + now_next_cost) {
					Node_time[next_Node] = Node_time[Node] + now_next_cost;
					check = true;
				}
			}
		}
		if (!check)
			break;
	}
	// 한번 더 돌렸을 때(i=Node_num) 바뀐거면 true, 안바뀌면 false;
	if (check)
		return true;
	else
		return false;
}

int main() {
	std::ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int TC; cin >> TC;
	for (int test = 0; test < TC; test++) {
		int N, M, W; cin >> N >> M >> W;	// N:노드수, M:간선수, W:웜홀수
		for (int edge = 0; edge < M; edge++) {
			int start, end, time; cin >> start >> end >> time;
			v[start].push_back({ time, end });
			v[end].push_back({ time, start });
		}
		for (int hole = 0; hole < W; hole++) {
			int start, end, time; cin >> start >> end >> time;
			v[start].push_back({ -time, end });
		}
		fill(Node_time, Node_time + 501, INF);

		bool check = bellman(1, N);

		if (check)
			cout << "YES\n";
		else
			cout << "NO\n";

		for (int i = 1; i <= N; i++)
			v[i].clear();
	}
	return 0;
}
