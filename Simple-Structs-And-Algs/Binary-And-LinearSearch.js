// ---------------------- BINARY SEARCH ALGO ---------------------- //

array = [3, 12, 4, 8, 1, 0, 7, 5, 34, 47, 99, 28, 39];
array = mergeSort(array); //PULLED FROM MERGE SORT FILE;
console.log(array);
let steps = 0; // TESTING HOW MANY STEPS ARE NEEDED, NOT NEEDED JUST FOR TESTING

// @binarySearchTree Effectivly everytime this is called it starts at the middle and searches either left or right depending on the target value
function binarySearch(array, target, start, end) {
    if (start > end){
        return "Error The Provided Start exceeds he End this is impossible!"
    }
    
    const middle = Math.floor((start + end) / 2);

    if (array[middle] === target) {
        return target + " IS FOUND, STEPS = " + steps
    }
    // if the middle value is greater than the target only search the left side
    if (array[middle] > target) {
        // RECURSIVE - since its greater start from the middle but check from the start to the middle DIVIDE AND CONQUER
        return binarySearch(target, start, middle); 
    }
    if (array[middle] < target) {
        // if its less than that means it has to be further in the array so simply start from where you went to in the middle and go to the end
        return binarySearch(target, middle, end);
    }
}

// ---------------------- LINEAR SEARCH ---------------------- //

let linArray = [49, 4, 59, 5, 42, 99, 3];
function linSearch(array, val){
    for(let i = 0; i < linArray.length; i++){
        if (array[i] == val){
            return i;
        }
    
    }
        return -1;
}
console.log(linSearch(linArray, 4));
