import check50
import check50.c

@check50.check()
def exists():
    """mysort.c exists"""
    check50.exists("mysort.c")

@check50.check()
def compiles(exists):
    """mysort.c compiles"""
    check50.c.compile("mysort.c", lcs50=True)

@check50.check(compiles)
def square_size_4():
    """Sort small list"""
    check50.run("./mysort 4") \
        .stdin("4") \
        .stdin("-1") \
        .stdin("100") \
        .stdin("15") \
        .stdout("-1, 4, 15, 100")        
