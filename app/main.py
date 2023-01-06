import getpass
import os
import shutil
import subprocess
import sys


def main():
    # run the command
    command = sys.argv[3]
    args = sys.argv[4:]

    # create temp dir & copy executable into temp dir
    temp_dir = '/home/temp'
    executable_file = '/usr/local/bin/docker-explorer'

    os.makedirs(f"{temp_dir}{os.path.dirname(executable_file)}", exist_ok=True)
    shutil.copy(executable_file, f"{temp_dir}{executable_file}")

    # chroot to temp dir
    os.chroot(temp_dir)

    completed_process = subprocess.run([command, *args], capture_output=True)

    sys.stdout.buffer.write(completed_process.stdout)
    sys.stderr.buffer.write(completed_process.stderr)

    if completed_process.returncode != 0:
        sys.exit(completed_process.returncode)


if __name__ == "__main__":
    main()
