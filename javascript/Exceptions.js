/*global console, require*/
/*jslint white: true*/

// -------------
// Exceptions.js
// -------------

var assert = require('assert');

function f (b) {
    "use strict";
    if (b) {
        throw "abc";}
    return 0;}

console.log("Exceptions.js");

try {
    assert(f(false) === 0);}
catch (e) {
    assert(false);}

try {
    assert(f(true) === 1);
    assert(false);}
catch (e) {
    assert((typeof e) === "string");
    assert(e          === "abc");}

console.log("Done.");
