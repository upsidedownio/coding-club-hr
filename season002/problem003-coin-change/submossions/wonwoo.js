const sub = function (coins, remains) {
    for (let i = 0; i < coins.length; i++) {
        const c = coins[i];
        if (coins[i] <= remains) {
            return {selected: c, remains: remains - c};
        }
    }
    return {selected: null, remains: remains};
};

const smallerThan = function (coins, comparable) {
    return coins.find((v) => v < comparable);
};

/**
 * @param {number[]} coins
 * @param {number} amount
 * @return {number}
 */
const coinChange = function (coins, amount) {
    //greedy algorithm + dynamic programming
    let selectedCoins = [];
    let remains = amount;

    coins = coins.sort((a, b) => {
        return a - b;
    }).reverse();

    let dead = 0;

    while (true) {
        if (dead > 2) {
            return -1;
        }

        const step = sub(coins, remains);
        if (step.selected === null) {
            if (step.remains === 0) {
                console.log(selectedCoins);
                return selectedCoins.length;
            } else {
                // dead end
                if (selectedCoins[0].max && smallerThan(coins, selectedCoins[0].max)) {
                    console.log('dead end', selectedCoins);
                    return -1;
                }
                // console.log('failed combination', selectedCoins);
                selectedCoins = selectedCoins.reverse();
                let lastSelectedIdx = selectedCoins.findIndex((v) => !!v.max);

                if (lastSelectedIdx === -1) {
                    lastSelectedIdx = 0;
                }
                selectedCoins.slice(lastSelectedIdx, selectedCoins.length);

                selectedCoins = selectedCoins.reverse();
                // console.log('slice', selectedCoins);
                let lastItem = selectedCoins.pop();
                let nextCandidate = smallerThan(coins, lastItem.selected);
                while (!nextCandidate) {
                    lastItem = selectedCoins.pop();
                    if (!lastItem) {
                        console.log('dead end');
                        return -1;
                    }
                    nextCandidate = smallerThan(coins, lastItem.selected);
                }
                lastItem.max = lastItem.selected;
                lastItem.selected = nextCandidate;
                lastItem.remains += lastItem.max;
                lastItem.remains -= lastItem.selected;
                selectedCoins.push(lastItem);
                remains = lastItem.remains;
                // console.log('history updated', selectedCoins, remains);
            }
        } else {
            selectedCoins.push(step);
            remains = step.remains;
            if (remains === 0) {
                console.log(selectedCoins);
                return selectedCoins.length;
            }
        }
    }
};

// scoring
const inputs = [
    {
        coins: [5, 1, 2],
        amount: 11
    },
    {
        coins: [2],
        amount: 3
    },
    {
        coins: [4, 7, 17],
        amount: 21
    },
    {
        coins: [4, 7, 17],
        amount: 25
    },
    {
        coins: [186, 419, 83, 408],
        amount: 6249
    }
];

const expects = [
    3,
    -1,
    2,
    3,
    20
];

for (let i = 0; i < inputs.length; i++) {
    console.log(`item ${i}: ${inputs[i].coins}, ${inputs[i].amount}`);
    const ans = coinChange(inputs[i].coins, inputs[i].amount);
    console.log(`ans: ${ans}, expect: ${expects[i]}\n`);
}
