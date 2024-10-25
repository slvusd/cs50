import check50
import check50.c

@check50.check()
def exists():
    """password.c exists"""
    check50.exists("password.c")

@check50.check()
def compiles():
    """password.c compiles"""
    check50.c.compile("password.c", lcs50=True)

@check50.check(compiles)
def very_weak():
    """checks for a very weak password"""
    check50.run("./password.c pass").stdout("Very Weak").exit(0)

@check50.check(compiles)
def weak():
    """checks for a weak password"""
    check50.run("./password.c password").stdout("Weak").exit(0)

@check50.check(compiles)
def fair():
    """checks for a fair password"""
    check50.run("./password.c 3l3phant!").stdout("Fair").exit(0)

@check50.check(compiles)
def strong():
    """checks for a strong password"""
    check50.run("./password.c :hlH|8i1I\4}").stdout("Strong").exit(0)

@check50.check(compiles)
def very_strong():
    """checks for a very strong password"""
    check50.run("./password.c 5k1bidi_Riz2-0HiO").stdout("Very Strong").exit(0)
