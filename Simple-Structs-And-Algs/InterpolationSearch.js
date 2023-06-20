// ---------------------- INTERPOLATION SEARCH ---------------------- //
// sorted array needed! //

let polArray = [1, 3, 5, 7, 28, 29, 48, 349, 430, 2720, 2839];
let stepsPol = 0; // FOR TESTING ONLY NOT NEEDED

function interpolationSearch(array, val) {
    let high = array.length - 1
    let low = 0;
    
    while(val >= array[low] && val <= array[high] && low <= high) {
        // formula where the targeted value is likely to be 
        probe = Math.round(low + (high - low) * (val - array[low]) / (array[high] - array[low]))
    

    if (array[probe] == val) {
        return "Probe Found " + steps
    }
    else if (array[probe] < val) {
        low = probe + 1;
        stepsPol++; // testing val

    } else {
        high = probe - 1;
        stepsPol++; // testing val
    }
}
    interpolationSearch(array, val);

}
console.log(interpolationSearch(polArray, 48));
