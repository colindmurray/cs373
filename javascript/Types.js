/*global console, require*/
/*jslint white: true*/

// --------
// Types.js
// --------

// http://www.w3schools.com/js/js_datatypes.asp

var _      = require('lodash');
var assert = require('assert');

console.log("Types.js");

var b = false;
b = true;
assert((typeof b) === "boolean");
assert(_.isBoolean(b));

var n = 2.34;
assert((typeof n) === "number");
assert(_.isNumber(n));

var s = "abc";
assert((typeof s) === "string");
assert(_.isString(s));

function f (v) {
    "use strict";
    return v + 1;}
assert((typeof f) === "function");
assert(_.isFunction(f));
assert(f instanceof Function);
assert(f instanceof Object);
assert(Object.getPrototypeOf(f) === Function.prototype);

var a = [2, 3, 4];
assert((typeof a) === "object");
assert(_.isArray(a));
assert(a instanceof Array);
assert(a instanceof Object);
assert(Object.getPrototypeOf(a) === Array.prototype);

var x = {n : 2.34, s : "abc"};
assert((typeof x) === "object");
assert(_.isObject(x));
assert(x instanceof Object);
assert(Object.getPrototypeOf(x) === Object.prototype);

assert(Function instanceof Object);
assert(Object.getPrototypeOf(Function.prototype) === Object.prototype);

assert(Array instanceof Object);
assert(Object.getPrototypeOf(Array.prototype) === Object.prototype);

assert(Object instanceof Object);
assert(Object.getPrototypeOf(Object.prototype) === null);

console.log("Done.");
