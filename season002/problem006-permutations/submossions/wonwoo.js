/**
 * @param {number[]} nums
 * @return {number[][]}
 */
const permute = function (nums) {

};

const printMat = function (matrix) {
    if (matrix !== undefined) {
        matrix.forEach(v => {
            console.log(v)
        })
    }
};

// scoring
const inputs = [
    [1, 2, 3]
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
