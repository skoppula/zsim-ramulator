#include <iostream>
#include "zsim_hooks.h"

using namespace std;

int main() {
    cout << "C++ test" << endl;
    zsim_roi_begin();
    zsim_heartbeat();
    zsim_PIM_function_begin();
    zsim_PIM_function_end();    
    zsim_roi_end();
    cout << "C++ test done" << endl;
    return 0;
}
