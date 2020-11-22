# SublimeEitherRun

either run a command or not depenend on an shell command output result

my use case is, checking a file added by myself on git, than to call jsPrettier format command.

it very like a JavaScript Promise version sublime run_command

# how to use

work with sublime-hooks

```js
{
  {
    "command": "either_run",
    "args": {
      "cmd": "git log --diff-filter=A --author=yourName",
      "resolve": "js_prettier"
    }
  }
}
```
