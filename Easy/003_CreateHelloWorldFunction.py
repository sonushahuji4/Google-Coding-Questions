# https://leetcode.com/problems/create-hello-world-function/description/?envType=company&envId=google&favoriteSlug=google-three-months&difficulty=EASY&role=full-stack

/**
 * @return {Function}
 */
var createHelloWorld = function() {
    
    return function(...args) {
        return "Hello World"
    }
};

/**
 * const f = createHelloWorld();
 * f(); // "Hello World"
 */
