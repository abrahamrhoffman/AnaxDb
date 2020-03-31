import subprocess


def _check_version():
    f = open("../setup.py", "rb")
    data = f.read();f.close()
    data = data.splitlines()
    for ix, ele in enumerate(data):
        if ("version") in ele:
            ele = ele.split("=")[1]
            ele = ele.replace('"', '')
            ele = ele.replace(",", "")
            return ele

def build(version):
    cmd = ("docker build -t abehoffman/anaxdb-build:{} .".format(version))
    subprocess.call(cmd, shell=True)

def push(version):
    cmd = ("docker push docker.io/abehoffman/anaxdb-build:{}".format(version))
    subprocess.call(cmd, shell=True)

def stop():
    cmd = ("docker stop anaxdb-build")
    subprocess.call(cmd, shell=True)
    cmd = ("docker rm anaxdb-build")
    subprocess.call(cmd, shell=True)

def run(version):
    cmd = ("""docker run --rm \
                         --name anaxdb-build \
                         abehoffman/anaxdb-build:{}""".format(version))
    subprocess.call(cmd, shell=True)

def main():
    version = _check_version()
    build(version)
    push(version)
    stop()
    run(version)

if __name__ == "__main__":
    main()
