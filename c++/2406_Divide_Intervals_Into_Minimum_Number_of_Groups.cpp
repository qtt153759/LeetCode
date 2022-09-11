#include<bits/stdc++.h>
using namespace std;
int minGroups(vector<vector<int>>& ints) {
    sort(begin(ints), end(ints));
    priority_queue<int, vector<int>, greater<int>> pq;
    for (const auto &i : ints) {
        printf("%d - %d\n",i[0],i[1]);
        if (!pq.empty() && pq.top() < i[0])
            pq.pop();
        pq.push(i[1]);
    }
    return pq.size();
}
int main(){
  vector<vector<int>> ints={{5,10},{6,8},{1,5},{2,3},{1,10}};
  printf("%d",minGroups(ints));
}