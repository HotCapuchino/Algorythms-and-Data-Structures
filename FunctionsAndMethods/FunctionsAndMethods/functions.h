#pragma once

struct Circle {
	double x;
	double y;
	double radius;
};

double distance_from_center_to_origin(Circle * circle) {
	return sqrt((circle->x - 0) * (circle->x - 0) + (circle->y - 0) * (circle->y - 0));
}

double distance_between_circles(Circle * circle1, Circle * circle2) {
	return sqrt((circle1->x - circle2->x) * (circle1->x - circle2->x) + (circle1->y - circle2->y) * (circle1->y - circle2->y));
}

double distance_to_X_axis(Circle * circle) {
	double result = abs(circle->y) - circle->radius;
	return result > 0 ? result : 0;
}

double distance_from_circle_to_origin(Circle * circle) {
	double result = distance_from_center_to_origin(circle) - circle->radius;
	return result > 0 ? result : 0;
}

double can_be_inscribed(Circle * target_circle, Circle * destination_circle) { 
	return target_circle->radius > destination_circle->radius;
}

double are_they_crossed(Circle * circle1, Circle * circle2) {
	double distance_between = distance_between_circles(circle1, circle2);
	double minor_radius = circle1->radius < circle2->radius ? circle1->radius : circle2->radius;
	double major_radius = circle1->radius > circle2->radius ? circle1->radius : circle2->radius;
	if (distance_between < minor_radius + major_radius ||
		distance_between == minor_radius + major_radius ||
		distance_between + minor_radius >= major_radius) return true;
	return false;
}