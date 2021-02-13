#pragma once
#include <iostream>
#include "Robot.h"

enum CellStatus {
	PAINTED,
	NOT_PAINTED
};

class Field {
private:
	int field_metric;
	int ** field;
	Robot robot = Robot();
	void paintMainDiagonal() {
		paintCell();
		while (robot.getX() < field_metric - 1 && robot.getY() < field_metric - 1) {
			robot.rotate(RIGHT);
			robot.step();
			robot.rotate(DOWN);
			robot.step();
			paintCell();
		}
	}
	
	void goUp() {
		robot.rotate(UP);
		while (robot.getY() != 0) {
			robot.step();
		}
	}

	void paintExtraDiagonal() {
		paintCell();
		while (robot.getX() != 0 && robot.getY() != field_metric - 1) {
			robot.rotate(LEFT);
			robot.step();
			robot.rotate(DOWN);
			robot.step();
			paintCell();
		}
	}

	void paintCell() {
		if (robot.shouldPaintCell(field_metric)) {
			field[robot.getX()][robot.getY()] = PAINTED;
		}
	}

public:
	Field(int field_metric) {
		this->field_metric = field_metric > 1 ? field_metric : 2;
		field = new int*[field_metric];
		for (int i = 0; i < field_metric; i++) {
			field[i] = new int[field_metric];
			for (int j = 0; j < field_metric; j++) {
				field[i][j] = NOT_PAINTED;
			}
		}
	};

	~Field() {
		for (int i = 0; i < field_metric; i++) {
			delete field[i];
		}	
		delete field;
	}

	void paintField() {
		paintMainDiagonal();
		goUp();
		paintExtraDiagonal();
	}

	void printField() {
		for (int i = 0; i < field_metric; i++) {
			for (int j = 0; j < field_metric; j++) {
				if (field[i][j] == PAINTED) {
					std::cout << 1 << " ";
				} else {
					std::cout << 0 << " ";
				}
			}
			std::cout << std::endl;
		}
	}
};