Let's say you have two machines, Alice and Bob.

Alice is a machine you want to use Android Studio on, to compile and run dev builds from.

But Alice can't access an Android device normally. Maybe:

* your organisation's IT policy prevents you connecting phones via USB 
* Alice's hardware specs are too slow to run Android Studio, a browser and an emulator on the same computer
* Alice is running on a virtal machine itself, and the VM hasn't been configured to allow running an emulator on it
* You *do* have a phone you can run the app on, but you need to test a different hardware profile, 
	eg a phone with a tiny screen, an old version of Android, or a phone without Bluetooth capability.


Fortunately for you, you have another computer, Bob, which *can* run the emulator you want.

The only thing is, the android emulator is set up to doesn't connect directly to your network; it's sat behind a virtual router, and can't be accessed directly.

If using Virtual Box you'll want to set your virtual machine to use Bridged Networking,
which allows the guest machine to act as if it was just another device on the same LAN as the host.
It can access LAN machines, and they can access it. 

You could try running the emulator on Harry, the host machine,
but Harry's firewall policies (controlled by IT, which you can't change)
don't allow you to forward the necessary ports.

------------------------------------------------------------------------------

on the machine Bob, running the emulator:
sudo apt-get install redir
redir :6666 :5555

# on machine Alice, running Android Studio:
open Android Studio settings and search for adb
go to Debugger
Under 'ADB Service lifecycle management', select Use existing manually managed server
	for 'Existing ADB server port', put 5038

run
adb connect -P 5038 <Bob's IP>:5555
