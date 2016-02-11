#!/usr/bin/python3

import subprocess
import os
from pathlib import Path
from blessings import Terminal
import click
from _version import __version__

__author__ = 'schwa'

term = Terminal()

def print_version(ctx, param, value):
    if not value or ctx.resilient_parsing:
        return
    click.echo('{}, version {}'.format("xcode-toggle", __version__))
    ctx.exit()


@click.command()
@click.option('--version', '-v', is_flag=True, callback=print_version,
              expose_value=False, is_eager=True, help="Show version information")
@click.option("-p", "--print", "command", flag_value="print", help="Print current select Xcode path")
@click.option("-l", "--list", "command", flag_value="list", help="List all found Xcode paths")
@click.option("-t", "--toggle", "command", flag_value="toggle", help="Toggle between all Xcode paths")
@click.option("-i", "--interactive", "command", flag_value="ask", help="Select Xcode interactively")
@click.option("-s", "--select", "command", flag_value="select", help="Select Xcode manually")
@click.option("-x", "--toolchains", "command", flag_value="toolchains", help="Select Swift toolchains interactively")
@click.argument("path", nargs=-1)
def main(command, path):
    """
    Tool for fast switching between Xcode versions.

    The '--list' command is the default behaviour.
    """
    if command == "print":
        click.echo(get_current_path())
    elif command in [None, "list"]:
        list_paths()
    elif command == "toggle":
        paths = get_paths()
        current_path = get_current_path()
        index = paths.index(current_path)
        next_path = paths[(index + 1) % len(paths)]
        click.echo("Switching to: {t.bold}{path}{t.normal}".format(t=term, path=next_path))
        subprocess.check_call(["/usr/bin/sudo", "/usr/bin/xcode-select", "-s", str(next_path)])
        list_paths()
    elif command == "ask":
        current_path = get_current_path()
        xcode_paths = get_paths()
        for index, path in enumerate(xcode_paths):
            if current_path == path:
                click.echo("[{index}] {path} {t.bold}[Current]{t.normal}".format(t=term, index=index, path=path))
            else:
                click.echo("[{index}] {path}".format(t=term, index=index, path=path))
        option = input("Enter a number: ")
        option = int(option)
        next_path = xcode_paths[option]
        subprocess.check_call(["/usr/bin/sudo", "/usr/bin/xcode-select", "-s", str(next_path)])
        list_paths()
    elif command == "toolchains":
        # $ export PATH=/Library/Developer/Toolchains/swift-latest.xctoolchain/usr/bin:"${PATH}"
        shell_path = Path(os.environ["SHELL"])
        toolchains_path = Path("/Library/Developer/Toolchains")
        paths = list(toolchains_path.glob("*"))
        path = choose(paths)
        click.echo("Using {}".format(path))
        os.environ["PATH"] += ":{}/usr/bin".format(path)
        os.system(str(shell_path))

    else:
        raise Exception("Unknown command: ", command)


def choose(items, current=None):
    for index, item in enumerate(items):
        if current == item:
            click.echo("[{index}] {item} {t.bold}[Current]{t.normal}".format(t=term, index=index, item=item))
        else:
            click.echo("[{index}] {item}".format(t=term, index=index, item=item))
    option = input("Enter a number: ")
    option = int(option)
    return items[option]


def list_paths():
    current_path = get_current_path()
    xcode_paths = get_paths()
    for path in xcode_paths:
        if current_path == path:
            click.echo("{path} {t.bold}[Current]{t.normal}".format(t=term, path=path))
        else:
            click.echo("{path}".format(t=term, path=path))


def get_paths():
    output = subprocess.check_output(["/usr/bin/mdfind",
                                      'kMDItemCFBundleIdentifier="com.apple.dt.Xcode" and kMDItemContentType="com.apple.application-bundle"'])
    output = output.strip()
    paths = [Path(path) for path in output.decode("utf-8").split("\n")]
    return sorted(paths)


def get_current_path():
    current_path = Path(subprocess.check_output(["/usr/bin/xcode-select", "-p"]).decode("utf-8"))
    for index, part in enumerate(current_path.parts):
        if Path(part).suffix == ".app":
            return Path(*current_path.parts[:index + 1])
    return None


if __name__ == '__main__':
    # sys.argv[1:] = ["-a"]
    main()
