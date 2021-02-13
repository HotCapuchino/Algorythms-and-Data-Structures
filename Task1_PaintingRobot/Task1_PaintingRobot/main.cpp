#include "Field.h"

using namespace std;
int main(void) {
	int field_size = 0;
	cout << "Enter size of the field: ";
	cin >> field_size;
	Field field = Field(field_size);
	cout << "Before:\n";
	field.printField();
	field.paintField();
	cout << "After:\n";
	field.printField();
	system("pause");
}