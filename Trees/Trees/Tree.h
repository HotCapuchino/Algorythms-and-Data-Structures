#pragma once
#include "Node.h";

class Tree {
private:
	Node* find_min_leaf(Node* start_node, Node* min_node);
	void print(int spaces, Node* node = nullptr);
public:
	Node* root;
	Tree();
	void add(string some_data);
	void remove(string node_data);
	Node* find(string node_data);
	Node* findParent(Node* node, Node* current_node);
	void printTree(int spaces);
	~Tree();
};

