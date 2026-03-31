from invoke import task
from sys import platform

# En itse oikein hoksannut miten saisin tämän onnistumaan,
# kun itselläni on käytössä Windows kone, mutta Claude generoi
# tämmöisen vaihtoehdoksi, joten toivon että se toimii!

# generoitu koodi alkaa
@task
def start(ctx):
    ctx.run("python3 src/index.py", pty=platform != "win32")

@task
def test(ctx):
    ctx.run("pytest src", pty=platform != "win32")

@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest src", pty=platform != "win32")

@task(coverage)
def coverage_report(ctx):
    ctx.run("coverage html", pty=platform != "win32")
# generoitu koodi päättyy