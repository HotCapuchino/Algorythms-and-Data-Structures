#include "Tree.h";
#include <vector>;

using namespace std;
Tree::Tree() {}

void Tree::add(string some_data) {
	Node* node = new Node(some_data);
	if (root == nullptr) {
		root = node;
		return;
	}
	Node* current_node = root;
	Node* previous_node = current_node;
	bool is_right = false;
	while(true) {
		previous_node = current_node;
		if (current_node->getData().compare(some_data) > 0) {
			current_node = current_node->left;
			is_right = false;
		} else {
			current_node = current_node->right;
			is_right = true;
		}
		if (current_node == nullptr) {
			current_node = node;
			if (is_right) {
				previous_node->right = current_node;
			}
			else {
				previous_node->left = current_node;
			}
			break;
		}
	}
}

Node* Tree::find_min_leaf(Node* start_node, Node* min_node) {
	if (start_node->left) {
		min_node = find_min_leaf(start_node->left, min_node);
	} 
	if (start_node->right) {
		min_node = find_min_leaf(start_node->right, min_node);
	}
	if (!start_node->left && !start_node->right) {
		if (min_node->getData().compare(start_node->getData()) > 0) {
			min_node = start_node;
		}
	}
	return min_node;
}

void Tree::remove(string node_data) {
	Node* node_to_delete = this->find(node_data);
	if (!node_to_delete) {
		cout << "Node with such value doesn't exist!" << endl;
		return;
	}
	Node* parent = findParent(node_to_delete, root);
	if (node_to_delete->getChildrenAmount() == 2) {
		// deleting node with two children
		Node* min_node = root;
		min_node = find_min_leaf(node_to_delete, min_node);
		Node* min_leaf_parent = findParent(min_node, node_to_delete);
		// changing pointer of parent elem (moving elem)
		if (parent->left == node_to_delete) {
			parent->left = min_node;
		} else {
			parent->right = min_node;
		}
		// changing pointer of parent of min leaf in order not to cause infinite loop
		if (min_leaf_parent->left == min_node) {
			min_leaf_parent->left = nullptr;
		} else {
			min_leaf_parent->right = nullptr;
		}
		min_node->right = node_to_delete->right;
		min_node->left = node_to_delete->left;
	} else if (node_to_delete->getChildrenAmount() == 0) {
		// deleting leaf
		if (parent->left == node_to_delete) {
			parent->left = nullptr;
		} else {
			parent->right = nullptr;
		}
		node_to_delete->~Node();
	} else if (node_to_delete->getChildrenAmount() == 1) {
		// deleting node with one child
		if (node_to_delete->right) {
			parent->right = node_to_delete->right;
		} else {
			parent->left = node_to_delete->left;
		}
	}
}

Node* Tree::find(string node_data) {
	if (root == nullptr) {
		cout << "Please, insert at least one node to your tree!" << endl;
		return nullptr;
	}
	Node* current_node = root;
	while(true) {
		if (current_node->getData().compare(node_data) > 0) {
			current_node = current_node->left;
		} else if (current_node->getData().compare(node_data) < 0) {
			current_node = current_node->right;
		} else {
			return current_node;
		}
		if (!current_node) {
			return nullptr;
		}
	}
}

Node* Tree::findParent(Node* node, Node* current_node) {
	if (node == root || !current_node) {
		return nullptr;
	}
	if (current_node->right == node || current_node->left == node) {
		return current_node;
	}
	Node* found_node = nullptr;
	found_node = findParent(node, current_node->right);
	if (found_node) return found_node;
	found_node = findParent(node, current_node->left);
	if (found_node) return found_node;
}

void Tree::printTree(int spaces) {
	this->print(spaces, this->root);
}

void Tree::print(int spaces, Node* node) {
	int i = spaces;
	if (node) {
		this->print(spaces + 1, node->right);
		while (i > 0) {
			printf("\t");
			i--;
		}
		cout << node->getData() << endl;
		this->print(spaces + 1, node->left);
	}
}


Tree::~Tree() {
	delete root;
}