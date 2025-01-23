# VSCODE PRIMER

# Explore of first level of interface.

- `CTRL+SHIFT+P` - Command Palette
- `CTRL+P` - Quick Open

# USER GUIDE

## Editing

### Keyboard shortcuts - IMPORTANT

- There are so many keyboard shortcuts for almost any action
- The file `keybindings.json` can be used to customize the shortcuts.
  - Look to the top right buttons to switch between GUI and JSON view.

### Multiple selections (multi-cursor)

You can add secondary cursors with `Alt+Click` or `Alt+Shift+Down/Up`.

```
The quick brown fox jumps over the lazy dog.
    The quick brown fox jumps over the lazy dog.
        The quick brown fox jumps over the lazy dog.
            The quick brown fox jumps over the lazy dog.
```

#### Shrink/expand selection

Very useful to limit the code selection of a giant file.

```cpp
namespace Hello {
    namespace World {
        class HelloWorld {
            public:
                void sayHello() {
                    std::cout << "Hello, World!" << std::endl;
                }
        };
    }
}
```

### Column (box) selection

Can select a section with `Shift+Alt` and click-select.

```
//Key                   Character       Virtual Key Code
//Ctrl+Shift+Alt+Up     Arrow ↑         38
//Ctrl+Shift+Alt+Down   Arrow ↓         40
//Ctrl+Shift+Alt+Left   Arrow ←         37
//Ctrl+Shift+Alt+Right  Arrow →         39

```

