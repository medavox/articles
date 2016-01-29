# General-Purpose TextMode Text Editor


Here's an idea which will hopefully become more than that as time passes.

## Background


There is currently no command line text editor that follows the design principle [of least surprise](http://en.wikipedia.org/wiki/Principle_of_least_astonishment):

I can't fire up nano, or Vim (and i shudder to even think of installing emacs), and use ctrl+left or right to move between words; I can't hold shift and press End to select to the end of the line. If I want to do something that 'advanced', I'd have to learn Vim.

No thanks. I won't learn a completely different muscle-memory language for editing text files in one particular context (purely for political or historical reasons), when all these keyboard shortcuts work perfectly in every other editor I use (Eclipse, netbeans, notepad++, geany, gedit....).

The ctrl+arrow stuff is so standard, it's implemented in Android text-input boxes.

If we can have this functionality in our mobile phones, why not in our ssh sessions?

Nothing about text-mode text editing prevents this, so why hasn't it been invented yet?

So I'll invent it.

In all likelihood, this'll be a fork of nano.

## Libraries


  * I'll most likely be using [this keyboard input handling library](http://www.leonerd.org.uk/code/libtermkey/), which claims to be able to capture ctrl-arrow keypresses.
  * [Ncurses](https://www.gnu.org/software/ncurses/ncurses.html) will still be able to provide text-based layout and things.

## Design Document


  * Written in C, primarily for POSIX/UNIX systems (read:linux)
  * Portable!


Let's start listing features this text editor will have.

### Display

  * Line numbers permanently along the left-hand side
  * Number of occurrences displayed when searching
  * Column number, word count displayed at bottom. Current line number highlighted (inverted) in line numbers.

### Behaviour

  * WILL NOT be tabbed, or open >1 file simultaneously; dammit Jim, it's a text editor, not an IDE!
  * Will have syntax highlighting
      * Using an existing language's syntax files (nano's or vim's will do), to reduce user learning overhead (and provide instant language support)
  * WILL highlight selected text with inverted colouring
  * WILL NOT support Vim keystroke emulation in any way; anyone who has taken the time and effort to learn vim probably still knows how to use the standard text-editing interface that everyone else has used for 15+ years.
      * Also they'll always just be able to use Vim anyway, as Vim runs anywhere this will.
  * Corresponding bracket highlighting
  * Smooth scrolling
  * WILL NOT be able to start a new file inside the editor;
      * Do that in the shell, then open that file for editing.
      * Or start the editor with a non-existent filename as an argument.
  * typing any valid keys on the keyboar without a modifier key will insert/overwrite those characters at the current point
  * Will respect the decades-old insert/overwrite modes, switched with the Insert key
  * UNDO AND REDO! (how hard can it be to write a linked-list stack of textfile state, and add to it every time the user modifies the file?)

### Possible/Future Extras

  * gpm-based mouse support???
  * File-menu style menu simulation, reachable by pressing alt or clicking (with mouse support) the top of the screen

### Keyboard shortcuts


The idea is, you (or your fingers) should be able to guess all these. These are only a reminder so I know what I'll have to implement.

#### Navigating Text

| Key        | Action              |
|------------|---------------------|
| left       | move left one char  |
| right      | move right one char |
| up         | move up one line    |
| down       | move down one line  |
| Ctrl+left  | move left one word  |
| Ctrl+right | move right one word |
| Home       | move to (non-whitespace) start of line |
| End        | move to (non-whitespace) end of line |
| Ctrl+Home  | move to start of file |
| Ctrl+End   | move to end of file   |
| Ctrl+F     | find a string in the file   |
| Ctrl+H     | replace a string in the file (opens a small ncurses dialog)   |
| F3         | move to next occurrence   |
| shift+F3, shift+n | move to previous occurrence |
| Ctrl+X     | Cuts any selected text   |
| Ctrl+C     | Copies any selected text |
| Ctrl+V     | Pastes clipboard at caret marker |
| Ctrl+D     | Duplicates the current line (duplicated line is below) |
| Ctrl+K     | Deletes (Kills) the current line (file moves up to fill gap) |
| Ctrl+L     | Goes to a line (small dialog popup) |
| Ctrl+T     | Swaps (Transposes) the current line with the line above |

#### File System

| Key        | Action              |
|------------|---------------------|
| Ctrl+S     | Save a file (single-line filename prompt) |
| Ctrl+O     | Open a file (single-line filename prompt) |

#### Misc

| Key        | Action              |
|------------|---------------------|
| Insert     | Toggle between insert and overwrite modes (have this displayed in the same pseudo-status bar as column number) |
| Ctrl+X, Alt+X, Ctrl+W | Closes the editor. Prompts if you want to save any unsaved changes first (if there are any). |

Here's some extended [nano functionality](http://chxo.com/be2/nano_find_replace.html) I could co-opt into making this sane fork of nano.

## Links 


From my browser, originally.

### Similar Stuff


  * [JOE's own editor - another textmode text editor](http://joe-editor.sourceforge.net/)
  * [dex - a dextrous text editor](https://github.com/tihirvon/dex)
  * [http://www.yolinux.com/TUTORIALS/LinuxTextEditors.html](Linux text editors comparison on YoLinux)

### Useful Stuff


  * [a spiffy collection of nano syntax highlighting files](https://github.com/serialhex/nano-highlight)
  * [config file syntax highlighting for nano](https://bbs.archlinux.org/viewtopic.php?id=133595)
