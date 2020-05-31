#!/usr/bin/env python
# coding: utf-8

# In[4]:


import os ,sys
import time

print('PLEASE CONNECT INTERNET VIA ETHERNET')
input('Press Enter When Conected ')

os.system('timedatectl set-ntp true')

print('Please format your disk with gparted and use only sdX1 others are unsupported. EFI ONLY. quit if not already done and run again')
SD = input('Disk to install a, b, c, etc. IN SMALL sd and 1 already set. ')
USR = input('username?').lower()


os.system('mkfs.ext4 /dev/sd'+SD+'1')
os.system('mount /dev/sd'+SD+'1'+' /mnt')
os.system('pacstrap /mnt base linux linux-firmware')
os.system('genfstab -U /mnt >> /mnt/etc/fstab')

print('PLEASE WAIT')
time.sleep(7)

os.system('arch-chroot /mnt ln -sf /usr/share/zoneinfo/Asia/Kolkata')
os.system('arch-chroot /mnt hwclock --systohc')
os.system('arch-chroot /mnt locate-gen')
os.system('arch-chroot /mnt pacman -S --noconfirm nano')
os.system('arch-chroot /mnt mkinitcpio -P')
os.system('arch-chroot /mnt pacman -S --noconfirm grub')

os.system('arch-chroot /mnt grub-install --target=i386-pc /dev/sd'+SD)
os.system('arch-chroot /mnt grub-mkconfig -o /boot/grub/grub.cfg')
os.system('arch-chroot /mnt useradd -m '+USR)
os.system('arch-chroot /mnt pacman -S --noconfirm gnome')

os.system('arch-chroot /mnt systemctl enable gdm.service')
os.system('arch-chroot /mnt pacman -S --noconfirm gnome-software-packagekit-plugin')

os.system('arch-chroot /mnt pacman -S --noconfirm libreoffice-fresh')
os.system('arch-chroot /mnt pacman -S --noconfirm pulseaudio')

os.system('arch-chroot /mnt pacman -S --noconfirm  gnome-tweaks')

os.system('arch-chroot /mnt systemctl enable NerworkManager.service')
os.system("arch-chroot /mnt gsettings set org.gnome.desktop.wm.preferences button-layout ':minimize,maximize,close'")
os.system('arch-chroot /mnt pacman -S --noconfirm jre-openjdk')
os.system('arch-chroot /mnt pacman -S --noconfirm jdk-openjdk')

os.system('arch-chroot /mnt pacman -S --noconfirm termite')

os.system('arch-chroot /mnt pacman -S --noconfirm gnome-software-packagekit-plugin')
os.system('arch-chroot /mnt git clone https://aur.archlinux.org/snapd.git')
os.s)ystem('arch-chroot /mnt cd snapd')
os.system('arch-chroot /mnt makepkg -si')

os.system('arch-chroot /mnt systemctl enable --now snapd.socket')

os.system('arch-chroot /mnt snap install snap-store')
print('''By Sahibjot Singh Sidhu.
official channel: BlackSAJRAS.
THANKS FOR USING

I WANTED TO CUSTOMIZE MORE BUT WAS UNABLE SORRY.
CUSTOMIZATION IS SUPPORTED.


THINGS TO DO AFTER RUNNING INSTALLER:
IN CHROOT (ALL IMPORTANT)
1) EDIT /etc/locale (Language setup)USE ARCH WIKI.
2) EDIT /etc/hostname (For computer name)USE ARCH WIKI.
3) EDIT /etc/hosts (For network) USE ARCH WIKI.
4) Execute passwd and put user specified next to this. (For PASSWORD password is important) USE ARCH WIKI
.''')
input('DONE? ')


# In[ ]:




