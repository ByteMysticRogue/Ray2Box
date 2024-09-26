# Ray2Box

Ray2Box is a command-line tool designed to convert V2ray links into Singbox configuration files. This tool supports multiple V2ray link types such as vmess, vless, hysteria 2, shadowsocks, trojan, providing an easy and efficient way to generate Singbox configuration files.

## Table of Contents

- [Features](#features)
- [Usage](#usage)
- [Options](#options)
- [Example](#example)
- [Installation](#installation)
  - [From Source](#from-source)
  - [Building Executable](#building-executable)
- [Contributing and Reporting Issues](#contributing-and-reporting-issues)
  - [How to Report Issues](#how-to-report-issues)
- [License](#license)

## Features

- Convert multiple types of V2ray links to Singbox configuration.
- Supports input from URLs, files, or individual links.
- Generates JSON configuration files compatible with Singbox.
- Command-line tool for easy integration into scripts or automation.

## Usage

Ray2Box can be run from the command line with various input options.

### Basic Usage

You can use any one of the following options:

1. **Convert from a URL**:
   
    ```bash
    Ray2Box.exe --url <URL> --output <output_file>
    ```

2. **Convert from a file (.txt format only)**:

    ```bash
    Ray2Box.exe --file <file_path> --output <output_file>
    ```

3. **Convert from a single link**:

    ```bash
    Ray2Box.exe --link <V2ray_link> --output <output_file>
    ```

### Options

| Option               | Description                                          |
|----------------------|------------------------------------------------------|
| `-u`, `--url`        | Fetch configuration from a URL                       |
| `-f`, `--file`       | Read configuration from a `.txt` file only           |
| `-l`, `--link`       | Convert a single V2ray link                          |
| `-o`, `--output`     | Specify the output file name for the generated Singbox config. Simply provide the desired file name. |

### Example

```bash
python -m Cli.Ray2Box --file configs.txt --output singbox_config
```

## Installation

### From Source

To install and run `Ray2Box` from source, make sure you have Python 3.6 or later installed on your system.

1. Clone the repository:

    ```bash
    git clone https://github.com/ByteMysticRogue/Ray2Box.git
    cd Ray2Box
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Run the Program:
    
    Windows:

    ```bash
    python -m Cli.Ray2Box
    ```

    Linux:
    
    ```bash
    python3 -m Cli.Ray2Box
    ```

### Building Executable

If you want to create an executable binary for Windows, Linux, or macOS, you can use `Nuitka`.

1. Install Nuitkka:

    ```bash
    pip install nuitka
    ```

2. Build the executable:

    ```bash
    nuitka --standalone --onefile --follow-imports --include-package=requests --python-flag=-O Cli/Ray2Box.py
    ```

This will generate a single executable file (Ray2Box.exe or equivalent) in the `build` directory.

## Contributing and Reporting Issues

We welcome contributions and feedback from the community! If you encounter any problems or have ideas to improve the program, please consider the following:

### Report Issues

If you find any bugs or unexpected behavior while using the program, please submit an issue on the [GitHub Issue Tracker](https://github.com/ByteMysticRogue/Ray2Box/issues). When submitting an issue, include:

- A clear description of the problem.
- Steps to reproduce the issue.
- Any relevant error messages or screenshots.
- Information about your environment (operating system, Python version, etc.).

### Contributing to the Project

If you'd like to contribute code, documentation, or other improvements, please follow these steps:

### Support and Feedback

If you like this project, please consider giving it a ⭐.