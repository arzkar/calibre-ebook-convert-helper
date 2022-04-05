<h1 align="center">calibre-ebook-convert-helper</h1>

A helper CLI for calibre's ebook-convert CLI which is used to convert all files in an directory into another format.<br>

Calibre needs to be installed to use this CLI.<br>

Supported sites which are compatible with Calibre can be found here: https://manual.calibre-ebook.com/generated/en/ebook-convert.html<br>

To report issues for the CLI, open an issue at https://github.com/arzkar/calibre-ebook-convert-helper/issues

# Installation

## From pip (Recommended)

```
pip install -U ebook-convert-helper
```

## From Github Source (Pre-release, for testing new features by Beta testers)

```
pip install git+https://github.com/arzkar/calibre-ebook-convert-helper@main
```

# Usage

```
> ebook-convert-helper --help
usage: ebook-convert-helper [-h] -i INPUT_FORMAT -o OUTPUT_FORMAT --dir
                                    DIR [--delete-file] [-r] [--verbose] [--debug]
                                    [--log] [--version]

A helper CLI for calibre's ebook-convert CLI which is used to convert all files in an directory into another format.

Calibre needs to be installed to use this CLI.

Supported sites which are compatible with Calibre can be found here: https://manual.calibre-ebook.com/generated/en/ebook-convert.html

To report issues for the CLI, open an issue at https://github.com/arzkar/calibre-ebook-convert-helper/issues

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT_FORMAT, --input-format INPUT_FORMAT
                        Input format
  -o OUTPUT_FORMAT, --output-format OUTPUT_FORMAT
                        Output format
  --dir DIR             Absolute Path to the directory
  --delete              Delete all the files containing the Input format
  -r, --recursive       Convert all files from both the directory and its sub-directories
  --ignore              Read directories or files from .echignore which will be excluded from the conversion
  --verbose             Show ebook-convert's stdout
  --debug               Show the log in console
  --log                 Generate a log file in the current directory
  --version             Display version & quit
```

---

## Example

- To convert all `mobi` files inside the directory `~/Books` into `azw3`

```
ebook-convert-helper -i mobi -o azw3 --dir ~/Books
```

- To include all the sub-directories inside the `--dir` directory, use `--recursive`

```
ebook-convert-helper -i mobi -o azw3 --dir ~/Books --recursive
```

- To delete the all the files with `-i, --input-format` i.e. `mobi`, use `--delete`

```
ebook-convert-helper -i mobi -o azw3 --dir ~/Books --delete
```

- To ignore directories or files, use `--ignore` which will read the `.echignore` file from the root directory specified by `--dir` and exclude its contents

```
ebook-convert-helper -i mobi -o azw3 --dir ~/Books --ignore
```

---

## Note

`.echignore` file needs to be in the root directory which is specified by `--dir`. Each directory or file needs to be in its own line and the path can either be relative or absolute.
