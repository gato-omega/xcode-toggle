#!/usr/bin/env python

import subprocess

from pathlib import Path
from blessings import Terminal
import click

__author__ = 'schwa'

term = Terminal()


@click.command()
@click.option("-p", "--print", "command", flag_value="print", help="Print current select Xcode path")
@click.option("-l", "--list", "command", flag_value="list", help="List all found Xcode paths")
@click.option("-t", "--toggle", "command", flag_value="toggle", help="Toggle between all Xcode paths")
@click.option("-i", "--interactive", "command", flag_value="ask", help="Select Xcode interactively")
@click.option("-s", "--select", "command", flag_value="select", help="Select Xcode manually")
@click.argument("path", nargs=-1)
def main(command, path):
    if command == "print":
        print get_current_path()
    elif command == "list":
        list_paths()
    elif command == "toggle":
        paths = get_paths()
        current_path = get_current_path()
        index = paths.index(current_path)
        next_path = paths[(index + 1) % len(paths)]
        print "Switching to: {t.bold}{path}{t.normal}".format(t=term, path=next_path)
        subprocess.check_call(["/usr/bin/sudo", "/usr/bin/xcode-select", "-s", str(next_path)])
        list_paths()
    elif command == "ask":
        current_path = get_current_path()
        xcode_paths = get_paths()
        for index, path in enumerate(xcode_paths):
            if current_path == path:
                print "[{index}] {path} {t.bold}[Current]{t.normal}".format(t=term, index=index, path=path)
            else:
                print "[{index}] {path}".format(t=term, index=index, path=path)
        option = input("Enter a number: ")
        option = int(option)
        next_path = xcode_paths[option]
        subprocess.check_call(["/usr/bin/sudo", "/usr/bin/xcode-select", "-s", str(next_path)])
        list_paths()
    elif command == "select":
        subprocess.call(["/usr/bin/sudo", "/usr/bin/xcode-select", "-s", path[0]])
    else:
        pass


def list_paths():
    current_path = get_current_path()
    xcode_paths = get_paths()
    for path in xcode_paths:
        if current_path == path:
            print "{t.bold}{path} {t.red}[Current]{t.normal}".format(t=term, path=path)
        else:
            print "{path}".format(t=term, path=path)


def get_paths():
    output = subprocess.check_output(["/usr/bin/mdfind", 'kMDItemCFBundleIdentifier="com.apple.dt.Xcode" and kMDItemContentType="com.apple.application-bundle"'])
    output = output.strip()
    paths = [Path(path) for path in output.split("\n")]
    return sorted(paths)


def get_current_path():
    current_path = Path(subprocess.check_output(["/usr/bin/xcode-select", "-p"]))
    for index, part in enumerate(current_path.parts):
        if Path(part).suffix == ".app":
            return Path(*current_path.parts[:index + 1])
    return None


if __name__ == '__main__':
    # sys.argv[1:] = ["-a"]
    main()
