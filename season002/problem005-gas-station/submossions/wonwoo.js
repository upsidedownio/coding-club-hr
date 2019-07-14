/**
 * get circular index
 * @param {number} length   - length of array
 * @param {number} i        - desire index
 * @returns {number} - index
 */
const cidx = function (length, i) {
    return (length + i) % length;
};

/**
 * @param {number[]} gas
 * @param {number[]} cost
 * @return {number}
 */
const canCompleteCircuit = function (gas, cost) {
    const margin = [];
    for (let i = 0; i < gas.length; i++) {
        margin[i] = gas[cidx(gas.length, i + 1)] - cost[i];
    }
    console.log(gas);
    console.log(margin);
    const sum = margin.reduce((result, item, index) => {
        return result + item;
    }, 0);
    console.log('sum', sum);

    if (sum < 0) {
        return -1;
    } else {
        // const shiftMargin = margin;
        // let ticketUsed = false;
        // for (let i = 0; i < margin.length; i++) {
        //     if (shiftMargin[i] < 0) {
        //         if(!ticketUsed){
        //             shiftMargin[i]++;
        //             ticketUsed = true;
        //         }
        //         shiftMargin[cidx(shiftMargin.length, i + 1)] += shiftMargin[i];
        //         shiftMargin[i] = 0;
        //         console.log(shiftMargin);
        //     } else if (shiftMargin[i] > 0) {
        //         shiftMargin[cidx(shiftMargin.length, i + 1)] += (shiftMargin[i] - 1);
        //         shiftMargin[i] = 1;
        //         console.log(shiftMargin);
        //     }
        // }
        // return shiftMargin.findIndex(v => v === 1);


        // 2
        // let sum = 0;
        // let start = 0;
        // let cursor = 1;
        // sum = gas[start];
        // while(true){
        //     sum += margin[cursor];
        //     while(sum < 0){
        //         sum -= gas[start];
        //         sum += gas[cidx(gas.length, start+1)];
        //         start++;
        //         sum -= margin[start];
        //         if(start === gas.length){
        //             return -1;
        //         }
        //     }
        //     cursor++;
        //     if(cursor === gas.length){
        //         return start;
        //     }
        // }

        for (let i = 0; i < gas.length; i++) {
            let sum = gas[i];
            let j = cidx(gas.length, i + 1);
            let output = i;
            while(i !== j){
                sum += margin[j];
                console.log(i, j, sum);
                if(sum < 0){
                    output = -1;
                    break;
                }
                j = cidx(gas.length, j + 1);
            }
            if(output >= 0) {
                return output;
            }
        }
    }
};

// scoring
const inputs = [
    {
        gas: [1, 2, 3, 4, 5],
        cost: [3, 4, 5, 1, 2]
    },
    {
        gas: [2, 3, 4],
        cost: [3, 4, 3]
    },
    {
        gas: [5, 8, 2, 8],
        cost: [6, 5, 6, 6]
    }
];

const expects = [
    3,
    -1,
    3
];

for (let i = 0; i < inputs.length; i++) {
    console.log(`item ${i}: ${inputs[i].gas}, ${inputs[i].cost}`);
    const ans = canCompleteCircuit(inputs[i].gas, inputs[i].cost);
    console.log(`ans: ${ans}, expect: ${expects[i]}\n`);
}
