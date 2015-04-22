/*global console, require, suite, test*/
/*jslint plusplus: true, white: true*/

// -------------
// UnitTests3.js
// -------------

var assert = require('assert');

function cycle_length (n) {
    "use strict";
    assert(n > 0);
    var c = 1;
    while (n > 1) {
        if ((n % 2) === 0) {
            n = n / 2;}
        else {
            n = (3 * n) + 1;}
        ++c;}
    assert(c > 0);
    return c;}

suite('cycle_length',
    function () {
        "use strict";

        test('test_1',
            function () {
                assert.equal(cycle_length( 1), 1);});

        test('test_2',
            function () {
                assert.equal(cycle_length( 5), 6);});

        test('test_3',
            function () {
                assert.equal(cycle_length(10), 7);});});

/*
% mocha -u tdd UnitTests3.js


  cycle_length
    ✓ test_1
    ✓ test_2
    ✓ test_3

  3 passing (7ms)
*/
