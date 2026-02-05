This lecture is based on the Linux From Scratch Project. A host environment is setup to create the
Linux From Scratch system. A second drive is added to the VM, and mounted to `/mnt/lfs`. A build
user is created to perform the build process.

# ===== LFS TL;DR Resume After Reboot =====

# 1. Become root

sudo -i

# 2. Set LFS mount point

export LFS=/mnt/lfs

# 3. Mount LFS partition

mount /dev/vdb3 /mnt/lfs

# 4. Verify mount

mount | grep lfs ls /mnt/lfs

# 5. Switch to build user (only before chroot)

su - lfs export LFS=/mnt/lfs

# 6. Confirm environment

echo $PATH | grep tools

# 7. Continue book steps
