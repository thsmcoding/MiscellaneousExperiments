#include "pch.h"
#include "elementarysorts.h"

template<typename U>
bool compareU(U i, U j) {
	return i < j;
}

template<typename U>
void selectionSort(std::vector<U>& vec1) {
	for (int i = 0; i < vec1.size(); i++) {
		auto current = vec1[i];
		int min_index = i;
		U minimum = vec1[i];
		for (int j = i; j < vec1.size(); j++) {
			if (compareU(vec1[j], minimum)) {
				minimum = vec1[j];
				min_index = j;
			}
		}
		//exchange happen here
		if (min_index != i) {
			vec1[i] = minimum;
			vec1[min_index] = current;
		}

	}
}