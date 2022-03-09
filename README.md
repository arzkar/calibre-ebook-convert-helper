<h1 align="center">calibre-ebook-convert-helper</h1>

A helper script for calibre's ebook-convert CLI which is used to convert all files in an directory into another format.<br>

Calibre needs to be installed to use this script.<br>

Supported sites which are compatible with Calibre can be found here: https://manual.calibre-ebook.com/generated/en/ebook-convert.html<br>

To report issues for the CLI, open an issue at https://github.com/arzkar/calibre-ebook-convert-helper/issues

# Installation

## Dependencies

- Depends on [Calibre](https://github.com/kovidgoyal/calibre) so it needs to be installed in your system. Calibre can be download from [here](https://calibre-ebook.com/download).

- Depends on [Python](https://www.python.org/) so it needs to be installed in your system. Python can be installed from [here](https://www.python.org/downloads/)

  - Python packages: [tqdm](https://github.com/tqdm/tqdm) for progressbar and [colorama](https://github.com/tartley/colorama) for colored terminal text.
    Install using:

    ```
    pip install -r requirements.txt # if you cloned the project
    or
    pip install -U tqdm colorama
    ```

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
wget https://raw.githubusercontent.com/arzkar/calibre-ebook-convert-helper/main/ebook-convert-helper.py
```

- Using [curl](https://curl.se/):

```
curl -O https://raw.githubusercontent.com/arzkar/calibre-ebook-convert-helper/main/ebook-convert-helper.py
```

- From within the browser:
  - Go to this [page](https://raw.githubusercontent.com/arzkar/calibre-ebook-convert-helper/main/ebook-convert-helper.py)
  - Right Click and save the file using "Save Page as"
  - Make sure that the filename is `ebook-convert-helper.py`, not `.txt`

## Run

```
python3 ebook-convert-helper.py
```

# Usage

```
> python3 ebook-convert-helper.py --help
usage: ebook-convert-helper [-h] -i INPUT_FORMAT -o OUTPUT_FORMAT --dir
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
python3 ebook-convert-helper.py -i mobi -o azw3 --dir ~/Books
```

- To include all the sub-directories inside the `--dir` directory, use `--recursive`

```
python3 ebook-convert-helper.py -i mobi -o azw3 --dir ~/Books --recursive
```

- To delete the all the files with `-i, --input-format` i.e. `mobi`, use `--delete`

```
python3 ebook-convert-helper.py -i mobi -o azw3 --dir ~/Books --delete
```

- To ignore directories or files, use `--ignore` which will read the `.echignore` file from the root directory specified by `--dir` and exclude its contents

```
python3 ebook-convert-helper.py -i mobi -o azw3 --dir ~/Books --ignore
```

---

## Note

`.echignore` file needs to be in the root directory which is specified by `--dir`. Each directory or file needs to be in its own line and the path can either be relative or absolute.
