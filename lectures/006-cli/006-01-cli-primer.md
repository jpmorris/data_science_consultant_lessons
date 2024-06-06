# CLI Shortcuts and directory/command navigation

# Topic overview
- CLIs at HHSOIG
- CLI Commands
- Advanced topics

# CLIs at HHSOIG:
- On GFEs:
  - Cygwin
  - Git Bash
  - Windows Subsystem for Linux
- In AWS:
  - Sagemaker Jupyterlab
  - Sagemaker Code Editors
  - Self-Managed Jupyterlab
  - Cloud9
  - CloudShell
  - SSH into EC2 instances
- Containers:
  - Docker


# CLI commands 

## Advanced review of basics 
- Getting help
  - `man <command>` - Display the manual page for a command.
  - `<cmd> --help` - Display help information for a command.
  - Some commands have man pages some have help flags and some have both, few have neither
- `cp -r` - Copy directories recursively.
- `cp <file1> <file2> <file3> <destination>` - Copy multiple files to a destination.
- `cp <file> ~-`: Copy a file to the previous directory.
- `ls -lat` - List files in long format, hidden files, and sort by time.
- `rm -rf` - Remove files and directories recursively and forcefully.
  - You can use `rmdir` for directories, but `rm -rf` is universal, just be careful
  - `<ctrl + C>` to stop a command

## Moving around CLI/commands 

### commands
- `clear`: Clear the terminal screen.
- `Ctrl + l`: Clear the terminal screen.
- `pwd` - Print the current working directory.
- `!!`: Repeat the last command
  - `sudo !!`: important when you forget `sudo` in the last command
- `!<n>`: Repeat the nth command in the history (find n using `history`)
- `!string`: Repeat the last command that starts with the string.
- `!$`: Last argument of the last command.
- `^foo^bar`: Replace the first occurrence of `foo` with `bar` in the last command.
- `<ctrl+u>...<ctrl+y>`: interrupt and resume a command in progress
- `<alt>+.`: Insert the last argument of the last command.
- `fc`: Open the last command in the default text editor

### Tab completion
- `<TAB>`: Auto-complete the current command or file path
- Tab completion is a feature of the shell that allows the user to complete a command or file path
  by pressing the `Tab` key. 
- Tab completion can be used in many contexts files, directories, commands and sometimes arguments.
- If tab does not complete, this usually means that there is a typo in the command or file path
  (unless completion is not supported for that context).

### bash navigation shortcuts
- `Ctrl + a`:  Move to the beginning of the line.
- `Ctrl + e`:  Move to the end of the line.
- `Ctrl + u`:  Delete from the cursor to the beginning of the line.
- `Ctrl + k`:  Delete from the cursor to the end of the line.
- `Ctrl + w`:  Delete the word before the cursor.
- `Alt + b`:  Move back one word.
- `Alt + f`:  Move forward one word.

### reverse i-search - `Ctrl + r` In searching previous commands you have used in the past a common
one is

- `history | grep <string>`: Search the command history for a string

A built-in feature of the bash shell that allows the user to search through the command history by
typing a few characters and pressing `Ctrl + r`. This will search through the history for the most
recent command that matches the characters typed.

## Moving through directories

### commands
- `.` - The current directory.
- `..` - The parent directory.
  - `./<cmd>` - Run a command in the current directory.
  - `../<cmd>` - Run a command in the parent directory.
  - `<cmd>` - Run a command in the PATH.
- `~` - The home directory.
- `find . | grep <string>`: FIND A FILE -  Search for a file name recursively
- `grep <pattern> * -iR`: FIND A STRING IN A FILE - Search for a pattern in all files recursively
  (case-insensitive)
- `ln -s <source> <destination>`: CREATE A SYMLINK - Create a symbolic link to a file or directory.

### `ALT + Left` and `ALT + Right` Almost all shells can be configured to use the
`dirs`/`popd`/`pushd` tools via the `ALT + Left` and `ALT + Right` keys. This is a very useful
feature that allows the user to quickly navigate through the directory stack.

### popd `popd`/`pushd`/`dirs` are built-in shell commands that keeps an entire directory stack in
history for the session. This allows the user to pop off previously visited directories to return to
them.
- **popd** - Remove the top directory from the stack and cd into it.
- **pushd** - Push the current directory onto the stack and cd into the directory at the top of the
  stack.
