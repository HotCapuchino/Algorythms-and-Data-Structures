#pragma once
#include <string>
#include <iostream>


using namespace std;
class Node {
private:
	string data = "";
public:
	Node* left = nullptr;
	Node* right = nullptr;
	Node(string some_data);
	string getData();
	int getChildrenAmount();
	~Node();
	friend ostream& operator <<(ostream& out,  Node* node);
};

