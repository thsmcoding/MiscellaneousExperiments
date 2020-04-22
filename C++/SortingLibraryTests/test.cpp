#include "pch.h"
#include <vector>
#include "C:\Users\hassi\source\repos\SortingLibrary\SortingLibrary\elementarysorts.cpp"
#include <algorithm>
#include <string>

TEST(EMPTYVECTORCASE, selectionSortFunction) {
	std::vector<int> vector1 = {};
	std::vector<int> vector1_bis = {};
	selectionSort<int>(vector1_bis);
	EXPECT_EQ(vector1, vector1_bis);
}

TEST(INTEGERVECTORCASE, selectionSortFunction) {
	std::vector<int> vector1 = { -1,0,7,8,-1,2,7,100,-400,35,38 };
	std::vector<int> vector1_bis = { -1,0,7,8,-1,2,7,100,-400,35,38 };
	std::sort(vector1.begin(), vector1.end());

	selectionSort<int>(vector1_bis);
	EXPECT_EQ(vector1, vector1_bis);
}

TEST(INTEGERVECTOR_DUPLICATECASE, selectionSortFunction) {
	std::vector<int> vector1 = { -1,0,-1,-1,15,7,15,15 };
	std::vector<int> vector1_bis = { -1,0,-1,-1,15,7,15,15 };
	std::sort(vector1.begin(), vector1.end());
	selectionSort<int>(vector1_bis);
	EXPECT_EQ(vector1, vector1_bis);
}

TEST(STRINGCASE, selectionSortFunction) {
	std::vector<std::string> vector1 = { "maman", "happy", "friday","here" };
	std::vector<std::string> vector1_bis = { "maman", "happy", "friday","here" };
	std::sort(vector1.begin(), vector1.end());
	selectionSort<std::string>(vector1_bis);
	EXPECT_EQ(vector1, vector1_bis);
}
