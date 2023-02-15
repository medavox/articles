# (Debian?) Linux One-Liners 


These are various bash commands and tricks I've accumulated, which help in the day-to-day usage of my linux laptop.


## Sort files and folders in the current directory by size, human readably

    du -ahd 1 | sort h 



This will print out the largest file and folders in the current directory, 
with the largest at the bottom (closest to the prompt)

NOTE: If this doesn't work, then it's because the `-d` option was only introduced to `du` after debian 6.
Try `--max-depth=1` instead.


## Search APT Currently Installed packages

    dpkg --get-selections | grep -i <searchterm>



This will search (case-insensitive) your locally installed apt packages for any containing the string <searchterm>.


## Get more info on a package

    apt-cache show <exact package name>


Gives you a bunch more info than just the name (hopefully including a short description) of the named package.

## Search all available packages

    apt-cache search <searchterm>

Beware, this can give a lot of results.

## Play videos fullscreen on commandline using mplayer

    screenwidth=<your screen width>; mplayer -nosound -vo fbdev -xy $screenwidth -zoom <video file>

Doesn't bother with sound,
because I haven't worked out how to just run a sound server without an X server yet,
and there's no need to waste system resources playing something you can't hear.

## Losslessly Extract Audio from an MP4 using FFMPEG

    ffmpeg -i <infile> -vn -acodec copy <outfile>.mp4

Extracts the audio from an MP4 videon without transcoding of any kind.
Avoids any loss of audio quality.

This command will probably need to be revisited and changed,
following ffmpeg's upheaval, name change, etc.
But for now it still works, even with deprecated warnings.

UPDATE:

here's the new version of the command, for us with libAV (the fork of ffmpeg adopted by all distros I use):

    avconv -i <infile> -vn -acodec copy <outfile>.mp4


Yes, it's exactly the same. Panic over.


## Recursively find-replace a regex pattern with a new one, in files matching a criteria

    find ./ -iname <filname-pattern> -exec sed -i 's/oldtext/newtext/' {} \;


## Recursively search in text files for a pattern

    grep -Irn <text>


Surround the searched-for text with quotes if it contains a space.

## Recursively count all occurrences of a given string in all text files in the provided dir

    grep -Iric <text> | grep -v :O |  sort -n -t : -k 2
    
#recursively search for files containing both StringA and StringB (StringA and StringB don’t have to be on the same line)
    
    grep -Irl StringA | xargs grep StringB


    
%tags:linux, apt, debian, ubuntu, bash, commandline, server
