import os
import subprocess
import time


BLOCK_SIZE = 4096
MIN_AGE = time.time() - 86400 * 7


def removesuffix(s, suf):  # Until python 3.9
    return s[:len(s) - len(suf)] if s.endswith(suf) else s


def truncated(log):
    return subprocess.run(['bunzip2', '--test', log], stderr=subprocess.DEVNULL).returncode == 2


def main():
    for d, _, files in os.walk(os.environ.get('NIX_LOG_DIR', '/nix/var/log/nix')):
        for f in files:
            path = os.path.join(d, f)
            st = os.stat(path)
            if (st.st_size % BLOCK_SIZE) == 0 and st.st_mtime > MIN_AGE and truncated(path):
                print(d[-2:] + removesuffix(f, '.bz2'))


if __name__ == '__main__':
    main()
