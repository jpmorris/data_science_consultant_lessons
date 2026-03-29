## Review

<div style="background-color: rgb(87, 61, 61);">
<font color="red">**To Remember Forever**</font>

### Important Tasks to Remember

- Symbolic Links: `ln -s`
- How to change file permissions: `chmod 600`, `chown`
  - Very important for `~/.ssh/*.pem`
- How to elevate privileges: `sudo`
- How to install packages on a machine: `yum`, `dnf`, `apt`, et al.
- How to get system logs: `systemctl`, `journalctl`
- How to modify your startup environment: `~/.bashrc` (and probably `export` for
environment variables)
</div>

### Where we were at with Linux From Scratch - Chapters 1-4

#### 1. Create cross-toolchain compiler

We bootstrap an existing system to create the compiled code to run on the new
system

- You cant simply compile everything on your host system because:
- Your system might produce binaries tied to the host system
- You need clean, predictable build environment
- cross-compilation prevents circular dependencies

#### 2. Prepare Host System

Setup host system with necessary tools (`gcc`, development tools)

#### 3. Compile Essential Software Stack

LFS requires ~70-80 packages to create a minimal but functional Linux system
including:

- Kernel: Linux kernel itself
- C Library: Glibc (provides system calls interface)
- Toolchain: GCC (compiler), Binutils (linker, assembler), Make
- Shell: Bash
- Core Utilities: Coreutils (ls, cp, mv, etc.), Findutils, Grep, Sed, Gawk
- System Utilities: Util-linux, Procps, Psmisc
- Boot Tools: GRUB bootloader, SysVinit
- Compression: Gzip, Bzip2, Xz
- Text Processing: Perl, Python (needed for build systems)
- Documentation: Man-pages, Texinfo

#### 4. Final pre-compile preparations

- Create lfs user and build with this user (which has the clean environment)
- Path and directory setup
- **Cross-Compilation**
- Problem: you need a compiler to build a compiler
- Solution: use host compiler to build a cross-compiler, use cross-compiler to
  build minimal system then `chroot` into that system and rebuild remaining
  cleanly

#### 5. Compile **cross-toolchain** - tools that run on host but produce executables for target system

- Build process uses: host `gcc`, binutils, make, bash, perl, python (to compile
  the cross-toolchain itself)
- Cross-toolchain configuration:
- `--with-sysroot=$LFS` - hardcoded into cross-compiler to look for
  libraries/headers in `$LFS`
- `--target=x86_64-lfs-linux-gnu` - target triplet tells cross-compiler what
  system to build for
- The `lfs` vendor field distinguishes from host system (`x86_64-pc-linux-gnu`)
- Once built, cross-toolchain completely ignores host libraries/headers, uses
  only LFS target resources
- Key packages: Binutils Pass 1, GCC Pass 1, Linux Headers, Glibc, Libstdc++

#### 6. Cross compile Temporary tools using the cross-toolchain (bash, gawk, file, ncurses, gzip, make, patch, sed, tar, xz, etc)

- These tools run on host but are linked to LFS libraries
- Prepares minimal tool set for next stage

#### 7. Enter `chroot` and build additional temporary tools (these are now tools compiled in the target system)

- We enter an isolated environment using `chroot` and start to build the system
  - create directories
  - create /dev device nodes with `mount -vt depts...`
  - create `/etc/mtab`
  - create `/etc/hosts`
  - create `/etc/passwd` and `/etc/group`

#### 8. Installing basic system software into target system

- After setting tools in `chroot` we install the basic system
- `passwd root` to set root password

#### 9. System Configuration

#### 10. Making the LFS System Bootable

### Commands to build Looker

## Building a Looker Box

### SSM vs SSH

## Logging and Event Management

## Shell and User Interface Layer

## Networking Stack

## Scheduled Tasks and Automation

## Boot loader (GRUB)

## Hardware and Device Management
