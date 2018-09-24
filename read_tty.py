import io, os

tty = io.TextIOWrapper(
    io.FileIO(
        os.open(
            "/dev/ttyACM0",
            os.O_NOCTTY | os.O_RDWR),
        "r+"))

for line in iter(tty.readline, None):
    print(line.strip())
