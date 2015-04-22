/*global console, require, suite, test*/
/*jslint plusplus: true, white: true*/

// ------------
// Coverage3.js
// ------------

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
                assert.equal(cycle_length(1), 1);});

        test('test_2',
            function () {
                assert.equal(cycle_length(2), 2);});

        test('test_3',
            function () {
                assert.equal(cycle_length(3), 8);});});

/*
% istanbul cover _mocha -- -u tdd Coverage3.js


  cycle_length
    ✓ test_1
    ✓ test_2
    ✓ test_3


  3 passing (6ms)

=============================================================================
Writing coverage object [/Users/downing/Dropbox/examples/javascript/coverage/coverage.json]
Writing coverage reports at [/Users/downing/Dropbox/examples/javascript/coverage]
=============================================================================

=============================== Coverage summary ===============================
Statements   : 100% ( 18/18 )
Branches     : 100% ( 2/2 )
Functions    : 100% ( 5/5 )
Lines        : 100% ( 18/18 )
================================================================================
*/
