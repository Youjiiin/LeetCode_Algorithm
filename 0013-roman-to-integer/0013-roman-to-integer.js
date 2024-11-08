/**
 * @param {string} s
 * @return {number}
 */
var romanToInt = function(s) {
    const roman = {
        I: 1,
        V: 5,
        X: 10,
        L: 50,
        C: 100,
        D: 500,
        M: 1000
    }

    let answer = 0;
    for (let i = 0; i < s.length; i++) {
        const now = roman[s[i]];
        const next = roman[s[i + 1]];

        if (now < next) {
            answer += next - now;
            i++;
        } else {
            answer += now;
        }
    }

    return answer
};