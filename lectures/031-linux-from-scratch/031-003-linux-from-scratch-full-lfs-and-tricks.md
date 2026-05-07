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
- Remember bash is a viable alternative to python in many shell- or string-
based workflows
</div>

### Other Learnings

- Repomix
- Choices for interface TUI vs static webpage, vs served webpage (vs. mobile
  app, desktop application ...)
- How Express works
- What's in a chrome plugin

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

- Transfer ownership of all `$LFS/*` directories from `lfs` user to `root`
  (`chown --from lfs -R root:root`)
- **Prepare Virtual Kernel File Systems** — mount them so the chroot environment
  can talk to the running kernel:
  - `mount --bind /dev $LFS/dev` — bind-mount host `/dev`
  - `mount -vt devpts devpts $LFS/dev/pts` — pseudo-terminals
  - `mount -vt proc proc $LFS/proc`
  - `mount -vt sysfs sysfs $LFS/sys`
  - `mount -vt tmpfs tmpfs $LFS/run`
- **Enter the chroot environment** as root with a clean PATH (cross-toolchain
  `/tools/bin` is intentionally excluded):
  ```
  chroot "$LFS" /usr/bin/env -i HOME=/root TERM="$TERM" \
      PATH=/usr/bin:/usr/sbin /bin/bash --login
  ```
- **Create the FHS directory tree** inside the new system (`/boot`, `/home`,
  `/etc/sysconfig`, `/usr/local`, `/var/log`, etc.)
- **Create essential files and symlinks**:
  - `/etc/mtab` → symlink to `/proc/self/mounts`
  - `/etc/hosts`, `/etc/passwd`, `/etc/group` (with standard system users: root,
    bin, daemon, tty, etc.)
  - Initialize log files: `/var/log/wtmp`, `lastlog`, `faillog`, `btmp`
- **Build 6 additional temporary packages** (still inside chroot, but now truly
  native):
  - Gettext (i18n utilities: `msgfmt`, `msgmerge`, `xgettext`)
  - Bison (parser generator)
  - Perl (needed by many build systems)
  - Python (needed by many build systems)
  - Texinfo (documentation tools)
  - Util-linux (miscellaneous system utilities)
- **Clean up and optionally back up** the temporary system:
  - Remove docs/man pages and `.la` libtool archive files
  - Remove `/tools` directory (1 GB, no longer needed)
  - Optional: `tar -cJpf $HOME/lfs-temp-tools-12.4.tar.xz .` — checkpoint
    snapshot before Chapter 8

#### 8. Installing basic system software into target system

This is the main build phase — ~85 packages installed natively into the final
LFS system. Still inside `chroot`.

- **Key categories of packages installed**:
  - C library & math: Glibc, Zlib, Libxcrypt, GMP, MPFR, MPC
  - Compression: Bzip2, Xz, Lz4, Zstd, Gzip
  - Toolchain (final): Binutils, GCC (full pass), Ncurses, Readline
  - Core utilities: Coreutils, Findutils, Diffutils, Gawk, Grep, Sed
  - System utilities: Util-linux, Procps-ng, Psmisc, Shadow (user management)
  - Build tools: Make, Patch, Autoconf, Automake, Libtool, Pkgconf, M4, Flex,
    Bison
  - Scripting: Perl, Python, Tcl/Expect (for test suites)
  - Networking: IPRoute2, OpenSSL
  - Boot: GRUB-2.12, Kmod, E2fsprogs, SysVinit
  - Editors/Docs: Vim, Man-pages, Texinfo, Groff, Less
  - Init system: **SysVinit** (LFS uses classic System V init, not systemd)
  - Device management: **Udev** (from Systemd source, udev component only)
  - Logging: Sysklogd
  - Python ecosystem: flit-core, wheel, setuptools, packaging, MarkupSafe,
    Jinja2
  - Build system helpers: Meson, Ninja
- **`passwd root`** — set the root password for the new system
- **Stripping** — remove debug symbols from binaries and libraries to reduce
  image size (~1 GB saved)
- **Cleaning up** — remove test artifacts, `.la` files, cross-toolchain remnants
  (`userdel -r tester`)

#### 9. System Configuration

Configure the system so it boots and operates correctly.

- **Boot process overview** — LFS uses **SysVinit** (classic System V init), not
  systemd
  - `init` reads `/etc/inittab`; run levels 0-6 (halt, single-user, multi-user,
    reboot)
  - Default run level is **3** (multi-user with networking)
  - Bootscripts live in `/etc/rc.d/init.d/`; symlinks in `/etc/rc.d/rc?.d/` use
    `K##`/`S##` naming to control start/stop order
- **LFS-Bootscripts** package — installs the set of start/stop scripts:
  - `udev`, `mountfs`, `network`, `sysklogd`, `setclock`, `console`, `localnet`,
    `checkfs`, `swap`, etc.
