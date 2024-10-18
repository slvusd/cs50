import check50
import check50.c

@check50.check()
def exists():
    """drop.c exists"""
    check50.exists("drop.c")

@check50.check()
def compiles():
    """drop.c compiles"""
    check50.c.compile("drop.c", lcs50=True)

@check50.check(compiles)
def drop_0():
    """basic average"""
    check50.run("./drop 3 0").stdin("100").stdin("90").stdin("80").stdout("average: 90").exit(0)

@check50.check(compiles)
def drop_1():
    """Drop lowest grade"""
    check50.run("./drop 4 1") \
        .stdin("100").stdin("90").stdin("80").stdin("70") \
            .stdout("average: 85").stdout("drops: 70").stdout("drop average: 90") \
                .exit(0)
