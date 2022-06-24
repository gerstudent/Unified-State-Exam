/*
    Напишите программу, которая ищет среди целых чисел, принадлежащих
    числовому отрезку [185311;185330], числа, имеющие ровно четыре
    различных натуральных делителя. Для каждого найденного числа запишите
    эти четыре делителя в четыре соседних столбца на экране с новой строки.
    Делители в строке должны следовать в порядке возрастания.
*/

#include <algorithm>
#include <cmath>
#include <iostream>
#include <vector>
using namespace std;

vector<int> fdividers(int x) {
  vector<int> dividers;
  for (int i = 1; i <= sqrt(x); i++) {
    if (x % i == 0) {
      dividers.push_back(i);
      if (i * i != x) {
        dividers.push_back(x / i);
      }
    }
  }
  return dividers;
}

int main() {
  for (int i = 185311; i <= 185330; ++i) {
    vector<int> divs = fdividers(i);
    if (divs.size() == 4) {
      sort(divs.begin(), divs.end());
      for (int div : divs) {
        cout << div << ' ';
      }
      cout << '\n';
    }
  }
  return 0;
}
