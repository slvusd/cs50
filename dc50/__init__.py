import check50
import check50.c

@check50.check()
def exists():
    """dc50.c exists"""
    check50.exists("dc50.c")

@check50.check()
def compiles():
    """dc50.c compiles"""
    check50.c.compile("dc50.c")

@check50.check(compiles)
def one_plus_one():
    """adds 1 plus 1"""
    check50.run("./dc50 1 1 +").stdout("2").exit(0)

