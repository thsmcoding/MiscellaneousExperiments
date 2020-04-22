#pragma once
#include<vector>

template<typename U> inline bool compareU(U i, U j);


template<typename U> inline void selectionSort(std::vector<U>&);


template<typename U>  bool compareU(U i, U j) {
	return i < j;
}



template<typename U> void selectionSort(std::vector<U>& vec1) {
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
		//exchanges happen here
		if (min_index != i) {
			vec1[i] = minimum;
			vec1[min_index] = current;
		}

	}
}

//template<typename U>
//void insertionSort(std::vector<U>&);

//template<typename U>
//void shellSort(std::vector<U>&);

