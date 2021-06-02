#pragma once
#include "Node.h";

class Tree {
private:
	enum rotations {
		LEFT_LEFT,
		RIGHT_RIGHT,
		LEFT_RIGHT,
		RIGHT_LEFT
	};
	Node* find_min_leaf(Node* start_node, Node* min_node);
	void print(int spaces, Node* node = nullptr);
	int get_height(Node* node, int current_height);
	Node* check_balance(Node* node);
	void rotate_right(Node* root, Node* pivot);
	void rotate_left(Node* root, Node* pivot);
	/*int detect_rotate_case(Node* unbalanced_root = nullptr);*/
	Node* get_pivot(Node* unbalanced_root = nullptr);
	Node* root;
public:
	Tree();
	void add(string some_data);
	void remove(string node_data);
	Node* find(string node_data);
	Node* find_parent(Node* node, Node* current_node);
	void print_tree(int spaces);

	// IT WILL BE PRIVATE, RIGHT NOW IT'S JUST FOR TESTING
	Node* need_to_be_balanced();
	int detect_rotate_case(Node* unbalanced_root = nullptr);
	void balance_tree(Node* unbalanced_root = nullptr);
	int get_tree_height();
	~Tree();
};

