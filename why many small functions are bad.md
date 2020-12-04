I follow a more functional style, where each function does one whole thing. 
It should have no side effects, so it will always produce the same output for a given input. 
This is also easier to test.

Prioritising code readability over complexity or 'cleverness' is a good goal, 
but not to the point of trying to translate an English sentence into a function name.

I've never been a fan of XP and 'clean code'. 
I think code which doesn't need any documentation AT ALL is an attractive myth.

It's attractive because writing documentation is such a hated task.
But I think that while it's better to write LESS documentation and fewer comments on autopilot 
(that ultimately add nothing to what was gleaned by reading the code itself 
https://blog.codinghorror.com/code-tells-you-how-comments-tell-you-why/).

Describing your intentions in human language will always be clearer 
than attempting to rephrase an entire sentence into aVeryLongMethodNamesLikeThis. 
Especially when the function always does exactly the same thing, 
because it takes no inputs and accesses no state.


A smattering of mindfully-written human-language explanation goes a long way, and can speed up onboarding.


65k method limit
---------------

It can add to the doc comment & testing burden (more functions to write tests & doc for) if any of these are not private.
Comments should be preferred over function definitions to explain rationale, as they add no performance cost whatsoever (whereas an app apk has more than 65k methods has to use a different format as a workaround to Android VM limitations, which may be slower) and if explanatory function names are followed with multi word function names, comments do not clutter up the rest of the code with calls to methods with very long names, potentially breaking the line length limit (80, 100, or 120 depending on the project)


I'm definitely NOT saying that we shouldn't give variables, functions and classes descriptive names; we absolutely should. 
But creating extra functions whose ONLY purpose is to describe the code, seems the wrong approach to me.

Functionality should be divided into individual tasks, but no further. 



Doing Less Than One Thing Per Function Is a Bad Idea
------------------------------------

https://medium.com/@copyconstruct/small-functions-considered-harmful-91035d316c29

The readability and performance cost, of pulling a block of functionality out of the surrounding execution context into its own function, 
is only worth it IFF that new function could be used in more than one place.


I'm also definitely NOT arguing for gigantic functions. 

Functions should Do One Thing, and no less.

As opposed to functions that Do 10% of the task,
then unconditionally pass the work on to the next function, 
which does another 10% (maybe in another part of the code base, meaning the reader has to break their train of thought to find the next part), 
which then calls the function to do the next 10%, and so on.

These groups of functions are often called as if they were one function, 
and are always (unconditionally) called in only one place by the next function in the chain.
They act like a baton relay-race. But code is already executed line by line, so this adds nothing but call complexity.

The 'Thing' in this metaphor should still be a small subtask of the larger goal. 
Functional composition is still desired. 
But only when that approach is appropriate.


Literate Programming
--------------------

Now that you've explained your rationale, I understand that the code style was an intentional design choice. 
But this decision had to be explained with words.
I couldn't have discovered that without a conversation with you about it.

If you were unavailable to explain your intention, there would be nowhere else that I could discover WHY you chose to architect it this way. I would be forced to either go along with the decision without understanding why (thereby preventing me from properly maintaining the code, because I couldn't understand when it is appropriate to change strategy), or refactor it to a known methodology, which is wasted time.

Comments aren't always bad
-------------------------

Even on this page http://www.codeodor.com/index.cfm/2008/6/18/Common-Excuses-Used-To-Comment-Code-and-What-To-Do-About-Them/2293 , 
the author admits in his point 1 (of reasons to document code) that doc comments should be written to document APIs that others will use.

In the case of our multi-developer, multi-platform software product, 'APIs others will use' means every non-private function and class, because this code needs to be understandable on its own by any future new starters, potentially without us around to explain it.

Point 4 (documenting design decisions) also applies, especially on Android, where workarounds for suboptimal design decisions by others (especially by the Android API itself) are common.

Readability
-----------

A clean code guide I refreshed myself with to also recommends favouring readability, which is a good idea.
But in my opinion, many small functions can harm this goal. 
These allow the flow of execution to jump around in a more nonlinear fashion than is necessary,
making the code harder to read and understand, 
because the reader has to break their train of thought and physically find the next piece of code that is executed.

A better way would be to comment each "paragraph" of related functionality within its surrounding function.

Has the readability of this approach actually been tested? 
As in, has the codebase been read, understood sufficiently and then modified by someone without prior knowledge?

In terms of fundamental clean code principles, I would argue that having many short zero-parameter arguments violates KISS and possibly YAGNI.
