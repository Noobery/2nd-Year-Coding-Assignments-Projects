/* Alrick Ivan A. Gicole
Group Members: GC Neal Christian Clarin, Xerxes Lance Laurenz Lompon
Implementation of the three Algorithms Presented
*/

#include <iostream>
using namespace std;

//Sorting Algortihm for Finding  the ThirdMax
void selectionSort(int arr[], int n) {

    for (int i = 0; i < n - 1; i++) { // outer loop to iterate over array elements
        int minIndex = i; // assume current element is the minimum

        for (int j = i + 1; j < n; j++) { // inner loop to find the minimum element in the unsorted portion of the array
            if (arr[j] < arr[minIndex]) { // if a smaller element is found, update minIndex
                minIndex = j;
            }
        }
        swap(arr[i], arr[minIndex]); // swap the minimum element with the first unsorted element
    }
}

// This function finds the smallest of the three largest elements in an array of integers to get thirdMax
int findThirdMaxArray(int arr[], int n) {

    // Initialize the first three elements of the array as the maximum values
    int firstMax = arr[0];
    int secondMax = arr[1];
    int thirdMax = arr[2];

    // Loop through the rest of the array and update the maximum values
    for (int i = 3; i < n; i++) {
        if (arr[i] == firstMax || arr[i] == secondMax || arr[i] == thirdMax) {
            continue; // Skip duplicates
        }

        // Update the maximum values if the current element is greater than any of them
        if (arr[i] > firstMax || arr[i] > secondMax || arr[i] > thirdMax) {
             if (firstMax <= secondMax && firstMax <= thirdMax){
                firstMax = arr[i];
             }
             else if (secondMax <= firstMax && secondMax <= thirdMax){
               secondMax = arr[i];
             }
             else {
                thirdMax = arr[i];
             }
        }
    }

    // Finding the least value of the 3 variables which is the ThirdMax in the array
    int least = firstMax;
        if (secondMax < least) {
        least = secondMax;
        }
        if (thirdMax < least) {
        least = thirdMax;
        }

    return least;

    }

//This function finds the maximum value in the array and then create a new array without the max value unti we find ThirdMax
int findThirdMaxMultipleArray(int arr[], int n) {

    int maxValue_1 = arr[0]; // Initialize maxValue1 to the first element of the array
    int arrWithoutMax_1[n - 1]; // Create an array of length n - 1 to hold the values of arr without maxValue1
    int arrWithoutMax_2[n - 2]; // Create an array of length n - 2 to hold the values of arrWithoutMax1 without its maximum value

    for (int i = 1; i < n; i++) { // Find the maximum value in the original array and store it
        if (arr[i] > maxValue_1) {
            maxValue_1 = arr[i];
        }
    }

    int j = 0;
    for (int i = 0; i < n; i++) { //copying the values to arrWithoutMax_1 without the max value from the original array
        if (arr[i] != maxValue_1) {
            arrWithoutMax_1[j] = arr[i];
            j++;
        }
    }

    int maxValue_2 = arrWithoutMax_1[0];
    for (int i = 1; i < n - 1; i++) { // Find the maximum value in arrWithoutMax1 and store it
        if (arrWithoutMax_1[i] > maxValue_2) {
            maxValue_2 = arrWithoutMax_1[i];
        }
    }

    j = 0;
    for (int i = 0; i < n - 1; i++) { //copying the values to arrWithoutMax_2 without the max value arrWithoutMax_1
        if (arrWithoutMax_1[i] != maxValue_2) {
            arrWithoutMax_2[j] = arrWithoutMax_1[i];
            j++;
        }
    }

    int maxValue_3 = arrWithoutMax_2[0];
    for (int i = 1; i < n - 2; i++) {  // Find the maximum value in arrWithoutMax2, which is the ThirdMax
        if (arrWithoutMax_2[i] > maxValue_3) {
            maxValue_3 = arrWithoutMax_2[i];
        }
    }

    return maxValue_3; // Return the third maximum value
}

int main() {


    int a[] = {11, 21, 42, 6, 3, 10, 14, 24, 28, 30}; //sample array
    int n = sizeof(a) / sizeof(a[0]); //to get the size of the array


    cout << "The ThirdMax using THREE THIRD MAX: " << findThirdMaxArray(a, n) << endl;

    cout << "The ThirdMax using MULTIPLE ARRAYS: " << findThirdMaxMultipleArray(a, n) << endl;

    selectionSort(a, n);
    cout << "The ThirdMax using SORTING: " << a[n - 3] << endl;


    return 0;
}
