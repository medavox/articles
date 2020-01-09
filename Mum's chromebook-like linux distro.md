Mum's chromebook-like linux distro
================================


as minimal a Desktop GUI linux installation as possible
based on debian-stable, or a Linux Mint or Ubuntu version built on that,
if one exists
designed to NEVER NEED MANUAL UPDATING AFTER INITIAL INSTALL
we'll run on debian-stable, and either it will never be updated,
 or updated automatically. 
More likely that normal software will never be updated\*,
as any update may break something

\* low-level security updates may still auto-update, eg the kernel
eg updates unlikely to affect the GUI,
or the wifi


GUI
---

DE is openbox
File Manager is whichever I think is most user-friendly provided by debian
probably candidate:
XFCE stuff
LXDE
KDE
GNOME
DeepIn
Enlightenment?

Remember, the widget toolkit provides the File Chooser!

So in Firefox this is GTK.

We need to use the de-fucked GTK3, GTK3-mushrooms or GTK3-classic 
(these are only availabe on arch and manjaro, 
so find a debian equivalent, or find a way to package these for debian)

### Desktop

the Desktop will solely consist of icons for runnable apps, 
and a folder called "My Files"

Desktop contents cannot be customised by a normal user

Normal Windows-style taskbar
No Start Menu


Goals
----

The goal is to reduce as much as possible the amount of things that can go wrong.
ie:
* Minimise the ability of non-technical users to accidentally break things 
(eg, move the taskbar)
* keep security as up-to-date as possible

It shall be low-to-no maintenance after installation,
and yet remain secure-by-default against external security threats.

There is no complete guard against external stupidity,
but removing the permissions of swindlable users to carry out the instructions of a malicious third-party,
will reduce the third-party's ability to take over.

This does not mitigate phishing-based security threats.
Internet accounts security is its own can of worms

It will be built with the assumption that 
**everyday users don't know what they're doing**,
and a privileged account is required to do almost anything outside running existing software
(this includes modifying the contents of the hard drive outside the Downloads folder)

Minimal Feature Set
------------------

absolutely minimal set of features provided locally.


* no settings to modify (for normal users)
* maybe no local files storage?
* volume, 
* brightness, 
* shutdown, 
* battery indicator
* WiFi login dialog
* DHCP client
* no monitor management 


Mum's account will have access to very little -- no privileges for:
	installing new software via package manager

firefox browser, which is complex enough that it has its own list of customisations:
	* updates itself regularly
	* installing browser extensions is blocked

new software is only provided, reluctantly, through AppImages
these are self-contained archives of software bundled with all their dependencies
hopefully we can cause any and all of these to auto-update

The majority of functionality can be provided via online services,
a la Chromebooks

Google Docs is a fine replacement for whatever Office looks like these days
Maybe include LibreOffice Writer as a backup,
and maybe AbiWord

Printer Installation
--------------------

use linux printer drivers, 
ignore the packaged CD

