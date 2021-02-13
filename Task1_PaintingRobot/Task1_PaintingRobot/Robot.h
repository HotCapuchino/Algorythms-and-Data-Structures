#pragma once
#include "Directions.h"

class Robot {
private:
	int direction = UP;
	int x = 0;
	int y = 0;
public:
	Robot() {};
	void step() {
		switch (direction) {
		case UP: y--;
			break;
		case RIGHT: x++;
			break;
		case DOWN: y++;
			break;
		case LEFT: x--;
			break;
		default:
			break;
		}
	}
	void rotate(int direction) {
		while (this->direction != direction) {
			this->direction += 1;
			if (this->direction > 4) this->direction = 4 - this->direction;
		}
	}
	int getX() { 
		return x;
	}
	int getY() {
		return y;
	}
	bool shouldPaintCell(int field_metric) {
		if (x == y || field_metric - x - 1 == y || x == field_metric - y - 1) return true;
		return false;
	}
	~Robot() {};
	friend class Field;
};