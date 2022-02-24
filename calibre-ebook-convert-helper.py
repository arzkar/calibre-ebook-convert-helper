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
        print(
            f"Directory: {args.dir} doesnt exist!\nPlease enter a valid directory path")
        if args.debug:
            logger.error(f"DirectoryNotFound: {args.dir}")
        exit(1)

    files = get_files(args, logger)
    convert_files(args, files, logger)

    if args.version is True:
        print("calibre-ebook-convert-helper: v0.1")
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
    files_list = []
    if args.recursive:
        if args.debug or args.log:
            logger.info(
                f"Searching for {args.input_format} files in the directory recursively")
        else:
            print(
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
            print(
                f"Searching for {args.input_format} files in the directory non-recursively")

        for item in os.listdir(args.dir):
            item_path = os.path.join(args.dir, item)
            if os.path.isfile(item_path):
                if item_path.endswith(f".{args.input_format}"):
                    files_list.append(item_path)

    if args.debug or args.log:
        logger.info(f"Files found: {len(files_list)}")
    else:
        print(f"Files found: {len(files_list)}\n")

    return files_list


def convert_files(args, files, logger):
    start_time = timeit.default_timer()
    avg_time = []
    printProgressBar(0, len(files), length=50)
    for i, input_file in enumerate(files):

        if args.debug or args.log:
            logger.info(f"Converting {input_file}")
        else:
            print(f"Converting {input_file}")

        filename = Path(input_file)
        output_file = filename.with_suffix(f".{args.output_format}")
        proc = subprocess.Popen(['ebook-convert', input_file, output_file],
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        time.sleep(0.1)

        if (i/len(files)*100) < 5:
            expected_time = "?"
        else:
            curr_time = timeit.default_timer()
            avg_time.append(curr_time-start_time)
            start_time = timeit.default_timer()  # reset start time

            expected_time = calc_expected_time(
                (sum(avg_time)/len(avg_time))*(len(files)-i))

        # Update Progress Bar
        printProgressBar(i + 1, len(files), length=50,
                         expected_time=expected_time)

        out, err = proc.communicate()

        if args.verbose:
            print(out.decode())

        # if the process return code is 0
        if proc.returncode == 0:
            if args.delete:
                if os.path.exists(output_file):
                    if args.debug or args.log:
                        logger.info(f"Deleting {input_file}")
                    else:
                        print(f"Deleting {input_file}")

                    # Delete the input file
                    os.remove(input_file)
        else:
            print(err.decode())

        if args.debug or args.log:
            logger.info(f"File converted to {output_file}")
        else:
            print(f"File converted to {output_file}\n")


def printProgressBar(iteration, total, decimals=1,
                     length=100, expected_time='?', fill='█'):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration       - Required  : current iteration (int)
        total           - Required  : total iterations (int)
        decimals        - Optional  : positive number of decimals in percent complete (int)
        length          - Optional  : character length of bar (int)
        expected_time   - Optional  : expected time of completion(str)
        fill            - Optional  : bar fill character (str)
    """
    percent = ("{0:." + str(decimals) + "f}") \
        .format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    status = f"{iteration}/{total}"

    sys.stdout.write(
        f'\r{percent}% |{bar}| {status}, ETA: {expected_time}\r')
    sys.stdout.flush()
    # Print new line on Complete


def calc_expected_time(seconds):
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60

    return "%02d:%02d:%02d" % (hour, minutes, seconds)


def init_logging(args):
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