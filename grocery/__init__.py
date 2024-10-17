import check50

@check50.check()
def exists():
    """grocery.py exists"""
    check50.exists("grocery.py")

@check50.check()
def test1():
    """Outputs 1"""
    check50.run("python3 grocery.py").stdin("banana").stdin("orange").stdin("apple").stdout("banana, orange, apple.").exit(0)
