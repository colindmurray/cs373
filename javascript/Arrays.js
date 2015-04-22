// ---------
// Arrays.js
// ---------

// http://devdocs.io/lodash-array/

var assert  = require('assert');

var _       = require('lodash');
var chunk   = _.chunk;
var isEqual = _.isEqual;

console.log("Arrays.js");

var a = [2, 3, 4];
assert(a.length == 3);
assert(a[0] == 2);
assert(a[1] == 3);
assert(a[2] == 4);
assert(a[3] == undefined);

assert(isEqual(chunk(a), [[2], [3], [4]]));

console.log("Done.");
