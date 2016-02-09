# xode-toggle

CLI tool for fast switching between Xcode versions

## Features

* Switch between Xcode interactively or via "toggling" between all installed versions
* Finds all Xcodes installed in /Applications
* Will automatically invoke `sudo` so you don't have to remember
* Interactively select a Swift toolchain and automatically spawn a new shell session configured for it

## Installation

If you don't mind polluting your system's python install with junk:

```sh
sudo pip install git+https://github.com/schwa/xcode-toggle.git
```

If you know how to add `Library/Python/2.7/bin/` to your shell's `PATH`:

```sh
sudo pip install --user git+https://github.com/schwa/xcode-toggle.git
```

If you know how to use virtualenv (preferred) then good for you, but you don't need instructions.

## Usage

```sh
schwa@mote ~> xcode-toggle --help
Usage: xcode-toggle [OPTIONS] [PATH]...

Options:
  -p, --print        Print current select Xcode path
  -l, --list         List all found Xcode paths
  -t, --toggle       Toggle between all Xcode paths
  -i, --interactive  Select Xcode interactively
  -s, --select       Select Xcode manually
  -x, --toolchains   Select Swift toolchains interactively
  --help             Show this message and exit.
```

[Here](http://schwa.github.io/xcode-toggle/Session_1.html) is xcode-toggle in action.
