# SimpleCalculator

This calculator was constructed as an exploration of test driven development.

The test framework chosen was Python's unittest package, included in the standard library. 
from the root project folder, the bash command `python3 -m unittest test.calculator_test` will run the test suite.

The test-driven development pattern followed here is:
1. After declaring prospective tests with expected assertions, the class details flesh themselves out in order to run tests without crashing.
The inital test cases should produce failing tests.
2. From here the methods are written in the simplest manner to produce passing results. 
3. Once there are at least three duplications of nearly identical code-blocks, the code will need to be refactored for dry or abstracted simplifications.
