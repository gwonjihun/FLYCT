#include <iostream>
using namespace std;

int chars[26];

int main() {
  int n;
  cin >> n;
  int result = 0;
  
  for (int i = 0; i<n; i++) { 
    string s; 
    cin >> s;
    bool check = true;

    int chars[26] = {};
    for (int j = 0; j<s.length(); j++){
      if (s[j] != s[j-1] && chars[s[j]-'a'] != 0){
        check = false;
        break;
      }
      chars[s[j] -'a']++;
    }

    if (check == true)
      result++;
  }

  cout << result;
}