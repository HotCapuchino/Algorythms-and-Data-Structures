#pragma once

class Krug {
private:
	double x;
	double y;
	double radius;
public:
	Krug(double x, double y, double radius) {
		this->x = x;
		this->y = y;
		this->radius = radius;
	}
	double distance_from_center_to_origin() {
		return sqrt((x - 0) * (x - 0) + (y - 0) * (y - 0));
	}
	double distance_to_other_krug(Krug & krug) {
		return sqrt((x - krug.x) * (x - krug.x) + (y - krug.y) * (y - krug.y));
	}
	double distance_to_X_axis() {
		double result = abs(y) - radius;
		return result > 0 ? result : 0;
	}
	double distance_from_krug_to_origin() {
		double result = this->distance_from_center_to_origin() - radius;
		return result > 0 ? result : 0;
	}
	double can_be_inscribed_in(Krug & destination_krug) {
		return radius > destination_krug.radius;
	}
	double are_crossed_with(Krug & krug) {
		double distance_between = this->distance_to_other_krug(krug);
		double minor_radius = radius < krug.radius ? radius : krug.radius;
		double major_radius = radius > krug.radius ? radius : krug.radius;
		if (distance_between < minor_radius + major_radius ||
			distance_between == minor_radius + major_radius ||
			distance_between + minor_radius >= major_radius) return true;
		return false;
	}
	~Krug(){}
};