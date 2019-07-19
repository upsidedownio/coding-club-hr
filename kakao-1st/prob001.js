/**
 * @typedef {string} MapString  - Part of map by constructed ' ' and '#'
 */
/**
 * @typedef {number} MapCode
 */

/**
 * @param {number} n        - map size
 * @param {MapCode[]} arr1  - map code 1
 * @param {MapCode[]} arr2  - map code 2
 * @return {MapString[]}
 */
const makeMap = function (n, arr1, arr2) {
    let completeMap = [];
    for (let i = 0; i < n; i++) {
        // bitwise OR
        completeMap[i] = arr1[i] | arr2[i];
    }
    return completeMap.map(code => toMapString(code, n));
};

/**
 * convert MapCode to MapString
 * @param {MapCode} mapCode - map code
 * @param {number} n        - map size
 * @returns {MapString}
 */
function toMapString(mapCode, n) {
    let binaryString = Number(mapCode).toString(2);
    // if length of binaryString is shorter than map size, MSBs should padded by '0'
    let padded = '0'.repeat(n).substring(binaryString.length) + binaryString;
    padded = padded.replace(/0/g, ' ');
    padded = padded.replace(/1/g, '#');
    return padded;
}

/**
 * concat MapString[] to multi-line String
 * @param {MapString[]} map
 * @returns {string}
 */
function printMap(map) {
    let output = '';
    map.forEach(code => {
        output += code + '\n';
    });
    return output;
}

// scoring
const inputs = [
    {n: 5, arr1: [9, 20, 28, 18, 11], arr2: [30, 1, 21, 17, 28]},
    {n: 6, arr1: [46, 33, 33, 22, 31, 50], arr2: [27, 56, 19, 14, 14, 10]}
];

const expects = [
    [
        "#####",
        "# # #",
        "### #",
        "#  ##",
        "#####"
    ],
    [
        "######",
        "###  #",
        "##  ##",
        " #### ",
        " #####",
        "### # "
    ]
];

for (let i = 0; i < inputs.length; i++) {
    console.log(`item ${i}: ${JSON.stringify(inputs[i])}`);
    const ans = makeMap(inputs[i].n, inputs[i].arr1, inputs[i].arr2);
    console.log(`expect:`);
    console.log(printMap(expects[i]));
    console.log(`ans:`);
    console.log(printMap(ans));
}

// time consumed: 15min
