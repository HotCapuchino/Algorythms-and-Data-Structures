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
	// auto balancing
	while (Node* unbalanced_node = need_to_be_balanced()) {
		balance_tree(unbalanced_node);
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
		if (!min_node) {
			min_node = start_node;
		} else if (min_node->getData().compare(start_node->getData()) > 0) {
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
	Node* parent = find_parent(node_to_delete, root);
	if (node_to_delete->getChildrenAmount() == 2) {
		// deleting node with two children
		Node* min_node = nullptr;
		min_node = find_min_leaf(node_to_delete, min_node);
		Node* min_leaf_parent = find_parent(min_node, node_to_delete);
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
	while (Node* unbalanced_node = need_to_be_balanced()) {
		balance_tree(unbalanced_node);
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

Node* Tree::find_parent(Node* node, Node* current_node) {
	if (node == root || !current_node) {
		return nullptr;
	}
	if (current_node->right == node || current_node->left == node) {
		return current_node;
	}
	Node* found_node = nullptr;
	found_node = find_parent(node, current_node->right);
	if (found_node) return found_node;
	found_node = find_parent(node, current_node->left);
	if (found_node) return found_node;
}

void Tree::print_tree(int spaces) {
	this->print(spaces, this->root);
}

int Tree::get_tree_height() {
	return get_height(root, 1);
}

int Tree::get_height(Node* node, int current_height) {
	if (!node) {
		return 0;
	}
	int right_height = 0;
	int left_height = 0;
	if (!node->right && !node->left) {
		return current_height;
	}
	if (node->right) {
		right_height = get_height(node->right, current_height + 1);
	}
	if (node->left) {
		left_height = get_height(node->left, current_height + 1);
	}
	return right_height <= left_height ? left_height : right_height;
}

void Tree::balance_tree(Node* unbalanced_root) {
	int rot_case = detect_rotate_case(unbalanced_root);
	Node* pivot = get_pivot(unbalanced_root);
	Node* unbalanced_root_parent = find_parent(unbalanced_root, root);
	switch (rot_case) {
		case LEFT_LEFT: {
			// works
			rotate_left(unbalanced_root, pivot);
			break;
		}
		case RIGHT_RIGHT: {
			// works
			rotate_right(unbalanced_root, pivot);
			break;
		}
		case LEFT_RIGHT: {
			// works
			rotate_right(unbalanced_root->left, get_pivot(unbalanced_root->left));
			pivot = get_pivot(unbalanced_root);
			rotate_left(unbalanced_root, pivot);
			break;
		}
		case RIGHT_LEFT: {
			// works
			rotate_left(unbalanced_root->right, get_pivot(unbalanced_root->right));
			pivot = get_pivot(unbalanced_root);
			rotate_right(unbalanced_root, pivot);
			break;
		}
		default: break;
	}
}

void Tree::rotate_left(Node* unbalanced_root, Node* pivot) {
	Node* unbalanced_root_parent = find_parent(unbalanced_root, root);
	Node* buffer = pivot->right;
	pivot->right = unbalanced_root;
	unbalanced_root->left = buffer;
	if (unbalanced_root_parent) {
		if (unbalanced_root_parent->right == unbalanced_root) {
			unbalanced_root_parent->right = pivot;
		} else {
			unbalanced_root_parent->left = pivot;
		}
	} else {
		root = pivot;
	}
}

void Tree::rotate_right(Node* unbalanced_root, Node* pivot) {
	Node* unbalanced_root_parent = find_parent(unbalanced_root, root);
	Node* buffer = pivot->left;
	pivot->left = unbalanced_root;
	unbalanced_root->right = buffer;
	if (unbalanced_root_parent) {
		if (unbalanced_root_parent->right == unbalanced_root) {
			unbalanced_root_parent->right = pivot;
		} else {
			unbalanced_root_parent->left = pivot;
		}
	} else {
		root = pivot;
	}
}

Node* Tree::get_pivot(Node* unbalanced_root) {
	int right_height = get_height(unbalanced_root->right, 1);
	int left_height = get_height(unbalanced_root->left, 1);
	return right_height > left_height ? unbalanced_root->right : unbalanced_root->left;
}

int Tree::detect_rotate_case(Node* unbalanced_root) {
	int right_height = get_height(unbalanced_root->right, 1);
	int left_height = get_height(unbalanced_root->left, 1);
	Node* pivot = get_pivot(unbalanced_root);
	int pivot_right_height = pivot->right ? get_height(pivot->right, 1) : 0;
	int pivot_left_height = pivot->left ? get_height(pivot->left, 1) : 0;
	if (left_height > right_height) {
		return pivot_left_height > pivot_right_height ? LEFT_LEFT : LEFT_RIGHT;
	} else {
		return pivot_right_height > pivot_left_height ? RIGHT_RIGHT : RIGHT_LEFT;
	}
	return 0;
}

Node* Tree::need_to_be_balanced() {
	return check_balance(root);
}

Node* Tree::check_balance(Node* node) {
	if (!node) {
		return nullptr;
	}
	int right_height = get_height(node->right, 1);
	int left_height = get_height(node->left, 1);
	if (abs(right_height - left_height) > 1) {
		return node;
	}
	Node* left_node = check_balance(node->left);
	Node* right_node = check_balance(node->right);
	if (left_node) return left_node;
	if (right_node) return right_node;
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