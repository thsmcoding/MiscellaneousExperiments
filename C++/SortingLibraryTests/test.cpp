#include "pch.h"
#include <vector>
#include "../SortingLibrary/elementarysorts.h"
#include <algorithm>
#include <string>
#include "../gtest/gtest.h"

using namespace std;

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

TEST(INTEGERINSERTION, insertionSortFunction) {
	std::vector<int> vector1 = { 100,-1,0,-15,-17,207,85,14,63,789,157,41,-45 };
	std::vector<int> vector1_bis = { 100,-1,0,-15,-17,207,85,14,63,789,157,41,-45 };
	std::sort(vector1.begin(), vector1.end());
	insertionSort<int>(vector1_bis);
	EXPECT_EQ(vector1, vector1_bis);
}

TEST(INTEGERINSERTIONIMRPOVED, insertionSortimprovedFunction) {
	std::vector<int> vector1 = { 100,-1,0,-15,-17,207,85,14,63,789,157,41,-45 };
	std::vector<int> vector1_bis = { 100,-1,0,-15,-17,207,85,14,63,789,157,41,-45 };
	std::sort(vector1.begin(), vector1.end());
	insertionSortimproved<int>(vector1_bis);
	EXPECT_EQ(vector1, vector1_bis);
}

TEST(INTEGERBUBBLESORT, bubbleSortFunction) {
	std::vector<int> vector1 = {0,100,-1,0,-15,-17,207,85,14,63,789,157,41,-45 };
	std::vector<int> vector1_bis = { 0,100,-1,0,-15,-17,207,85,14,63,789,157,41,-45 };
	std::sort(vector1.begin(), vector1.end());
	bubbleSort<int>(vector1_bis);
	EXPECT_EQ(vector1, vector1_bis);
}

int main(int argc, char** argv) {
	::testing::InitGoogleTest(&argc, argv);
	return RUN_ALL_TESTS();
}