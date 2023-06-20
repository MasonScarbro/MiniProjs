// ---------------------- MERGESORT ---------------------- //

/* Small note: Merge sort is obviously capable of doing more than 
numbers for instance you could do letters by using their unicode, 
it is capable like many other sorting methods to do objects dependent on data and more
this code is the base layout for merge sort but either this code may need to be tampered with
or you may need code that assigns some sort of numeric value or data outside of the function */


const array = [3, 12, 4, 8, 1, 0, 7, 5];
function mergeSort(array) {
    if (array.length < 2 ){
        return array;
    }
    const midArray = Math.floor(array.length / 2); // Because JS vars arent given types this would be float
    const leftArray = array.slice(0, midArray); // take the left from the first index to the middle
    const rightArray = array.slice(midArray); // take the right from the middle to the end
    return merge(mergeSort(leftArray), mergeSort(rightArray)); // call merge which recursivley calls mergesort (the logic is in mergesort algo)
}
// Simply merges the final producss so that it will actually be sorted and in one array
function merge(leftArray, rightArray){
    const tempArray = []; // the tempary array that
    while (leftArray.length > 0 && rightArray.length > 0) { // while the arrays are not empty run this code
        if (leftArray[0] <= rightArray[0]) {
            tempArray.push(leftArray.shift()); // if the left starting index is less than push it to the array first and remove it so that the first index i.e [0] works with the next indecie
        } else {
            tempArray.push(rightArray.shift()); // ^ same logic but with the right array 
        }
    }
    return [...tempArray, ...leftArray, ...rightArray]; 
}
mergeSort(array);
