from invoke import task
from sys import platform


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