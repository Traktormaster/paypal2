import subprocess
from dataclasses import dataclass


@dataclass
class ServerProc:
    proc: subprocess.Popen
    url: str
