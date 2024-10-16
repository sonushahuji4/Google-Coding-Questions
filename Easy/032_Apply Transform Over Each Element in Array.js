# https://leetcode.com/problems/apply-transform-over-each-element-in-array/description/?envType=company&envId=google&favoriteSlug=google-three-months&difficulty=EASY&role=full-stack

/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var map = function(arr, fn) {
    const newArr = []
    for(let i = 0; i < arr.length; i++){
        newArr.push(fn(arr[i],i))
    }
    return newArr
};
