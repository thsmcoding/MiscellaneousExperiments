#pragma once
#include<vector>
#include<math.h>

template<typename U> inline bool compareU(U i, U j);
template<typename U> inline void selectionSort(std::vector<U>&);
template<typename U> inline void insertionSort(std::vector<U>&);
template<typename U> inline void insertionSortimproved(std::vector<U>&);
template<typename U> inline void bubbleSort(std::vector<U> &);
template<typename U> inline void quicksort(std::vector<U> &, int, int);
template<typename U> inline int quicksortpartition(std::vector<U> &, int, int);
template<typename U> inline void quicksort3way(std::vector<U>&, int, int);
template<typename U> inline void mergesortTD(std::vector<U>&, int, int);
template<typename U> inline void mergesortBU(std::vector<U>&, int, int);
template<typename U> inline void merge(std::vector<U>&, int, int, int);
template<typename U> inline void shellsort(std::vector<U>&);


template<typename U>  bool compareU(U i, U j) {
	return i < j;
}


/****** FUNCTION DEFINITIONS ************************************************/
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

template<typename U> int quicksortpartition(std::vector<U> &vec, int low, int high) {
	int i = low, j = high + 1;
	auto current = vec[i];
	while (1) {
		while (vec[++i] < current) {
			if (i == high)
				break;
		}
		while (vec[--j] > current) {
			if (j == low)
				break;
		}
		if (i >= j)
			break;

		auto temp_i = vec[i];
		auto temp_j = vec[j];
		vec[i] = temp_j;
		vec[j] = temp_i;
	}
	auto current_j = vec[j];
	vec[j] = current;
	vec[low] = current_j;
	return j;
}

template<typename U> void quicksort(std::vector<U> &vec, int low, int high) {
	if (low >= high)
		return;
	int partition_index = quicksortpartition(vec, low, high);
	quicksort(vec, 0, partition_index - 1);
	quicksort(vec, partition_index + 1, high);

}

template<typename U> void quicksort3way(std::vector<U>&vec, int low, int high) {
	if (low >= high)
		return;
	int inf = low, i = low + 1, sup = high;
	auto current = vec[low];
	while (i <= sup) {
		if (vec[i] < current) {
			auto temp_i = vec[i];
			auto temp_current = vec[inf];
			vec[inf++] = temp_i;
			vec[i++] = temp_current;

		}

		else if (vec[i] > current) {
			auto temp_i = vec[i];
			auto temp_sup = vec[sup];
			vec[i] = temp_sup;
			vec[sup] = temp_i;
			sup--;
		}
		else
			i++;
	}
	quicksort3way(vec, low, inf - 1);
	quicksort3way(vec, sup + 1, high);
}


template<typename U> void merge(std::vector<U>& vec, int low, int mid, int high) {
	std::vector<U> copy_vec;
	std::copy(vec.begin(), vec.end(), std::back_inserter(copy_vec));
	copy_vec = vec;
	int i, j;
	i = low;
	j = mid + 1;

	for (unsigned int k = low; k <= high; k++) {
		if (i > mid) vec[k] = copy_vec[j++];
		else if (j > high) vec[k] = copy_vec[i++];
		else if (copy_vec[i] < copy_vec[j]) vec[k] = copy_vec[i++];
		else  vec[k] = copy_vec[j++];
	}
}


template<typename U> void mergesortTD(std::vector<U>& vec, int low, int high) {
	if (high <= low)
		return;
	int mid = ceil(low + (high - low) / 2);
	mergesortTD(vec, low, mid);
	mergesortTD(vec, mid + 1, high);
	merge(vec, low, mid, high);
}

template<typename U> void mergesortBU(std::vector<U>& vec, int low, int high) {
	auto N = vec.size();
	for (unsigned int sz = 1; sz < N; sz = sz + sz) {
		for (unsigned int i = 0; i < N - sz; i += sz + sz) {
			int min = fmin(N - 1, i + sz + sz - 1);
			merge(vec, i, i + sz - 1, min);
		}
	}
}

template<typename U> void shellsort(std::vector<U>& vec) {
	int h = 1, N = vec.size();
	while (h < N / 3) {
		h = 3 * h + 1;
	}

	while (h >= 1) {
		for (int i = h; i < N; i++) {
			for (int j = i; j >= h && vec[j] < vec[j - h]; j -= h) {
				auto current_j = vec[j];
				auto current_j_h = vec[j - h];
				vec[j] = current_j_h;
				vec[j - h] = current_j;
			}
		}
		h = h / 3;

	}
}