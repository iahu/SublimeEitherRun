import sublime
import sublime_plugin

from subprocess import PIPE
from subprocess import Popen
from sys import version_info

if version_info[0] == 2:
  from utils import is_windows, get_proc_env
else:
  from .utils import is_windows, get_proc_env

class EitherRunCommand(sublime_plugin.TextCommand):
  def run(self, edit, cmd, resolve = None, reject = None):
    command = cmd.split(' ') if isinstance(cmd, str) else cmd
    proc = Popen(
        command, stdin=PIPE,
        stderr=PIPE,
        stdout=PIPE,
        env=get_proc_env(),
        shell=is_windows())

    stdout, stderr = proc.communicate()

    if proc.returncode == 0 and resolve:
      self.view.run_command(resolve)
    elif reject:
      self.view.run_command(reject)
