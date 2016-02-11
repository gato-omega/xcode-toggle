# xode-toggle

CLI tool for fast switching between Xcode versions

## Features

* Switch between Xcode interactively or via "toggling" between all installed versions
* Finds all Xcodes installed in /Applications
* Will automatically invoke `sudo` so you don't have to remember
* Interactively select a Swift toolchain and automatically spawn a new shell session configured for it

## Installation

```sh
pip install git+https://github.com/chrisschreiner/xcode-toggle.git
```

## Usage

```sh
schwa@mote ~> xcode-toggle --help
Usage: xcode-toggle [OPTIONS] [PATH]...

    Tool for fast switching between Xcode versions.

    The '--list' command is the default behaviour.
    
Options:
  -v, --version      Show version information
  -p, --print        Print current select Xcode path
  -l, --list         List all found Xcode paths
  -t, --toggle       Toggle between all Xcode paths
  -i, --interactive  Select Xcode interactively
  -s, --select       Select Xcode manually
  -x, --toolchains   Select Swift toolchains interactively
  --help             Show this message and exit
```

[Here](http://schwa.github.io/xcode-toggle/Session_1.html) is xcode-toggle in action.
