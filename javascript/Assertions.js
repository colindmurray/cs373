/*global console, require*/
/*jslint plusplus: true, white: true*/

// -------------
// Assertions.js
// -------------

var assert = require('assert');

function cycle_length (n) {
    "use strict";
    assert(n > 0);
    var c = 0;
    while (n > 1) {
        if ((n % 2) === 0) {
            n = n / 2;}
        else {
            n = (3 * n) + 1;}
        ++c;}
    assert(c > 0);
    return c;}

console.log("Assertions.js");

assert(cycle_length( 1) === 1);
assert(cycle_length( 5) === 6);
assert(cycle_length(10) === 7);

console.log("Done.");

/*
% npm install assert -- save

% node Assertions.js
Assertions.js

assert.js:86
  throw new assert.AssertionError({
        ^
AssertionError: false == true
    at cycle_length (/Users/downing/Dropbox/examples/javascript/Assertions.js:20:5)
    at Object.<anonymous> (/Users/downing/Dropbox/examples/javascript/Assertions.js:25:8)
    at Module._compile (module.js:460:26)
    at Object.Module._extensions..js (module.js:478:10)
    at Module.load (module.js:355:32)
    at Function.Module._load (module.js:310:12)
    at Function.Module.runMain (module.js:501:10)
    at startup (node.js:129:16)
    at node.js:814:3
*/
