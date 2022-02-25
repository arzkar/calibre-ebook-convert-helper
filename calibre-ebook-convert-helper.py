# Copyright 2022 Arbaaz Laskar

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#   http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import timeit
import time
import logging
from pathlib import Path
import subprocess
import os
import sys
import argparse
from tqdm import tqdm

bar_format = "{l_bar}{bar}| {n_fmt}/{total_fmt}, {rate_fmt}{postfix}, ETA: {remaining}"


def main(argv=None):

    if argv is None:
        argv = sys.argv[1:]

    parser = create_parser()
    args = parser.parse_args(argv)
    logger = init_logging(args)

    # if no args is given, invoke help
    if len(argv) == 0:
        parser.print_help(sys.stderr)
        sys.exit(1)

    if not os.path.isdir(args.dir):
        tqdm.write(
            f"Directory: {args.dir} doesnt exist!\nPlease enter a valid directory path")
        if args.debug:
            logger.error(f"DirectoryNotFound: {args.dir}")
        exit(1)

    files = get_files(args, logger)
    convert_files(args, files, logger)

    if args.version is True:
        tqdm.write("calibre-ebook-convert-helper: v0.1")
        sys.exit(0)


def create_parser():
    parser = argparse.ArgumentParser(prog='calibre-ebook-convert-helper',
                                     description="""
A helper script for calibre's ebook-convert CLI which is used to convert all files in an directory into another format.

Calibre needs to be installed to use this script.

Supported sites which are compatible with Calibre can be found here: https://manual.calibre-ebook.com/generated/en/ebook-convert.html

To report issues for the CLI, open an issue at https://github.com/arzkar/calibre-ebook-convert-helper/issues
""", formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument("-i", "--input-format", type=str,
                        required=True, help="Input format")

    parser.add_argument("-o", "--output-format", type=str,
                        required=True, help="Output format")

    parser.add_argument("--dir",  type=str,
                        required=True, help="Absoulte Path to the directory")

    parser.add_argument("--delete", action='store_true',
                        help="Delete all the files with the Input format")

    parser.add_argument("-r", "--recursive", action='store_true',
                        help="Convert all files from both the directory and its sub-directories")

    parser.add_argument("--verbose", action='store_true',
                        help="Show ebook-convert's stdout")

    parser.add_argument("--debug", action='store_true',
                        help="Show the log in console")

    parser.add_argument("--log", action='store_true',
                        help="Generate a log file in the current directory")

    parser.add_argument("--version", action='store_true',
                        help="Display version & quit")
    return parser


def get_files(args, logger):
    """
    Travserse through the directory and get a list of files to convert
    """
    files_list = []
    if args.recursive:
        if args.debug or args.log:
            logger.info(
                f"Searching for {args.input_format} files in the directory recursively")
        else:
            tqdm.write(
                f"Searching for {args.input_format} files in the directory recursively")

        for path, _, files in os.walk(args.dir):
            for file in files:
                file_path = os.path.join(path, file)
                if file_path.endswith(f".{args.input_format}"):
                    if os.path.exists(file_path):
                        files_list.append(file_path)

    else:
        if args.debug or args.log:
            logger.info(
                f"Searching for {args.input_format} files in the directory non-recursively")
        else:
            tqdm.write(
                f"Searching for {args.input_format} files in the directory non-recursively")

        for item in os.listdir(args.dir):
            item_path = os.path.join(args.dir, item)
            if os.path.isfile(item_path):
                if item_path.endswith(f".{args.input_format}"):
                    files_list.append(item_path)

    if args.debug or args.log:
        logger.info(f"Files found: {len(files_list)}")
    else:
        tqdm.write(f"Files found: {len(files_list)}\n")

    return files_list


def convert_files(args, files, logger):
    """
    Loop through the files and convert each of them sequentially
    """

    with tqdm(total=len(files), ascii=False,
              unit="file", bar_format=bar_format) as pbar:
        if len(files) == 0:
            if args.debug or args.log:
                logger.info("No files to convert!")
            else:
                tqdm.write("No files to convert!")

        for input_file in files:

            if args.debug or args.log:
                logger.info(f"Converting {input_file}")
            else:
                tqdm.write(f"Converting {input_file}")

            filename = Path(input_file)
            output_file = filename.with_suffix(f".{args.output_format}")

            proc = subprocess.Popen(['ebook-convert', input_file, output_file],
                                    stdout=subprocess.PIPE, stderr=subprocess.PIPE)

            out, err = proc.communicate()

            if args.verbose:
                tqdm.write(out.decode())

            # if the process return code is 0
            if proc.returncode == 0:
                # if the newly converted file exists
                if os.path.exists(output_file):
                    if args.delete:
                        if args.debug or args.log:
                            logger.info(f"Deleting {input_file}")
                        else:
                            tqdm.write(f"Deleting {input_file}")

                        # Delete the input file
                        os.remove(input_file)
            else:
                tqdm.write(err.decode())

            if args.debug or args.log:
                logger.info(f"File converted to {output_file}")
            else:
                tqdm.write(f"File converted to {output_file}\n")

            # update the progressbar
            pbar.update(1)


def init_logging(args):
    """
    Initilize logging, with StreamHandler and FileHandler if specified
    """
    logger = logging.getLogger('calibre-ebook-convert-helper')
    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
        '%(asctime)s - %(levelname)s - %(message)s')

    if args.debug:
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

    if args.log:
        log_file = os.path.join(args.dir, 'calibre-ebook-convert-helper.log')
        file_handler = logging.FileHandler(
            filename=log_file, mode='a')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    logger.info("Initialized logging")
    return logger


if __name__ == "__main__":
    main()
