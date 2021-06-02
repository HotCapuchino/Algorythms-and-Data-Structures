#include "Tree.h"

using namespace std;
int main() {
	Tree my_tree = Tree();
	my_tree.add("M");
	my_tree.add("F");
	my_tree.add("R");
	my_tree.add("P");
	my_tree.add("S");
	my_tree.add("O");
	my_tree.add("Q");
	my_tree.print_tree(1);
	my_tree.remove("R");
	my_tree.print_tree(1);
	/*cout << "\nAfter deleting leaf:\n" << endl;
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
	my_tree.printTree(1);*/
	system("pause");
}