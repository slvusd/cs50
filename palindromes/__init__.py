import check50
import check50.c

@check50.check()
def exists():
    """palindromes.c exists"""
    check50.exists("palindromes.c")

@check50.check()
def compiles():
    """palindromes.c compiles"""
    check50.run("clang palindromes.c -o palindromes -std=c11 -ggdb -lm -lcs50")

@check50.check(compiles)
def my_mom_has_a_very_level_civic():
    """checks for palindromes"""
#    check50.run("./dc50 1 1 +").stdout("2").exit(0)
    check50.run("./palindromes").stdin("my mom has a very level civic\n").stdout("3").exit(0)
