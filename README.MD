# Pysandbox 

- Easily test programming questions with python
- Add your testing text in `test.txt` and then add solution as a class `Solution` in `main.py` or you can change this inside `test.py` .
- By default from `main.py` `Solution().solve()` would be called with the input given in `test.txt`
- We have two tests inside of `test.py` . `test_answer` asserts on the return values while `test_print` checks the value printed in the terminal by using `print()`. You can use either or both
- You can provide the expected solution output inside `solution.txt` and that would be tested with the input of `test.txt`. 
