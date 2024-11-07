/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function (x) {
    let answer = true;

    if (x < 0) {
        return false;
    }

    // 숫자를 문자열로 변환
    const str = x.toString();

    for (let i = 0; i < str.length - 1; i++) {
        if (str[i] !== str[str.length - 1 - i]) {
            answer = false;
        }
    }
    return answer;
};