# Distribox

## AKA Git-Torrent


Here's an idea I had.

## Problem Outline


Dropbox is an incredibly useful piece of software for keeping files synced across multiple machines; but by using their service, Dropbox can stake a claim to your data. 

  * You have no idea what they're doing with it
  * You can't be sure they've really deleted something (hint: they haven't)
  * If you made a commercially interesting piece of software (something that could make money), what would happen to your rights to the IP?
  * The maximum file and storage sizes are (understandably, considering they personally store copies of everything you sync) very low, and this restricts its usefulness.

If you think about a normal use case (updating a few files at a time between devices, or friends), you don't REALLY need a centralised server to keep copies of everything. It's expensive to have that storage space, keeping it running and connected to the internet all the time.

Plus, as I said with Dropbox specifically, it encumbers your files with possible ownership and legal controversy. Best to avoid that can of worms.

Distribox shall be a decentralised method for syncing files between computers, but without anyone but you having copies.

The only people who have your files are people on your peer-access list


It shall use existing technology to provide this:-
  *[Bit-torrent](http://www.bittorrent.org/beps/bep_0003.html): good at reducing bandwidth costs of a one-to-many download, by trading pieces of files among peers. Means the original syncing file only needs to be uploaded once by the originator, (like Dropbox, to its central servers).
  *[rsync](http://rsync.samba.org/): robust file-transfer application, which uses differential transfer: only transfers new files, (or even parts of files, I think?) that have changed. Would save a lot of bandwidth.
  *[Git](http://git-scm.com/): an existing solution for peers to exchange versions of files; I don't THINK I want version history in this program, but it could be added as an optional feature later.
  *[PGP](http://www.cryptography.org/getpgp.htm): inevitably, some kind of encryption will be needed to prevent unauthorised peers from getting copies of your files. An authentication system would be good, possibly along with encrypted packet transmission, and/or encrypted storage. [Pretty Good Privacy](http://www.cryptography.org/getpgp.htm) is a good candidate for any of these. Depending on how paranoid the user is, or I am.

There is some functionality overlap with Git itself, but here are reason why I believe this software needs writing:
  * Git is not visible to end-users: its intended audience are developers, and its steep learning curve (tens of commands to learn each with its own single-character options; a new mental model for manipulating 'staged' files which are 'indexed') would prevent its adoption by non-programmer power users
  * Existing GUIs for git are unfinished, non-free, buggy o r as confusing as the commandline interface, with none of the portability.
  * Git is much more complex than is necessary for this task

## External Interface


Users will choose:-
  * a folder they wish to keep synced,
  * and ONE UNIFIED list of peers that sync to this folder.
  * a maximum size limit of data to sync (optionally no limit)


Theoretically users could choose different peer lists for different folders, but this could get complex for the user (and possibly for implementation) very quickly, so I will probably only let users sync 1 folder to 1 list of peers for now.

This will work best for one person editing at a time (avoiding merge conflicts), but can be adapted (again with existing technology) to work with more.

## Platform Support


I intend to write this for Windows, Linux and Android, which will affect library choices slightly. I won't implement this for an Apple product and, despite this being open-source, I'll take measures to make sure no-one else does. For an idea why, read [this article](http://www.cracked.com/article_18377_5-reasons-you-should-be-scared-apple.html). Or [this one](http://en.wikipedia.org/wiki/Criticism_of_Apple_Inc.). Or [this one](http://www.pcworld.com/article/181200/apple_marketing_locks_you_in.html).

The backend can probably be written once (pending disk and network IO libraries); just the external UI will need separate versions for each platform.

## The Act of syncing a file


At the start, peers will have to get all the files from a filled folder,

later, peers will have to receive updates

A peer with new files will announce updates to all peers (push?)

peers can download a difference patch, or the whole file if it's new

## Links

https://tahoe-lafs.org/trac/tahoe-lafs

http://code.google.com/p/mogilefs/

http://ceph.com/

http://sparkleshare.org/

https://git-annex.branchable.com/