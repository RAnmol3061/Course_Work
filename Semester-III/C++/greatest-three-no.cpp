#include <iostream>
using namespace std;

int main() {
  int a, b, c;
  cout << "Enter value of a,b and c: ";
  cin >> a >> b >> c;

  if (a > b) {
    if (a > c)
      cout << "a is greatest no.";
    else
      cout << "c is greatest no.";
  } else {
    if (b > c)
      cout << "b is greatest no.";
    else
      cout << "c is greatest no.";
  }

  return 0;
}
