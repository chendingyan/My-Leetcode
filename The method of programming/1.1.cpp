//
// Created by MikeChen on 2019-04-12.
//
// abcdef -> defabc
// 方法一：暴力破解
#include <iostream>
using namespace std;
void shiftLeftOne(char* s, int n){
    char t = s[0];
    for(int i = 1; i < n; i++){
        s[i-1] = s[i];
    }
    s[n-1] = t;
}

char* leftRotateString(char *s, int n, int m){
    while(m--){
        shiftLeftOne(s, n);
    }
    return s;
}


//方法二：三步反转
void reverse(char * s, int from, int to){
    while (from < to){
        char temp = s[from];
        s[from++] = s[to];
        s[to--] = temp;
    }
}

char * solution(char*s){
    reverse(s, 0, 2);
    reverse(s, 3, 5);
    reverse(s, 0, 5);
    cout << s;

}

int main()
{
    char s[] = "abcdef";
//    char * str = leftRotateString(s, 6, 3);
//    cout << str;
    solution(s);
    return 0;
}