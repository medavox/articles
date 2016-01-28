## Making Your Raspberry Pi Run Faster=

### (According To Me)

These are any tips I remember to write down, in order to get the most performance out of your pi.

## X Server (Desktop) Mode

  * Edit `/etc/xdg/lxsession/LXDE/autostart`
      Comment out the line (I used a #) which says `pcmanfm --profile LXDE`, to remove the desktop icons and background, which waste resources.
 
        * The line starting with `lxpanel` is the 'start menu' equivalent. I leave this running, because the default Openbox menu (right-click the desktop) is somewhat lacking if used as a full desktop, although you can disable that the same way.
## Commandline (SSH or direct tty bash) Mode

These two don't actually speed your pi up, but they are invaluable tools in order to work out what _is_ slowing you down:-

  * install `htop`: it's a syntax-highlighted extension of `top`, which supports scrolling, sorting by clicking, and lots of other cool, sanely-designed features. As opposed to memorising key presses to perform something simple like sorting by memory usage, with `top`.

      * Also get `gpm`: general purpose mouse server for terminal. This gives you mouse usage even without X running, allowing you to use unix-style copy/paste (highlight to copy, middle-click to paste), click columns to sort by them in `htop`. You can even have a semi-decent browsing experience, if you also:

  * Install a text-mode browser, such as `elinks`. I have also heard good things about `w3m` and `netsurf`, but neither seem as easy to use straight-off as elinks. Tip: if your mousewheel doesn't scroll, then use the insert and delete keys instead. Having a text-mode browser is handy if you have to configure a router which only accepts admin logins locally, and you're somewhere else, SSH'd into the pi.

  * Set up a static IP (more on this later), then uninstall the dhcp client (it goes by many names in the repositories -- search for dhcp), `iplugd` (handles plugging and unplugging of your ethernet cable) and network-manager(high level abstraction shit you don't need) Because _something_ needs to bring up your ethernet 'interface' (port), add this line: `ifup eth0` (where eth0 is the linux name of your eth plug, checkable with ifconfig) to `/etc/rc.local` to run it on boot.

  * install `sysv-rc-conf`: its ncurses interface is a bit claggy (how do you increase the daemon name column's width?) but this program allows you to edit which daemons (services) start in which run levels. Handy for a quick removal of a daemon you want to keep, but not at startup, such as gpm (which you won't want running ALL the time, only when you're logged in).


%tags:linux tips raspi raspberrypi raspberry pi apt debian ubuntu server
