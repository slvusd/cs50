import check50
import check50.c

@check50.check()
def exists():
    """p.c exists"""
    check50.exists("p.c")

@check50.check()
def compiles():
    """p.c compiles"""
    check50.c.compile("p.c")

@check50.check(compiles)
def test1():
    """Outputs 1"""
    check50.run("./p").stdout("1").exit(0)