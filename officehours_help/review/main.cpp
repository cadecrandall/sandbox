#include <iostream>
#include <vector>
using namespace std;

int main() {
    // EVEN feet & heads --> Charmed        level = f * h
    // ODD feet & heads --> Special         level = f + h
    // OTHERWISE odd/even feet & even/odd heads --> Mystical
    //      max(f,h)
    // IMPOSSIBLE: f or h == 0 DONE
    int f, h;
    cin >> f >> h;

    if (f == 0 || h == 0) {
        // not possible
        cout << "Not Possible";
        return 0;
    } else if (f % 2 == 0 && h % 2 == 0) {
        // Charmed
        int level = f * h;
        cout << "Charmed " << level;
    } else if (f % 2 == 1 && h % 2 == 1) {
        // Special
        int level = f + h;
        cout << "Special " << level;
    } else {
        // Mystical
        int level;
        if (f > h) {
            level = f;
        } else {
            level = h;
        }
        cout << "Mystical " << level;
    }
    return 0;
}
