/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var permute = function(nums) {
    const result = new Array();

    getNumber(copyArr(nums), i, result);

    return result;
};

function getNumber(arr, index, result);
for(let i=0; i<index; i++) {
    getNumber(arr, i, result);
}

function copyArr(origin) {
    const result = new Array();
    for(let i=0; i<origin.length; i++) {
        result.push(origin[i]);
    }

    return result;
}