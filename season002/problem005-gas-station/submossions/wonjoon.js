/**
 * @param {number[]} gas
 * @param {number[]} cost
 * @return {number}
 */
var canCompleteCircuit = function(gas, cost) {
    for(let i=0; i<gas.length; i++) {
        if(isValidStation(gas, cost, i)) {
            return i;
        }
    }

    return -1;
};

function isValidStation(gas, cost, start)  {
    let tank = 0;
    for(let i=0; i < gas.length; i++) {
        let index = i + start;

        if (index > gas.length - 1) {
            index = index - gas.length;
        }

        tank = tank + gas[index] - cost[index];
        if (tank < 0) {
            return false;
        }
    }

    return true;
}