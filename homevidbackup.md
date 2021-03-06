# Family Home Video Backup Solution


This is my plan for backing up my family's existing home videos (and possibly pictures). There's nothing really specific to me in here, so the advice in this plan can probably be used by anyone to aid them in preserving their family's history.

# Problem Outline 


My family's videos are all still stored on VHS, and some converted slides (to VHS) that my dad did. Most long-term backup articles I've read advise that this is normal, that backups will probably need to converted to newer formats about once every generation.

So this is my effort.

Since my parents filmed all those holidays and things in the 1980s onwards, computers have happened. 

Everything is digital now.

That may sound like a horribly outdated phrase even now, in 2013, but it's not. There are only two types of data: analogue and digital. They could probably better be described as continuous and discrete, like in maths, because that's what they are. 

Briefly, Analogue data has an infinitely fine range of values, like every possible decimal number between 0 and 1.0. Its precision is limited by technical constraints such as EM interference. An example of an analogue medium would be VHS tape, or radio (but not DAB, which is digital data transmitted over an analogue medium). Digital data has a finite range of values, like the numbers from 1 to 10. Or, more relevantly, from 0 to 255. 

#### Digital > Analogue...? 


Digital data is a lot more exact than analogue, so you can be more definite about what constitutes a perfect-quality signal (or datum), and what is corrupt. This provides for much more precise capture of fine values (electrical interference and background noise gets louder than the tiny values in analogue data at some point, so you lose those trailing decimal points, as it were), so in audio you get much crisper sounding cymbals, and in pictures and video, the image is much more sharp.

#### Analogue > Digital 


The major downside to digital data however, lies in its strength: as soon as the quality of the signal starts to drop, the readability of the digital data drops off quickly. It's called the [Digital Cliff Effect](https://en.wikipedia.org/wiki/Digital_cliff_effect), and it's a major problem for DAB radio and digital TV (freeview), because radio transmission signal strength is always going to be affected by lots of real-world factors like mountains, transmitter distance, interference from unshielded electric technology, weather...

