#include <iostream>
using namespace std;

int main() {
  int fact = 1, n;
  cout << "Enter n: ";
  cin >> n;
  for (int i = 1; i <= n; i++) {
    fact = fact * i;
  }
  cout << "Factorial = " << fact;
  return 0;
}
