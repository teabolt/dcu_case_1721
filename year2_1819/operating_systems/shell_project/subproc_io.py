import subprocess
import sys



def main():
    old_stdin = sys.stdin
    sys.stdin = open('subproc_in')
    old_stdout = sys.stdout
    sys.stdout = open('subproc_out', 'w')

    r = subprocess.run(['python3', 'subproc_child.py'], stdin=None, stdout=None)


if __name__ == '__main__':
    main()