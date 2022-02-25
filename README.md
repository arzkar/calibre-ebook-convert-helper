<h1 align="center">calibre-ebook-convert-helper</h1>

A helper script for calibre's ebook-convert CLI which is used to convert all files in an directory into another format.<br>

Calibre needs to be installed to use this script.<br>

Supported sites which are compatible with Calibre can be found here: https://manual.calibre-ebook.com/generated/en/ebook-convert.html<br>

To report issues for the CLI, open an issue at https://github.com/arzkar/calibre-ebook-convert-helper/issues

# Installation

## Dependencies

- Depends on [Calibre](https://github.com/kovidgoyal/calibre) so it needs to be installed in your system. Calibre can be download from [here](https://calibre-ebook.com/download).

- Depends on [Python](https://www.python.org/) so it needs to be installed in your system. Python can be installed from [here](https://www.python.org/downloads/)

---

**NOTE:**
The script was developed using Python 3.8.5 so if you are using an older version than that, you might run into some issue. Python 3.7+ _should_ work fine.

---

## Download

There are many ways to download the script:

- Using [git](https://git-scm.com/downloads):

```
git clone https://github.com/arzkar/calibre-ebook-convert-helper
```

- Using [Wget](https://www.gnu.org/software/wget/):

```
wget https://raw.githubusercontent.com/arzkar/calibre-ebook-convert-helper/main/calibre-ebook-convert-helper.py
```

- Using [curl](https://curl.se/):

```
curl -O https://raw.githubusercontent.com/arzkar/calibre-ebook-convert-helper/main/calibre-ebook-convert-helper.py
```

- From within the browser:
  - Go to this [page](https://raw.githubusercontent.com/arzkar/calibre-ebook-convert-helper/main/calibre-ebook-convert-helper.py)
  - Right Click and save the file using "Save Page as"
  - Make sure that the filename is `calibre-ebook-convert-helper.py`, not `.txt`

## Run

```

python3 calibre-ebook-convert-helper.py

```

# Usage

```

> python3 calibre-ebook-convert-helper.py --help
usage: calibre-ebook-convert-helper [-h] -i INPUT_FORMAT -o OUTPUT_FORMAT --dir
                                    DIR [--delete-file] [-r] [--verbose] [--debug]
                                    [--log] [--version]

A helper script for calibre's ebook-convert CLI which is used to convert all files in an directory into another format.

Calibre needs to be installed to use this script.

Supported sites which are compatible with Calibre can be found here: https://manual.calibre-ebook.com/generated/en/ebook-convert.html

To report issues for the CLI, open an issue at https://github.com/arzkar/calibre-ebook-convert-helper/issues

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT_FORMAT, --input-format INPUT_FORMAT
                        Input format
  -o OUTPUT_FORMAT, --output-format OUTPUT_FORMAT
                        Output format
  --dir DIR             Absoulte Path to the directory
  --delete              Delete all the files with the Input format
  -r, --recursive       Convert all files from both the directory and its sub-directories
  --verbose             Show ebook-convert's stdout
  --debug               Show the log in console
  --log                 Generate a log file in the current directory
  --version             Display version & quit
```

---

## Example

- To convert all `mobi` files inside the directory `~/Books` into `azw3`

```

python3 calibre-ebook-convert-helper.py -i mobi -o azw3 --dir ~/Books

```

- To convert all `mobi` files inside the directory `~/Books` and all its sub-directories into `azw3`

```

python3 calibre-ebook-convert-helper.py -i mobi -o azw3 --dir ~/Books --recursive

```

- To convert all `mobi` files inside the directory `~/Books` into `azw3` and delete the `mobi` files.

```

python3 calibre-ebook-convert-helper.py -i mobi -o azw3 --dir ~/Books --delete

```