- **Device and module handling (udev)**:
  - Kernel creates device nodes dynamically in `devtmpfs` at `/dev`
  - `udevd` daemon applies rules from `/etc/udev/rules.d/`,
    `/usr/lib/udev/rules.d/`
  - Network interfaces get persistent names based on firmware/MAC (e.g.
    `enp2s0`); can revert to `eth0` style with `net.ifnames=0` kernel param
- **Network configuration**:
  - Static IP: create `/etc/sysconfig/ifconfig.eth0` with `ONBOOT`, `IFACE`,
    `IP`, `GATEWAY`, `PREFIX`
  - DNS: `/etc/resolv.conf` with `nameserver` entries
  - Hostname: `echo "lfs" > /etc/hostname`
  - FQDN: `/etc/hosts` with `127.0.1.1 <FQDN> <HOSTNAME>`
- **SysVinit configuration**: create `/etc/inittab` defining the default
  runlevel and respawning 6 `agetty` TTYs
- **System clock**: `/etc/sysconfig/clock` — set `UTC=1` if hardware clock is
  UTC
- **Console/locale**:
  - `/etc/sysconfig/console` — keyboard map (`KEYMAP`), screen font (`FONT`),
    Unicode mode
  - `/etc/profile` — set `LANG` environment variable (e.g. `en_US.UTF-8`)
  - `/etc/inputrc` — readline library configuration (key bindings for bash)
  - `/etc/shells` — list of valid login shells (`/bin/sh`, `/bin/bash`)

#### 10. Making the LFS System Bootable

The final steps to produce a system you can actually boot into.

- **`/etc/fstab`** — filesystem mount table:
  - Root partition (`/`), swap, `proc`, `sysfs`, `devpts`, `tmpfs` for `/run`,
    `devtmpfs` for `/dev`
  - Replace `<xxx>` and `<yyy>` with actual device names (e.g. `sda2`, `sda5`)
    and filesystem type (e.g. `ext4`)
- **Compile the Linux kernel** (Linux-6.16.1) — the most hardware-specific step:
  - `make mrproper` — clean source tree
  - `make menuconfig` — interactive ncurses config (nearly 12,000 options;
    `make defconfig` is a safe starting point)
  - Critical options to enable: `DEVTMPFS`, `DEVTMPFS_MOUNT`, `CGROUPS`,
    `STACKPROTECTOR_STRONG`, `KASLR`, `DRM`/framebuffer support
  - `make` then `make modules_install`
  - Copy kernel image: `cp arch/x86/boot/bzImage /boot/vmlinuz-6.16.1-lfs-12.4`
  - Copy `System.map` and `.config` to `/boot/`
- **GRUB bootloader** (GRUB-2.12):
  - `grub-install /dev/sda` — write GRUB to the MBR (caution: overwrites
    existing bootloader)
  - Create `/boot/grub/grub.cfg` manually with a `menuentry` pointing to the
    kernel and root partition
  - GRUB uses `(hd0,1)` notation (0-based drives, 1-based partitions)
  - Use `PARTUUID=` instead of `/dev/sdX` to avoid device renaming issues
  - For UEFI systems: skip `grub-install` and follow BLFS UEFI instructions
    instead

### Commands Used to Build Looker Box

- 158 echo
- 82 grep
- 52 head
- 50 tail
- 40 ls
- 24 systemctl
- 23 aws
- 19 mysql
- 17 cat
- 17 dig
- 15 curl
- 15 find
- 13 timeout
- 9 cloud-init
- 9 chown
- 8 keytool
- 6 sleep
- 6 ps
- 6 journalctl
- 5 nc
- 5 ss
- 5 openssl
- 5 python3
- 5 true
- 4 bash
- 3 exec
- 2 stat
- 2 du
- 2 rm
- 2 dirname
- 2 unzip
- 1 awk
- 1 wc
- 1 dnf
- 1 nginx
- 1 mkdir
- 1 sed
- 1 update-ca-trust
- 1 psql
- 1 readlink
- 1 which
- 1 chmod
- 1 import_rds_ca.sh
- 1 xargs
- 1 looker
- 1 tr
- 1 pip3
- 1 klist

- ssm (228)
  - send-command (149)
  - get-command-invocation (73)
  - describe-instance-information (3)
  - start-session (3)

- ec2 (39)
  - describe-instances (16)
  - describe-security-groups (11)
  - describe-vpc-endpoints (4)
  - authorize-security-group-egress (2)
  - delete-vpc-endpoints (2)
  - describe-security-group-rules (2)
  - describe-route-tables (1)
  - reboot-instances (1)

- s3
  - cp
  - ls
  - sync

#### SSM vs SSH
