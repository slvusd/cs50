import check50
import check50.c

@check50.check()
def exists():
    """palindromes.c exists"""
    check50.exists("palindromes.c")

@check50.check()
def compiles():
    """palindromes.c compiles"""
    check50.c.compile("palindromes.c")

@check50.check(compiles)
def my_mom_has_a_very_level_civic():
    """checks for palindromes"""
#    check50.run("./dc50 1 1 +").stdout("2").exit(0)
    check50.run("./palindromes").stdout("3").exit(0)
