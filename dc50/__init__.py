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
    check50.run("clang palindromes.c -o palindromes -std=c11 -ggdb -lm -lcs50")

@check50.check(compiles)
def one_plus_one():
    """adds 1 plus 1"""
    check50.run("./dc50 1 1 +").stdout("2").exit(0)

@check50.check(compiles)
def three_minus_one():
    """subtract 1 from 3"""
    check50.run("./dc50 3 1 -").stdout("2").exit(0)

@check50.check(compiles)
def nineteen_modulo_three():
    """19 % 3"""
    check50.run("./dc50 19 3 %").stdout("1").exit(0)

