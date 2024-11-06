/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    let a;
    let b;
    for (let i = 0; i < nums.length - 1; i++) {
        let n = target - nums[i];
        let num = nums.slice(i + 1);

        if (num.includes(n)) {
            a = i;
            b = num.indexOf(n) + (i + 1);
            break;
        }
    }
    return [a, b];
};