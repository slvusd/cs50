import check50

@check50.check()
def exists():
    """grocery.py exists"""
    check50.exists("grocery.py")

@check50.check()
def test_output():
    """Outputs 1"""
    check50.run("python3 grocery.py").stdin("banana").stdin("orange").stdin("apple").stdout("banana, orange, apple.").exit(0)

@check50.check()
def test_sep():
    """Validate student used sep= in a print statement"""
    check50.run("grep 'print.*sep=' grocery.py").exit(0)

@check50.check()
def test_name():
    """First line should have a comment containing the student's first and last name"""
    check50.run("head -1 grocery.py").stdout("#\s*\w+\s+\w+")
