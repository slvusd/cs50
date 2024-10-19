import check50
import check50.c

@check50.check()
def exists():
    """square.c exists"""
    check50.exists("square.c")

@check50.check()
def compiles(exists):
    """square.c compiles"""
    check50.c.compile("square.c", lcs50=True)

@check50.check(compiles)
def square_size_4():
    """Square of size 4"""
    check50.run("./square").stdin("4") \
        .stdout("####") \
        .stdout("#  #") \
        .stdout("#  #") \
        .stdout("####") \
        .exit(0)
        

@check50.check(compiles)
def square_validate_input():
    """Validate square input"""
    check50.run("./square") \
        .stdin("0") \
        .stdin("-1") \
        .stdin("9") \
        .stdin("2") \
            .stdout("##").stdout("##") \
            .exit(0)

@check50.check(compiles)
def square_1():
    """Size of 1 works"""
    # Might need to validate that we don't get a second line of output
    check50.run("./square") \
        .stdin("1") \
            .stdout("#") \
            .exit(0)