Analogue copes much better with drops in signal quality; the data remains readable all the way down the SNR ([Signal-Noise_Ratio](https://en.wikipedia.org/wiki/Signal-to-noise_ratio)) line, proportionate to the signal quality. Once digital data gets below about 80% signal strength / uncorrupted data, then the entire thing usually becomes completely unreadable.

The reason I've talked at length about this, is because another things which causes signal strength drop, or more relevantly, _data corruption_, is **time**.

Over time, your poor little hard drive will suffer magnetic interference from all sorts of other, brash appliances. It has to, due to laws about accepting interference and all that. All of those EM waves [^1]. This happens whenever your HDD is turned on, or is on; but what about when your disk remains turned off for a year?
[^1]: Even the Sun generates EM pulses, during [solar flares](https://en.wikipedia.org/wiki/Solar_flare)!)) will slowly corrupt all the little 1s and 0s on your disks platters. Now, in normal operations, this isn't really a problem, because along with the visible storage you can use on your disk, it also has hidden,  internal storage space set aside used to check bits for corruption, and repair a certain percentage of corrupted data, from the checking bits ((I believe they are XORs of 2 other bits, but i'm not sure at this point
The amount of data-corrupting effects it will be exposed to in that time will be far more than the short bursts of whatever in between the daily (or, at most, weekly) start ups the average hard drive tolerates.

And this is why, in my opinion, computers should incorporate some kind of analogue storage medium. But other than that, I don't really know where I'm going with this. At the moment, there are no analogue storage formats I know of [^2] which computers can read. Hopefully this will change.
[^2]: tape disks don't count, because the data that is stored on them is still digital, so they'd still suffer the same effects.

# Requirements 


If this project is going to succeed as a digital repository of family memories that my adult grandchildren will be able to look at (and probably convert to another format themselves), then it has to fulfill certain properties in every stage of its implementation:-

  * **Future-Proof**(software): I don't want to have successfully preserved my family photos on disk for 30 years, only to find no-one can read JPEGs anymore. In order to prevent such natural obsolescence of technology from making my data unreadable, then I need to make sure my formats are: Open-Source and popular, preferably both.
      * Open source means that there will be more public documentation about the format, and if needs be, there will be old source code out there to help with reimplementing. Hell, there will probably already _be_ projects to keep the old format alive, without my contributions, thanks to the garden-shed-tinkerer mentality of the OSS community. Better than the method I need to see my parents when they were young, rotting in some uncooperative corporate basement vault somewhere. Shudder.
      * Popularity simply means that if I want to access this old format in 30 years, then with a popular format, others will be more likely to as well, making it easier to find help and old experts and such.
  * Future-Proof(hardware): This obviously means I won't be storing my backupos on floppy or IDE PATA hard disk (if that were even physically possible), but what about CD? it's a medium which has been around already for 30 years; and as a pc data container for 20. It is relatively physically robust [^3], but will it still be around in another 30 years? Will I (or my kids) still be able to get hold of a CD-ROM or compatible drive? the answer, unfortunately, I think is no.
[^3]: if you use good-quality archival CD-Rs, or so I'm told.
  * 
  * **Robust**:
  * **Cheap**(ish): Money is tight at the moment, and so I'm working on a (very) limited budget. That's not ideal in a  backup project, as storage media cost money, but fortunately I am used to this situation, so I can probably work around it.

# Hardware 


## Storage Medium 


## Copies 


In order to plan against unforeseen circumstances (burglary, flooding, house fires...), I need to have copies of this data in as many geographically disparate locations as possible.

My first thoughts are to have a copy (perhaps a master copy which the others sync to?) here [^4] with me my and partner; then my parent's house (I'm sure they won't mind having a hard drive or two, perhaps a PC tower, sitting somewhere if it's for a good cause). Next, preferably, I want to give a copy to my sister and her fiancee.
[^4]: currently in Slaidburn drive

The idea being, a copy in every household whom the data relates to. If my brother had his own, separate household, I'd give him a copy too.

These physical copies will have their own requirements:

  * Compact: I'll need to come up with official maximum dimensions and shape, but if I'm going for a fully-working, self-contained computer in every install, then no larger than the average plastic storage crate should do. If it's just a collection of hard drives (possibly using a Raspberry Pi for the computer part!), then an actual plastic storage crate will be perfect :)
  * **Robust**: The people whose homes this mysterious box goes into aren't going to know how, or even want to, to do any work to look after it properly. It's probably going to be shoved into a corner, or an attic, where temperatures could range from anything like -5C to 40C (attics get hot in the summer). It could be damp, and it could even have several 10s of kg of other domestic baggage piled on top of it. So these copies need to be relatively durable.

## Capture Technique 


There's hundreds of hours of home video on VHS tape that I need to capture at 1:1 playback speed. This is obviously going to take a [long time](tapingtime) if I do it serially (one at a time, one after the other), so capturing in parallel is probably going to be a good idea. This means using video multiple capture cards ( I have 1 PCI one, and a USB2.0 one), which means multiple PCs.

# Software 


## Video Format 


Here I need to decide on a future-proof, robust(won't panic and become unreadable if there's a corrupt byte here and there, including the header) video format which offers good compression (lossless? that would be expensive).

## File System 

[ZFS](https://en.wikipedia.org/wiki/Zfs) seems to be the best choice for long-term backup, having been designed specifically for [NAS](https://en.wikipedia.org/wiki/Network-attached_storage) systems. Its only fault is that it's designed by Sun, which means it's now owned by Oracle, who are dicks. In other words when they 'retire' the project in 20 years or so (or whatever), they'll probably just bin it, rather than release source code or anything, essentially cutting support dead. I'm not sure if it is possible to have a closed-source filesystem (probably patents will do the trick), but it is a worry that access to a filesystem will be entirely dictated by the selfish whim of an even more selfish company, whose only concern is profit.



My plan for a robust, distributed, future-proof, and cheap, home video backup solution.

%tags: plan, software
