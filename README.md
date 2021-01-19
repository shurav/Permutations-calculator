# Permutations-calculator

#include <iostream>
using namespace std;

int factorialFinder(int x)
{
    if (x==1)
    {
        return 1;
    }
    else
    {
        return x*factorialFinder(x-1);
    }
}

int permutationsCalculator(int x, int y)
{
    int n = factorialFinder(x);
    int z = factorialFinder(x-y);
    return (n/z);
}

int main()
{
    int n, k;
    cout << "This is a permutations calculator" << endl;
    cout << "Give the value for n" << endl;
    cin >> n;
    cout << "Give the value for k" << endl;
    cin >> k;
    cout << "The value of nPk is " << permutationsCalculator(n, k) << endl;
    return 0;
}
