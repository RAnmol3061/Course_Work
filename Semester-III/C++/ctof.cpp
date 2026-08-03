#include <iostream>
using namespace std;

int main() {
  float c, f;

  cout << "Enter Temperature in C: ";
  cin >> c;

  f = 1.8 * c + 32;
  cout << "Temperature in F: " << f;
  return 0;
}
