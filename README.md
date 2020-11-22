# SublimeEitherRun

either run a command or not depenend on an shell command output result

my use case is, checking a file added by myself on git, than to call jsPrettier format command.

it very like a JavaScript Promise version sublime run_command


# install

```sh
cd ~/Library/Application\ Support/Sublime\ Text/Packages/
git clone https://github.com/iahu/SublimeEitherRun.git EitherRun
```

# how to use

work with sublime-hooks

```js
{
  {
    "command": "either_run",
    "args": {
      "cmd": "git log --diff-filter=A --author=yourName", // required
      "resolve": "js_prettier", // optional, run if cmd return stdout
      "reject": "select_all" // optional, run if cmd return stderr
    }
  }
}
```
