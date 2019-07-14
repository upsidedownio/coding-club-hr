/**
 * @param {number[]} nums
 * @return {number[][]}
 */
const permute = function (nums) {
    let length = nums.length;
    let result = [];

    let iteration = length - 1;
    let index = 1;
    //first item is inserted here
    result.push(nums);
    let last = nums;

    for (let startIndex = nums.length - 2; startIndex >= 0; startIndex--) {
        for (let lastIndex = nums.length - 1; lastIndex > startIndex; lastIndex--) {
            console.log('base:', last);
            for (let i = 0; i < lastIndex - startIndex; i++) {
                last = rotateRight(last, startIndex, lastIndex);
                result.push(last);
                console.log('last', last);
            }
            last = rotateRight(last, startIndex, lastIndex);
            console.log('finish:', last);
        }
    }

    return result;
};

function rotateRight(items, startIndex, lastIndex) {
    // console.log('rotateRight', items, startIndex, lastIndex);
    let before = items.slice(0, startIndex);
    let after = items.slice(startIndex, lastIndex + 1);
    let remains = items.slice(lastIndex + 1, items.length);
    // console.log('after', after);
    // console.log('before', before);
    let temp = after.shift();
    // console.log('shift', temp);
    // console.log('after', after);
    after.push(temp);
    let output = before.concat(after).concat(remains);
    // console.log('rotated:', output);
    return output;
}


const printMat = function (matrix) {
    if (matrix !== undefined) {
        matrix.forEach(v => {
            console.log(v)
        })
    }
};

// scoring
const inputs = [
    [1, 2, 3, 4]
];

const expects = [
    [
        [1, 2, 3],
        [1, 3, 2],
        [2, 1, 3],
        [2, 3, 1],
        [3, 1, 2],
        [3, 2, 1]
    ]
];

for (let i = 0; i < inputs.length; i++) {
    console.log(`item ${i}: ${inputs[i]}`);
    const ans = permute(inputs[i]);
    console.log(`expect:`);
    printMat(expects[i]);
    console.log(`ans:`);
    printMat(ans);
}
