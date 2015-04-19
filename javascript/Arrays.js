// ---------
// Arrays.js
// ---------

// http://devdocs.io/lodash-array/

var _      = require('lodash');
var assert = require('assert');

console.log("Arrays.js");

var a = [2, 3, 4];
assert(a.length == 3);
assert(a[0] == 2);
assert(a[1] == 3);
assert(a[2] == 4);
assert(a[3] == undefined);

assert(_.isEqual(_.chunk(a), [[2], [3], [4]]));

console.log("Done.");
