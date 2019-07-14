/**
 * @param {number[]} gas
 * @param {number[]} cost
 * @return {number}
 */
const canCompleteCircuit = function (gas, cost) {

};

// scoring
const inputs = [
    {
        gas: [1, 2, 3, 4, 5],
        cost: [3, 4, 5, 1, 2]
    }
];

const expects = [
    3
];

for (let i = 0; i < inputs.length; i++) {
    console.log(`item ${i}: ${inputs[i].gas}, ${inputs[i].cost}`);
    const ans = canCompleteCircuit(inputs[i].coins, inputs[i].amount);
    console.log(`ans: ${ans}, expect: ${expects[i]}\n`);
}
