import check50
import check50.c

@check50.check()
def exists():
    """palindromes.c exists"""
    check50.exists("palindromes.c")

@check50.check()
def compiles():
    """palindromes.c compiles"""
    check50.c.compile("palindromes.c", lcs50=True)

@check50.check(compiles)
def my_mom_has_a_very_level_civic():
    """checks for palindromes"""
#    check50.run("./dc50 1 1 +").stdout("2").exit(0)
    check50.run("./palindromes").stdin("my mom has a very level civic.").stdout("3\n").exit(0)

@check50.check(compiles)
def did_my_mom_have_a_kayak():
    """checks for palindromes"""
    check50.run("./palindromes").stdin("Does my mom have a kayak?").stdout("2\n").exit(0)

@check50.check(compiles)
def How_was_your_day_today():
    """checks for palindromes"""
    check50.run("./palindromes").stdin("How was your day today, how was your race, I heard your racecar broke?").stdout("1\n").exit(0)

@check50.check(compiles)
def My_cats_nickname_is_Tacocat():
    """checks for palindromes"""
    check50.run("./palindromes").stdin("My cats nickname is Tacocat, because he loves tacos!").stdout("1\n").exit(0)

@check50.check(compiles)
def The_radar_deified_to_sign_the_deed():
    """checks for palindromes"""
    check50.run("./palindromes").stdin("bob deified to sign the deed to sign away his radar.").stdout("4\n").exit(0)

@check50.check(compiles)
def The_murdrum_wore_a_bib():
    """checks for palindromes"""
    check50.run("./palindromes").stdin("The murdrum wore a bib.").stdout("2\n").exit(0)
