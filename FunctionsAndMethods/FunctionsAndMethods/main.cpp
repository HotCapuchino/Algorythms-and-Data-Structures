#include <iostream>
#include "functions.h"
#include "methods.h"

using namespace std;
int main(void) {
	// functions
	cout << "functions: " << endl;
	Circle circle1;
	Circle circle2;
	circle1.x = 4;
	circle1.y = 6;
	circle1.radius = 3;
	circle2.x = 3;
	circle2.y = 2;
	circle2.radius = 1;
	cout << distance_from_center_to_origin(&circle1) << endl;
	cout << distance_between_circles(&circle1, &circle2) << endl;
	cout << distance_to_X_axis(&circle2) << endl;
	cout << are_they_crossed(&circle1, &circle2) << endl;
	// methods
	cout << "methods: " << endl;
	Krug krug1 = Krug(4, 6, 3);
	Krug krug2 = Krug(3, 2, 1);
	cout << krug1.distance_from_center_to_origin() << endl;
	cout << krug1.distance_to_other_krug(krug2) << endl;
	cout << krug2.distance_to_X_axis() << endl;
	cout << krug2.are_crossed_with(krug1) << endl;
	system("pause");
}