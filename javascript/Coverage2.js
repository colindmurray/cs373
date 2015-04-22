/*global console, require, suite, test*/
/*jslint plusplus: true, white: true*/

// ------------
// Coverage2.js
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
                assert.equal(cycle_length(2), 2);});});

/*
% istanbul cover _mocha -- -u tdd Coverage2.js


  cycle_length
    ✓ test_1
    ✓ test_2


  2 passing (5ms)

=============================================================================
Writing coverage object [/Users/downing/Dropbox/examples/javascript/coverage/coverage.json]
Writing coverage reports at [/Users/downing/Dropbox/examples/javascript/coverage]
=============================================================================

=============================== Coverage summary ===============================
Statements   : 93.75% ( 15/16 )
Branches     : 50% ( 1/2 )
Functions    : 100% ( 4/4 )
Lines        : 93.75% ( 15/16 )
================================================================================
*/
