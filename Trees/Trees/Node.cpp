#include "Node.h";


Node::Node(string some_data) {
	data = some_data;
}

string Node::getData() {
	return data;
}

int Node::getChildrenAmount() {
	return (left ? 1 : 0) + (right ? 1 : 0);
}

Node::~Node() {
	delete left;
	delete right;
}
