#include <iostream>
#include <stack>
#include <string>
#include <cctype>
using namespace std;
bool checkBieuThuc(const string& expr) {
    stack<char> s;
    for (char ch : expr) {
        if (ch == '(') {
            s.push(ch);
        } else if (ch == ')') {
            if (s.empty()) return false;
            s.pop();
        }
    }
    return s.empty();
}
bool checkGiaTri(const string& expr, bool A, bool B, bool C) {
    stack<bool> s;
    for (int i = expr.size() - 1; i >= 0; --i) {
        char ch = expr[i];
        if (isspace(ch)) continue; 
        if (ch == 'A') {
            s.push(A);
        } else if (ch == 'B') {
            s.push(B);
        } else if (ch == 'C') {
            s.push(C);
        } else if (ch == '-') {
            bool val = s.top(); s.pop();
            s.push(!val); 
        } else if (ch == '∧' || ch == '∨' || ch == '->') {
            bool left = s.top(); s.pop();
            bool right = s.top(); s.pop();
            if (ch == '∧') {
                s.push(left && right); 
            } else if (ch == 'V') {
                s.push(left || right); 
            } else if (ch == '→') {
                s.push(!left || right); 
            }
        }
    }
    return s.top();
}
int main() {
    string expression;
    cout << "Nhap bieu thuc logic: ";
    getline(cin, expression);
    if (!checkBieuThuc(expression)) {
        cout << "Bieu thuc khong hop le!" << endl;
        return 1;
    }
    bool A, B, C;
    cout << "Nhap gia tri cho bien A (0/1): ";
    cin >> A;
    cout << "Nhap gia tri cho bien B (0/1): ";
    cin >> B;
    cout << "Nhap gia tri cho bien C (0/1): ";
    cin >> C;
    bool result = checkGiaTri(expression, A, B, C);
    cout << "Ket qua bieu thuc: " << (result ? "True" : "False") << endl;

    return 0;
}
