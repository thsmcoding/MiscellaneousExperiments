#pragma once
#include<vector>

template<typename U> inline bool compareU(U i, U j);
template<typename U> inline void selectionSort(std::vector<U>&);
template<typename U> inline void insertionSort(std::vector<U>&);
template<typename U> inline void insertionSortimproved(std::vector<U>&);
template<typename U> inline void bubbleSort(std::vector<U> &);
template<typename U>  bool compareU(U i, U j) {
	return i < j;
}

/****** FUCNTION DEFINITIONS ************************************************/
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

template<typename U> void insertionSort(std::vector<U>& vec) {
	for (int i = 1; i < vec.size(); i++) {
		for (int j = i; j > 0 && (vec[j] < vec[j - 1]); --j) {
			auto item_j = vec[j];
			auto item_j_1 = vec[j - 1];
			vec[j] = item_j_1;
			vec[j - 1] = item_j;
		}
	}
}

template<typename U> void insertionSortimproved(std::vector<U>& vec) {
	for (int i = 1; i < vec.size(); i++) {
		auto current = vec[i];
		int j = i;
		for (j = i; j > 0 && (current < vec[j - 1]); --j) {
			auto item_j_1 = vec[j - 1];
			vec[j] = item_j_1;
		}
		vec[j] = current;
	}
}


template<typename U> void bubbleSort(std::vector<U> &vec) {
	auto N = vec.size();
	bool swapped = false;
	for (int i = 0; i < N; i++) {
		swapped = (swapped == true) ? false : swapped;
		for (int j = 0; j < N - i - 1; j++) {
			if (vec[j] > vec[j + 1]) {
				auto current = vec[j];
				auto current_next = vec[j + 1];
				vec[j] = current_next;
				vec[j + 1] = current;
				swapped = true;
			}
		}
		if (swapped == false)
			break;
	}
}
