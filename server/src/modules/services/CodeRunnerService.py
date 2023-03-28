import os
import subprocess
import sys
from subprocess import Popen, PIPE
import random, string


def randomword(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


def run(codeareadata):
    img = None

    # save original standart output reference
    code = codeareadata.decode()
    if code.find('plt.show()') >= 0:
        img = randomword(10)
        code = code.replace('plt.show()', "plt.savefig('imgs/" + img + ".png')")

    py = randomword(10)
    with open('tmp/' + py + '.py', 'w') as f:
        f.write(code)
        f.close()

    codeareadata = code.encode()
    original_stdout = sys.stdout

    out, err = Popen('python tmp/' + py + '.py', shell=True, stdout=PIPE).communicate()
    with open('file.txt', 'w') as f:  # change the standard output to the file we created
        f.write(out.decode())
        f.close()

    os.remove('tmp/' + py + '.py')

    output = open('file.txt', 'r').read()


# try:
# except Exception as e:
#     # to return error in the code
#     sys.stdout = original_stdout
#     output = e

    return {
        "result": output,
        "imgs": [img]
    }
