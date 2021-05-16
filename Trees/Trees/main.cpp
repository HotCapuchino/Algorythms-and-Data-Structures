#include "Tree.h"

using namespace std;
int main() {
	Tree my_tree = Tree();
	my_tree.add("M");
	my_tree.add("B");
	my_tree.add("G");
	my_tree.add("K");
	my_tree.add("R");
	my_tree.printTree(1);
	my_tree.remove("K");
	cout << "\nAfter deleting leaf:\n" << endl;
	my_tree.printTree(1);
	my_tree.add("K");
	cout << "\nAdded K again:\n" << endl;
	my_tree.printTree(1);
	my_tree.remove("G");
	cout << "\nAfter deleting node with one child:\n" << endl;
	my_tree.printTree(1);
	my_tree.add("A");
	my_tree.add("L");
	cout << "\nAdded some nodes:\n" << endl;
	my_tree.printTree(1);
	my_tree.remove("B");
	cout << "\nAfter deleting node with 2 child:\n" << endl;
	my_tree.printTree(1);
	system("pause");
}