[//]: <> (#### Column Selection mode)

### Save / Auto Save - IMPORTANT

- Essential feature to continually save without having to remember.
  - The default is to save 1 second
- History of all local saves is saved and can be viewed.

### Hot Exit

- By default VS remembers all unsaved changesto files when you exit.

### Find and Replace

- Essential feature of any editor that allows you to search and replace all text or step through and
  replace one by one.

#### Seed Search String From Selection

- Defaults search to selected word

#### Find In Selection

- You can limit your search to only the selection

#### Advanced find and replace options

- You can use regex and other advanced options

#### Multiline support and Find Widget resizing

- You can search for multiline strings and resize the find widget

### Search across files - IMPORTANT

- An essential feature to search across all files in a project.
- This is key to find particular line in a code base and trace back logic across several files.

#### Advanced search options

- Allows you to limit the global search to particular directories or file types.

#### Search and replace

- You can also search and replace across all files.

#### Case changing in regex replace

- Search and replace supports regex

### Search Editor

- Search Editor allows you to see search results in a full-sized window with surrounding context
- Use the `Open Search Editor` command.
<!--

#### Search Editor commands and arguments

#### Search Editor context default

#### Reuse last Search Editor configuration

-->

### IntelliSense - IMPORTANT

- IntelliSense is the code completion feature that provides context-aware suggestions as you type.
- You can hover over a keyword to see the documentation.

### Formatting - IMPORTANT

- VSCode allows for formatting by command or on save.
- You can also format a selection.
- Advanced teams should establish code standard norms and enable auto formatting as part of a
  githook.
  - This will ensure that changes to the code found in diffs or in git history reflect substantive
    changes and not just formatting changes.

### Folding

- You can fold code blocks to make it easier to read and concentrate only on the code that is
  relevant for your current task.

<u>Other shortcuts</u>

- Fold (`Ctrl+Shift+[`) folds the innermost uncollapsed region at the cursor.
- Unfold (`Ctrl+Shift+]`) unfolds the collapsed region at the cursor.
- Toggle Fold (`Ctrl+K Ctrl+L`) folds or unfolds the region at the cursor.
- Fold Recursively (`Ctrl+K Ctrl+[`) folds the innermost uncollapsed region at the cursor and all
  regions inside that region.
- Unfold Recursively (`Ctrl+K Ctrl+]`) unfolds the region at the cursor and all regions inside that
  region.
- Fold All (`Ctrl+K Ctrl+0`) folds all regions in the editor.
- Unfold All (`Ctrl+K Ctrl+J`) unfolds all regions in the editor.
- Fold Level X (`Ctrl+K Ctrl+2 for level 2`) folds all regions of level X, except the region at the
  current cursor position.
- Fold All Block Comments (`Ctrl+K Ctrl+/`) folds all regions that start with a block comment token.

#### Fold selection

- You can fold a selection of code.
- There are also plenty of other shortcuts for different folding commands.

<!--
### Indentation
#### Auto-detection

### File encoding support
### Overtype mode
-->

### Compare files - IMPORTANT

The `diff`ing capabilities of VSCode are very powerful.

- You can compare files during git merges, in your history, or just to compare two arbitrary files.

# Extensions

- VSCode has a extendable extension system that allows you to add new features to the editor.
- Wikipedia used to list VSCode as merely a 'text editor' because stock VSCode has few language
  specific features until you install extensions.
  - This means that you must instal (several) python extensions to get the full python experience.

Great (non-OS) extensions:

- Vim/Neovim - for even more powerful editing and navigation
- Git Pull Request - allows you to get a link to the github code and create and handle pull requests
- Peacock - allows you to color code your editor to easily distinguish between different projects
- Copilot - AI code completion
- SQL Notebooks - allows you to run SQL queries and edit in a notebook format
- AWS Toolkit - allows you to interact with AWS services directly from the editor
- PostgreSQL - allows you to interact with Postgres databases directly from the editor
- Docker - allows you to interact with Docker containers directly from the editor
- Black - autoformatter for python
- Ruff - autoformatter for python
- Code Spell Checker - spell checker
- Prettier - autoformatter for many languages
- GitLens - allows you to see git history and blame directly in the editor

## IntelliSense

### IntelliSense for your programming language

### IntelliSense features

### Types of completions

### Customizing IntelliSense

#### Settings

#### Tab Completion

#### Locality Bonus

#### Suggestion selection

#### Snippets in suggestions

#### Key bindings

### Enhance completions with AI

### Troubleshooting

### Next steps

### Common questions

#### Why am I not getting any suggestions?

#### Why am I not seeing method and variable suggestions?

## Code Navigation

### Quick file navigation

### Breadcrumbs

#### Breadcrumb customization

#### Symbol order in Breadcrumbs

#### Breadcrumb keyboard navigation

### Go to Definition

### Go to Type Definition

### Go to Implementation

### Go to Symbol

### Open symbol by name

### Peek

### Bracket matching

#### Bracket Pair Colorization

### Reference information

### Rename symbol

### Errors & warnings

### Code Action

### Inlay Hints

### Outgoing link protection

### Next steps

### Common questions

#### How can I automatically select the second entry in Quick Open instead of the first?

#### How can I configure Ctrl+Tab to navigate across all editors of all groups

#### How can I navigate between recently used editors without a picker

#### Was this documentation helpful?

##### In this article there are 17 sectionsIn this article

## Refactoring

### Code Actions = Quick Fixes and refactorings

#### Code Actions on save

### Refactoring actions

#### Extract Method

#### Extract Variable

#### Rename symbol

### Refactor Preview

### Keybindings for Code Actions

### Extensions with refactorings

### Next steps

### Common questions

#### Why don't I see any light bulbs when there are errors in my code?

#### Was this documentation helpful?

##### In this article there are 7 sectionsIn this article

## Debugging

### User interface

#### Run and Debug view

#### Debug actions

### Debugger extensions

### Start debugging

#### Run mode

### Launch configurations

#### Generate a launch configuration with AI

#### Launch versus attach configurations

#### Add a new configuration

### Breakpoints

### Logpoints

### Data inspection

### Launch.json attributes

### Variable substitution

### Platform-specific properties

### Global launch configuration

### Advanced breakpoint topics

#### Conditional breakpoints

#### Triggered breakpoints

#### Inline breakpoints

#### Function breakpoints

#### Data breakpoints

### Debug console REPL

### Redirect input/output to/from the debug target

### Multi-target debugging

#### Compound launch configurations

### Remote debugging

### Automatically open a URI when debugging a server program

#### Trigger debugging via Edge or Chrome

#### Triggering an arbitrary launch config

### Next steps

### Common questions

#### What are the supported debugging scenarios?

#### I do not see any launch configurations in the Run and Debug view dropdown. What is wrong?

#### Was this documentation helpful?

##### In this article there are 19 sectionsIn this article

## Testing

### About testing in VS Code

### Get started with testing in VS Code

### Extensions for testing

### Automatic test discovery in Testing view

### Write tests with AI

### Run and debug tests

### Test coverage

### Task integration

### Test configuration settings

### Next steps

#### Was this documentation helpful?

##### In this article there are 10 sectionsIn this article

## VS Code for the Web

## Integrate with External Tools via Tasks

### TypeScript Hello World

### Task auto-detection

### Custom tasks

#### Compound tasks

#### User level tasks

### Output behavior

### Run behavior

### Customizing auto-detected tasks

### Processing task output with problem matchers

### Binding keyboard shortcuts to tasks

### Variable substitution

### Operating system specific properties

### Global tasks

#### Character escaping in PowerShell

### Changing the encoding for a task output

### Examples of tasks in action

#### Transpiling TypeScript to JavaScript

#### Transpiling Less and SCSS into CSS

### Defining a problem matcher

### Defining a multiline problem matcher

### Modifying an existing problem matcher

### Background / watching tasks

### Next steps

### Common questions

#### Can a task use a different shell than the one specified for the Integrated Terminal?

#### Can a background task be used as a prelaunchTask in launch.json?

#### Why do I get "command not found" when running a task?

#### Was this documentation helpful?

##### In this article there are 19 sectionsIn this article

## Profiles in Visual Studio Code

### Access the Profiles editor

### Create a Profile

#### Check the current profile

#### Configure a profile

#### Folder & workspace associations

### Manage profiles

#### Switch profiles

#### Edit a profile

#### Delete a profile

#### Open a new window with a profile

#### Apply a setting to all profiles

#### Apply an extension to all profiles

### Synchronize profiles across machines

### Share Profiles

#### Export

##### Save as a GitHub gist

##### Save as a local file

#### Import

### Uses for profiles

#### Demos

#### Education

#### Report VS Code issues

### Profile Templates

#### Python Profile Template

#### Data Science Profile Template

#### Doc Writer Profile Template

#### Node.js Profile Template

#### Angular Profile Template

#### Java General Profile Template

#### Java Spring Profile Template

### Command line

### Common Questions

#### Where are profiles kept?

#### What is a Temporary Profile?

#### How can I remove the profile from my project?

#### Why are some settings not exported when exporting a profile?

#### Why are templates not available when creating a new profile?

#### Was this documentation helpful?

##### In this article there are 9 sectionsIn this article

## Settings Sync

### Turning on Settings Sync

### Merge or Replace

### Configuring synced data

### Conflicts

### Switching Accounts

### Syncing Stable versus Insiders

### Restoring data

### Synced Machines

### Extension authors

#### Sync user global state between machines

### Reporting issues

### How do I delete my data?

### Next steps

### Common questions

#### Is VS Code Settings Sync the same as the Settings Sync extension?

#### What types of accounts can I use for Settings Sync sign in?

#### Can I use a different backend or service for Settings Sync?

### Troubleshooting keychain issues

#### Windows & macOS

#### Linux

##### GNOME or UNITY (or similar)

##### KDE

##### Other Linux desktop environments

##### (recommended) Configure the keyring to use with VS Code

##### (not recommended) Configure basic text encryption

### Can I share settings between VS Code Stable and Insiders?

#### Was this documentation helpful?

##### In this article there are 15 sectionsIn this article

## Snippets in Visual Studio Code

### Built-in snippets

### Install snippets from the Marketplace

### Create your own snippets

#### File template snippets

### Snippet scope

#### Language snippet scope

#### Project snippet scope

### Snippet syntax

#### Tabstops

#### Placeholders

#### Choice

#### Variables

#### Variable transforms

#### Placeholder-Transform

#### Transform examples

#### Grammar

### Using TextMate snippets

### Assign keybindings to snippets

### Next steps

### Common questions

#### What if I want to use existing TextMate snippets from a .tmSnippet file?

#### How do I have a snippet place a variable in the pasted script?

#### Can I remove snippets from IntelliSense?

#### Was this documentation helpful?

##### In this article there are 9 sectionsIn this article

## Emmet in Visual Studio Code

### How to expand Emmet abbreviations and snippets

#### Using Tab for Emmet expansions

#### Emmet when quickSuggestions are disabled

#### Disable Emmet in suggestions

#### Emmet suggestion ordering

### Emmet abbreviations in other file types

### Emmet with multi-cursors

### Using filters

#### BEM filter (bem)

#### Comment filter (c)

#### Trim filter (t)

### Using custom Emmet snippets

#### HTML Emmet snippets

#### CSS Emmet snippets

#### Tab stops and cursors in custom snippets

### Emmet configuration

### Next steps

### Troubleshooting

#### Custom tags do not get expanded in the suggestion list

#### My HTML snippets ending with + do not work

#### Abbreviations are failing to expand

#### Where can I set all the preferences as documented in Emmet preferences?

#### Any tips and tricks?

#### Was this documentation helpful?

##### In this article there are 8 sectionsIn this article

## Command Line Interface (CLI)

### Command line help

### Launching from command line

### Core CLI options

### Opening Files and Folders

### Select a profile

### Working with extensions

### Advanced CLI options

#### Create remote tunnel

### Opening VS Code with URLs

### Next steps

### Common questions

#### 'code' is not recognized as an internal or external command

#### How do I get access to a command line (terminal) from within VS Code?

#### Can I specify the settings location for VS Code in order to have a portable version?

#### How do I detect when a shell was launched by VS Code?

#### Was this documentation helpful?

##### In this article there are 10 sectionsIn this article

## What is a VS Code "workspace"?

### How do I open a VS Code "workspace"?

### Single-folder workspaces

### Multi-root workspaces

#### Untitled multi-root workspaces

### Workspace settings

#### Single-folder workspace settings

#### Multi-root workspace settings

### Workspace tasks and launch configurations

### Common questions

#### What is the benefit of multi-root workspace over a folder?

#### Why is VS Code restoring all untitled workspaces on a restart?

#### How do I delete an untitled workspace?

#### Can I use a multi-root workspace without folders?

#### Does VS Code support projects or solutions?

#### Was this documentation helpful?

##### In this article there are 6 sectionsIn this article

## Workspace Trust

### Safe code browsing

### Restricted Mode

#### Tasks

#### Debugging

#### Workspace settings

#### Extensions

### Trusting a workspace

### Selecting folders

#### Selecting a parent folder

#### Folder configurations

### Enabling extensions

### Opening untrusted files

#### Opening untrusted folders

#### Empty windows (no open folder)

### Settings

### Command-line switch

### Next steps

### Common questions

#### Can I still edit my source code in Restricted Mode?

#### Where did my installed extensions go?

#### Can I disable the Workspace Trust feature?

#### How do I untrust a folder/workspace?

#### Why don't I see the "Don't Trust" button?

#### What does Workspace Trust protect against?

#### Was this documentation helpful?

##### In this article there are 10 sectionsIn this article

## Multi-root Workspaces

### Adding folders

#### Add Folder to Workspace

#### Drag and drop

#### Multiple selection native file open dialogs

#### command line --add

#### Removing folders

### Workspace file

#### Save Workspace As...

#### Opening workspace files

#### Workspace file schema

### General UI

#### Editor

#### Search

### Settings

#### Unsupported folder settings

### Debugging

#### Workspace launch configurations

### Tasks

#### Workspace task configuration

### Source Control

### Extensions

#### Extension recommendations

### Next steps

### Common questions

#### How can I go back to working with a single project folder?

#### As an extension author what do I need to do?

#### Was this documentation helpful?

##### In this article there are 10 sectionsIn this article

## Accessibility

### Zoom

#### Persisted zoom level

### Accessibility help

### High Contrast theme

### Color vision accessibility

#### Recommended themes for color vision accessibility

### Customizing warning colors

#### Selecting accessible colors

### Dim unfocused editors and terminals

### Keyboard navigation

#### Anchor selection

### Tab navigation

### Tab trapping

### Screen readers

### Screen reader mode

### Resize table columns via the keyboard

### Accessible View

### Input control and result navigation

### Terminal accessibility

#### Shell integration

#### Minimum contrast ratio

### Status bar accessibility

#### Diff editor accessibility

### Debugger accessibility

### Accessibility Signals

### Hover accessibility

### Current known issues

#### macOS

#### Linux

### Next steps

#### Was this documentation helpful?

##### In this article there are 21 sectionsIn this article

## Voice Support

### Editor dictation

### Voice in Copilot Chat

### Walky talky mode

### "Hey Code"

### Support for multiple languages

### Next steps

#### Was this documentation helpful?

##### In this article there are 6 sectionsIn this article

## Custom Layout

### Workbench

#### Primary side bar

#### Secondary side bar

#### Activity Bar position

#### Panel

#### Panel position

#### Panel alignment

#### Maximize Panel size

#### Customize Layout control

#### Drag and drop views and panels

### Tool bars

#### Hide items in tool bars

### Editor

#### Minimap and breadcrumbs

#### Editor groups

#### Split in group

#### Grid layout

#### Floating editor windows

#### Pinned tabs

#### Locked editor groups

### Next steps

#### Was this documentation helpful?

##### In this article there are 4 sectionsIn this article

## Local Port Forwarding

### How to use local port forwarding

### Common questions

#### How do I forward local services if I'm connected to a remote machine?

#### How are forwarded ports secured?

#### What limits are there on port forwarding?

#### Can I configure policies across my organization?

#### Was this documentation helpful?

##### In this article there are 2 sectionsIn this article

# SOURCE CONTROL

## Using Git source control in VS Code

### Working in a Git repository

### Cloning a repository

### Initialize a repository

### Commit

#### Generate a commit message with AI

#### Author commit messages using an editor

### Review uncommitted code changes with AI

### Branches and Tags

### Remotes

### Source Control Graph

### Git Status Bar actions

### Gutter indicators

### Merge conflicts

### 3-way merge editor

#### Resolving conflicts

#### Completing the merge

#### Alternative layouts and more

#### Understanding conflicts

### Viewing diffs

#### Accessible Diff Viewer

### Timeline view

### Git output window

### VS Code as Git editor

#### VS Code as Git difftool and mergetool

### Working with GitHub Pull Requests and Issues

### SCM Providers

#### SCM Provider extensions

### Next steps

#### Was this documentation helpful?

##### In this article there are 19 sectionsIn this article

## Introduction to Git in VS Code

### Set up Git in VS Code

### Open a Git repository

#### Clone a repository locally

#### Initialize a repository in a local folder

##### Publish local repository to GitHub

#### Open a GitHub repository in a codespace

#### Open a GitHub repository remotely

### Staging and committing code changes

### Pushing and pulling remote changes

### Using branches

#### Creating and reviewing GitHub pull requests

### Using Git in the built-in terminal

#### Git Bash on Windows

#### Was this documentation helpful?

##### In this article there are 6 sectionsIn this article

## Working with GitHub in VS Code

### Getting started with GitHub Pull Requests and Issues

### Setting up a repository

#### Cloning a repository

#### Authenticating with an existing repository

### Editor integration

#### Hovers

#### Suggestions

### Pull requests

#### Creating pull requests

#### Reviewing

### Issues

#### Creating issues

#### Working on issues

### GitHub Repositories extension

#### Opening a repository

#### Switching branches

#### Remote Explorer

#### Create Pull Requests

#### Virtual file system

#### Continue Working On...

### Next steps

#### Was this documentation helpful?

##### In this article there are 7 sectionsIn this article

# PYTHON

## Running Python code in Visual Studio Code

### Interactively running Python code

#### Native REPL

#### Terminal REPL

### Run Python code

#### Smart Send

### See also

#### Was this documentation helpful?

##### In this article there are 3 sectionsIn this article

## Editing Python in Visual Studio Code

### Autocomplete and IntelliSense

#### Customize IntelliSense behavior

#### Enable Auto Imports

#### Enable IntelliSense for custom package locations

### Enhance completions with AI

### Navigation

### Quick Fixes

#### Add import

#### Search for additional import matches

#### Change spelling

### Refactorings

#### Extract Variable

#### Extract Method

#### Rename Module

#### Move Symbol

#### Implement All Inherited Abstract Classes

#### Sort Imports

### Troubleshooting

#### Pylance Diagnostics

##### importResolveSourceFailure

##### importResolveFailure

##### importCycleDetected

### Next steps

#### Was this documentation helpful?

##### In this article there are 7 sectionsIn this article

## Linting Python in Visual Studio Code

### Choose a linter

### General Settings

### Disable linting

### Run linting

### Code Actions

### Logging

### Severity

### Troubleshooting linting

### Next steps

#### Was this documentation helpful?

##### In this article there are 9 sectionsIn this article

## Formatting Python in VS Code

### Choose a formatter

### Set a default formatter

### Format your code

### General formatting settings

### Troubleshoot formatting

### Next steps

#### Was this documentation helpful?

##### In this article there are 6 sectionsIn this article

## Python debugging in VS Code

### Python Debugger Extension

### Initialize configurations

### Additional configurations

### Basic debugging

### Command line debugging

#### Install debugpy

#### Command line syntax

#### Example

#### Command line options

### Debugging by attaching over a network connection

#### Local script debugging

#### Remote script debugging with SSH

### Set configuration options

#### name

#### type

#### request

#### program

#### module

#### python

#### pythonArgs

#### args

#### stopOnEntry

#### console

#### purpose

#### autoReload

#### subProcess

#### cwd

#### redirectOutput

#### justMyCode

#### django

#### sudo

#### pyramid

#### env

#### envFile

#### gevent

#### jinja

### Breakpoints and logpoints

#### Conditional breakpoints

#### Invoking a breakpoint in code

#### Breakpoint validation

### Debugging specific app types

#### Flask debugging

### Troubleshooting

### Next steps

#### Was this documentation helpful?

##### In this article there are 11 sectionsIn this article

## Python environments in VS Code

### Types of Python environments

#### Global environments

#### Local environments

##### Virtual environments

##### Conda environments

#### Python environment tools

### Creating environments

#### Using the Create Environment command

#### Create a virtual environment in the terminal

#### Create a conda environment in the terminal

### Working with Python interpreters

#### Select and activate an environment

#### Manually specify an interpreter

#### How the extension chooses an environment automatically

#### Where the extension looks for environments

#### Environments and Terminal windows

#### Choose a debugging environment

### Environment variables

#### Environment variable definitions file

#### Use of the PYTHONPATH variable

### Next steps

### More Python resources

#### Was this documentation helpful?

##### In this article there are 6 sectionsIn this article

## Python testing in Visual Studio Code

### A little background on unit testing

### Example test walkthroughs

### Configure tests

### Create tests

#### Tests in unittest

#### Tests in pytest

### Test discovery

### Run tests

### Run tests in parallel

### Run tests with coverage

### Debug tests

### Test commands

### Django unit tests

#### Troubleshooting

### IntelliSense for pytest

### Test configuration settings

#### General UI settings

#### General Python settings

#### unittest configuration settings

#### pytest configuration settings

#### IntelliSense settings

### See also

#### Was this documentation helpful?

##### In this article there are 14 sectionsIn this article

## Python Interactive window

### Jupyter code cells

#### Additional commands and keyboard shortcuts

### Using the Python Interactive window

#### IntelliSense

#### Plot Viewer

### Variables Explorer and Data Viewer

### Connect to a remote Jupyter server

### Convert Jupyter notebooks to Python code file

### Debug a Jupyter notebook

### Export a Jupyter notebook

#### Was this documentation helpful?

##### In this article there are 7 sectionsIn this article

# DATA SCIENCE

## Jupyter Notebooks in VS Code

### Setting up your environment

### Workspace Trust

### Create or open a Jupyter Notebook

### Running cells

#### Run a single code cell

#### Run multiple code cells

#### Run cells in section

### Save your Jupyter Notebook

### Export your Jupyter Notebook

### Work with code cells in the Notebook Editor

#### Create a code cell

#### Code cell modes

#### Add additional code cells

#### Select a code cell

#### Select multiple code cells

#### Move a code cell

#### Delete a code cell

#### Undo your last change

#### Switch between code and Markdown

#### Clear output or restart/interrupt the kernel

#### Enable/disable line numbers

### Table of Contents

### IntelliSense support in the Jupyter Notebook Editor

### Variable Explorer and Data Viewer

#### Data Viewer

#### Filtering rows

### Saving plots

### Custom notebook diffing

### Debug a Jupyter Notebook

#### Run by Line

#### Debug Cell

#### Search through notebook

### Connect to a remote Jupyter server

### Data Science profile template

#### Was this documentation helpful?

##### In this article there are 15 sectionsIn this article

## Quick Start Guide for Data Wrangler in VS Code

### Set up your environment

### Open Data Wrangler

#### Launch Data Wrangler from a Jupyter Notebook

#### Launch Data Wrangler directly from a file

### UI tour

#### Viewing mode interface

#### Editing mode interface

### Example: Replace missing values in your dataset

### Next steps

#### Was this documentation helpful?

##### In this article there are 5 sectionsIn this article

## Getting Started with Data Wrangler in VS Code

### Set up your environment

### Open Data Wrangler

#### Launch Data Wrangler from a Jupyter Notebook

#### Launch Data Wrangler directly from a file

### UI tour

#### Viewing mode interface

#### Editing mode interface

### Data Wrangler operations

### Modify previous steps

### Edit and export code

### Search for columns

### Troubleshooting

#### General kernel connectivity issues

#### Opening a data file gives UnicodeDecodeError

### Questions and feedback

### Data and telemetry

#### Was this documentation helpful?

##### In this article there are 10 sectionsIn this article

## PyTorch support in Visual Studio Code

### Data Viewer support for Tensors and data slices

### TensorBoard integration

### PyTorch Profiler integration

### IntelliSense through the Pylance language server

#### Was this documentation helpful?

##### In this article there are 4 sectionsIn this article

## Manage Jupyter Kernels in VS Code

### Jupyter Kernels

### Python Environments

### Existing Jupyter Server

### Codespaces Jupyter Server

### Adding Kernel Options

### Questions or feedback

#### Was this documentation helpful?

##### In this article there are 6 sectionsIn this article
