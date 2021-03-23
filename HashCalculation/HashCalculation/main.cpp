#include <iostream>
#include <fstream>
#include <vector>
#include <string>

using namespace std;
void readFromFile(string path_to_file, vector<string>* target_data) {
	fstream in;
	in.open(path_to_file);
	if (!in.is_open()) {
		cout << "Error occured while reading from file!";
		return;
	} 
	string buffer;
	while (getline(in, buffer)) {
		target_data->push_back(buffer);
	}
	in.close();
}

// 1 cпособ - сумма ASCII кодов
int hashFromChars(string target_string) {
	int total_size = 0;
	for (size_t i = 0; i < target_string.length(); i++) {
		total_size += (int)target_string[i];
	}
	return total_size;
}

// 2 способ - полиномиальный хэш
long long polyNomialHash(string target_string) {
	unsigned long total_size = 0;
	for (size_t i = 0; i < target_string.length(); i++) {
		total_size += pow((int)target_string[i], i);
	}
	return total_size;
}

int main() {
	cout << "Enter hash size (2 <= hash_size <= 30)" << endl;
	int hash_size = 0;
	cin >> hash_size;
	if (hash_size > 30 || hash_size < 2) {
		cout << "Hash size is out of range, terminating process...";
		return -1;
	}
	vector<string> file_strings;
	long long hash_table_size = (int)pow(2, hash_size);
	vector<bool> hash_table(hash_table_size, false);
	readFromFile("../res/endict.txt", &file_strings);
	int collision_amount = 0;
	long long index = 0;
	// сумма ASCII кодов
	for (int i = 0; i < file_strings.size(); i++) {
		index = hashFromChars(file_strings.at(i)) % hash_table_size;
		if (!hash_table.at(index)) {
			hash_table.at(index) = true;
		} else {
			collision_amount++;
		}
	}
	cout << "Collisions overall, (calculated by summing ASCII codes): " << collision_amount << endl;
	// полиномиальный подход
	vector<bool> hash_table2(hash_table_size, false);
	collision_amount = 0;
	string last_str = "";
	try {
		for (int i = 0; i < file_strings.size(); i++) {
			index = polyNomialHash(file_strings.at(i)) % hash_table_size;
			last_str = file_strings.at(i);
			if (!hash_table2.at(index)) {
				hash_table2.at(index) = true;
			}
			else {
				collision_amount++;
			}
		}
	} catch (exception exp) {
		cout << exp.what() << endl;
		cout << "Last string was: " << last_str << " its index: " << index << endl; 
	}
	cout << "Collisions overall, (calculated by polynomial hash): " << collision_amount << endl;
	system("pause");
}	