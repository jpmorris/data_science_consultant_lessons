# CLI Shortcuts and directory/command navigation

# Basics

## Which Shell
- **sh** - Bourne Shell - the original Unix shell.
- **bash** - Bourne Again Shell - the default shell on most Linux distributions.
- **zsh** - Z Shell - more modern and feature-rich than bash.
- **fish** - Friendly Interactive Shell - designed to be user-friendly and easy to use. Not POSIX-compliant.


## Tab completion
Tab completion is a feature of the shell that allows the user to complete a command or file path by pressing the `Tab` key. This can be used to complete the name of a command, file, or directory.

# Moving through directories

## popd
`popd`/`pushd`/`dirs` are built-in shell commands that keeps an entire directory stack in history for the session. This allows the user to pop off previously visited directories to return to them.
- **popd** - Remove the top directory from the stack and cd into it.
- **pushd** - Push the current directory onto the stack and cd into the directory at the top of the stack.
- **dirs** - Display the directory stack.
- **dirs -c** - Clear the directory stack.
- **dirs -v** - Display the directory stack with index numbers.
-

## reverse i-search - `Ctrl + r`
A built-in feature of the bash shell that allows the user to search through the command history by typing a few characters and pressing `Ctrl + r`. This will search through the history for the most recent command that matches the characters typed.

## fzf
Fuzzy finder CLI tool that lets you search commands, directories, and programs
After configurting the following shortcuts are available:
- **Ctrl + r** - Search command history.
- **Ctrl + t** - Search files and directories.
- **Alt + c** - Change to a subdirectory.

## `ALT + Left` and `ALT + Right`
Almost all shells can be configured to use the `dirs`/`popd`/`pushd` tools via the `ALT + Left` and `ALT + Right` keys. This is a very useful feature that allows the user to quickly navigate through the directory stack.

# Other 

## other CLI commands
- **<TAB>** - Auto-complete the current command or file path.
- **history** - Display the command history.
- **fc** - Open the last command in the default text editor.
- **!!** - Repeat the last command.
  - important when you forget `sudo` in the last command.
<!-- - **!n** - Repeat the nth command in the history. -->
- **!<n>** - Repeat the nth command before the last command.
- **!string** - Repeat the last command that starts with the string.
- **!$** - Last argument of the last command.
- **cp <file> ~-** - Copy a file to the previous directory.

- **Ctrl + a** - Move to the beginning of the line.
- **Ctrl + e** - Move to the end of the line.
- **Ctrl + u** - Delete from the cursor to the beginning of the line.
- **Ctrl + k** - Delete from the cursor to the end of the line.
- **Ctrl + w** - Delete the word before the cursor.
- **Alt + b** - Move back one word.
- **Alt + f** - Move forward one word.


## Ways to kill a process
- **Ctrl + c** - Kill the current process.
- **Ctrl + d** - Send an EOF signal to the current process.
- **kill -9 <pid>** - Kill a process by its process ID.
- **killall <process_name>** - Kill all processes with a given name.
- **pkill <process_name>** - Kill a process by its name.


## Background a process
- **Ctrl + z** - Background the current process.
- **bg** - Send the current process to the background.
- **fg** - Bring the current process to the foreground.

## Redirecting output
- **command > file** - Redirect the output of a command to a file.
- **command >> file** - Append the output of a command to a file.
- **command < file** - Redirect the input of a command from a file.
- **command1 | command2** - Pipe the output of command1 to the input of command2.

## pagers
- **more** - A pager that allows the user to scroll through the output of a command.
- **less** - like `more` but more feature-rich. 

## loops at cli

## important flags:
- **mkdir -p** - Create parent directories if they do not exist.
- **git commit -a** - Stage all changes and commit them.





