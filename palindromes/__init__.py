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

@check50.check(check)
def My_mom_has_a_very_level_civic():
    """checks for palindromes"""
    check50.run("./palindromes")
    check50.run("My mom has a very level civic.").stdout()

from re import match
 
expected = "3"
actual = check50.run("python3 hello.py").stdout()
if not match(expected, actual):
help = None
if match(expected[:-1], actual):
help = r"not all palindromes listed or too many"
raise check50.Mismatch("3", actual, help=help)


@check50.check(compiles)
def My_mom_has_a_very_level_civic():
    """checks for palindromes"""
    check50.run("./palindromes")
    check50.run("My mom has a very level civic.").stdout("3").exit(0)

@check50.check(compiles)
def Did_my_mom_have_a_kayak():
    """checks for palindromes"""
    check50.run("Did my mom have a kayak?").stdout("3").exit(0)

@check50.check(compiles)
def How_was_your_day_today():
    """checks for palindromes"""
    check50.run("How was your day today?").stdout("0").exit(0)

@check50.check(compiles)
def My_cats_nickname_is_Tacocat():
    """checks for palindromes"""
    check50.run("My cats nickname is Tacocat.").stdout("1").exit(0)

@check50.check(compiles)
def The_radar_deified_to_sign_the_deed():
    """checks for palindromes"""
    check50.run("The radar deified to sign the deed!").stdout("3").exit(0)

@check50.check(compiles)
def The_murdrum_wore_a_bib():
    """checks for palindromes"""
    check50.run("The murdrum wore a bib.").stdout("2").exit(0)
