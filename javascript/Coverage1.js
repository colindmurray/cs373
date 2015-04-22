/*global console, require, suite, test*/
/*jslint plusplus: true, white: true*/

// ------------
// Coverage1.js
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
                assert.equal(cycle_length(1), 1);});});

/*
% istanbul cover _mocha -- -u tdd Coverage1.js


  cycle_length
    ✓ test_1


  1 passing (5ms)

=============================================================================
Writing coverage object [/Users/downing/Dropbox/examples/javascript/coverage/coverage.json]
Writing coverage reports at [/Users/downing/Dropbox/examples/javascript/coverage]
=============================================================================

=============================== Coverage summary ===============================
Statements   : 71.43% ( 10/14 )
Branches     : 0% ( 0/2 )
Functions    : 100% ( 3/3 )
Lines        : 71.43% ( 10/14 )
================================================================================
*/
