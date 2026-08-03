#include <iostream>
using namespace std;

int main() {
  float sal, da, pf, hra, gross;
  char name[100];

  cout << "Enter name of Employee: ";
  cin >> name;

  cout << "Enter Base Salary: ";
  cin >> sal;

  da = 0.7 * sal;
  pf = 0.1 * sal;
  hra = 0.3 * sal;

  cout << "\nPaySlip:";
  cout << "\nName of Employee:  " << name;
  cout << "\nBasic Salary (INR): " << sal;
  cout << "\nDA (INR): " << da;
  cout << "\nHRA (INR): " << hra;
  cout << "\nPF( INR):" << pf;
  gross = sal + da + hra - pf;
  cout << "\nGross Salary (INR): " << gross;

  return 0;
}
