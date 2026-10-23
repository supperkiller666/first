#include <bits/stdc++.h>
using namespace std;
struct fat{
    int first,second;
    fat():first(0),second(0)
    {}
    bool operator <(const fat& other)const{
        return(tie(first,second)<tie(other.first,other.second));
    }
};
int main()
{   ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int s,n,x,y,pwr;
    cin>>s>>n;
    pwr=s;
    vector <fat> need;
    for(int i =0;i<n;++i){
        cin>>x>>y;
        fat xy;
        xy.first=x;
        xy.second=y;
        need.push_back(xy);
    }
    sort(need.begin(), need.end());
        for (int j=0;j<need.size();++j) {
        if (pwr<=need[j].first){
            cout<<"NO";
            return 0;
        }else{
        pwr+=need[j].second;
        }
    }
    cout<<"YES";
    return 0;
}
