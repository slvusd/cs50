import check50
import check50.c

@check50.check()
def exists():
    """p.c exists"""
    check50.exists("p.c")

@check50.check()
def compiles():
    """p.c compiles"""
    #check50.run("make p")
    check50.c.compile("p.c", lcs50=True)

@check50.check(compiles)
def test1():
    """Outputs 1"""
    check50.run("./p").stdin("1\n").stdout("1").exit(0)