- **dirs** - Display the directory stack.
- **dirs -c** - Clear the directory stack.
- **dirs -v** - Display the directory stack with index numbers.


## More advanced tools/commands

### fzf Fuzzy finder CLI tool that lets you search commands, directories, and programs After
configurting the following shortcuts are available:
- **Ctrl + r** - Search command history.
- **Ctrl + t** - Search files and directories.
- **Alt + c** - Change to a subdirectory.

### Other tools/commands to know 
- Great Reference: https://www.commandlinefu.com
- CLI commands can be
  - **built-in** - part of the shell itself.
  - **external but included** - standalone programs that are executed by the shell. 
  - **separate GNU tools** - standalone programs that are not part of the shell.
  - This distinction is not very important except to know that some of these tools will need to be
    installed and do not come by default
- Monitoring (log) files
  - `watch <cmd>` - Run a command repeatedly and display the output.
    - `watch -n 1 ls -lat` - Run `ls -lat` every second to watch for when a file appears or changes. 
- Viewing files/searching for patterns
  - `head -n <n> <file>` - Display the first `n` lines of a file.
  - `tail -n <n> <file>` - Display the last `n` lines of a file.
    - `tail -f <file>` - Display the last lines of a file and follow the file as it grows.
  - `cat <file>` - Display the contents of a file.
    - `cat <file> | grep <pattern>` - Display the contents of a file and search for a pattern.
    - `cat <file> | grep -v <pattern>` - Display the content of a file and exclude a pattern.
    - `cat <file> | egrep "<pattern1>|<pattern2>"` - Display the contents of a file and search for
      multiple patterns. 
    - egrep is the same as `grep -E` and allows for regular expressions.
  - `less <file>` - Display the contents of a file one page at a time.
  - `more <file>` - Display the contents of a file one page at a time.
- Space used/size:
  - `du --max-depth=1 --si` - Display the disk usage of the directories in the current directory  in
    human readable format. The max-depth flag will dictate at what level to sum the disk usage.
  - `df -h` - Display the disk usage of the file systems in human readable format.
- Changing ownership/permisisons
  - `chown <user>:<group> <file>` - Change the owner and group of a file.
  - `chmod <mode> <file>` - Change the permissions of a file.
    - `chmod 755 <file>` - Give the owner full permissions and everyone else read and execute
      permissions.
    - `chmod 644 <file>` - Give the owner full permissions and everyone else read permissions.
- Process management
  - `ps` - Display information about processes.
    - `ps aux` - Display all processes.
    - `ps aux | grep <process>` - Display all processes and search for a process.
  - `top` - Display a dynamic view of system processes.
  - `pkill <process_name>` - Kill a process by its name.
  - `kill <pid>` - Kill a process by its process ID.
    - `kill -9 <pid>` - Kill a process by its process ID forcefully.
  - `killall <process_name>` - Kill all processes with a given name.
  -`<ctrl + z>` - Suspend the current process.
  -`<ctral + c>` - Kill the current process.
  - `fg` - Bring the current process to the foreground.
  - `bg` - Send the current process to the background.
- Downloading files
  - `wget <url>` - Download a file from a URL.
  - `curl <url>` - Download a file from a URL.
    - Great tool for sending API requests
- Terminal session management
  - `tmux` - Create a new terminal session.
    - `tmux new -s <session_name>` - Create a new terminal session with a name.
    - `tmux attach -t <session_name>` - Reattach to a terminal session.
  - `screen` - Create a new terminal session.
    - `screen -r` - Reattach to a terminal session.
- `cat <file> | wc -l` - Count the number of lines in a file.


# (bash) programming from the CLI

## Common Shells
- **sh** - Bourne Shell - the original Unix shell.
- **bash** - Bourne Again Shell - the default shell on most Linux distributions.
- **zsh** - Z Shell - more modern and feature-rich than bash.
- **fish** - Friendly Interactive Shell - designed to be user-friendly and easy to use. Not
  POSIX-compliant.




## Redirecting output
- **command > file** - Redirect the output of a command to a file.
- **command >> file** - Append the output of a command to a file.
- **command < file** - Redirect the input of a command from a file.
- **command1 | command2** - Pipe the output of command1 to the input of command2.


## loops at cli

## important flags:
- **mkdir -p** - Create parent directories if they do not exist.
- **git commit -a** - Stage all changes and commit them.





