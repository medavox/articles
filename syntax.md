# Formatting Syntax 


<doku>DokuWiki> supports some simple markup language, which tries to make the datafiles to be as readable as possible. This page contains all possible syntax you may use when editing the pages. Simply have a look at the source of this page by pressing "Edit this page". If you want to try something, just use the [playground](playground:playground) page. The simpler markup is easily accessible via <doku>toolbar|quickbuttons>, too.

## Basic Text Formatting 


DokuWiki supports **bold**, _italic_, __underlined__ and `monospaced` texts. Of course you can **___`combine`___** all these.

    DokuWiki supports **bold**, _italic_, __underlined__ and `monospaced` texts.
    Of course you can **___`combine`___** all these.

You can use ~subscript~ and ^superscript^, too.

    You can use ~subscript~ and ^superscript^, too.

You can mark something as ~~deleted~~ as well.

    You can mark something as ~~deleted~~ as well.

**Paragraphs** are created from blank lines. If you want to **force a newline** without a paragraph, you can use two backslashes followed by a whitespace or the end of line.

This is some text with some linebreaks  
Note that the
two backslashes are only recognized at the end of a line  
or followed by  
a whitespace \\this happens without it.


### External Links 


External links are recognized automagically: http:_www.google.com or simply www.google.com - You can set the link text as well: [This Link points to google](http:_www.google.com). Email addresses like this one: <andi@splitbrain.org> are recognized, too.

### Internal 


Internal links are created by using square brackets. You can either just give a <pagename> or use an additional [link text](pagename).

<doku>pagename|Wiki pagenames> are converted to lowercase automatically, special characters are not allowed.

Linking to a specific section is possible, too. Just add the section name behind a hash character as known from HTML. This links to [this Section](syntax#internal).

    This links to [this Section](syntax#internal).

Notes:

  * Links to [existing pages](syntax) are shown in a different style from <nonexisting> ones.
  * DokuWiki does not use <wp>CamelCase> to automatically create links by default, but this behavior can be enabled in the <doku>config> file. Hint: If DokuWiki is a link, then it's enabled.
  * When a section's heading is changed, its bookmark changes, too. So don't rely on section linking too much.

    LANG.nosmblinks = `;

### Image Links 


You can also use an image to link to another internal or external page by combining the syntax for links and [images](#images_and_other_files) (see below) like this:

    [{{wiki:dokuwiki-128.png}}](http:_www.php.net)

[{{wiki:dokuwiki-128.png}}](http:_www.php.net)

Please note: The image formatting is the only formatting syntax accepted in link names.

The whole [image](#images_and_other_files) and [link](#links) syntax is supported (including image resizing, internal and external images and URLs and interwiki links).

## Footnotes 


You can add footnotes [^5] by using double parentheses.
[^5]: This is a footnote

    You can add footnotes [^6] by using double parentheses.
[^6]: This is a footnote

## Sectioning 


You can use up to five different levels of headlines to structure your content. If you have more than three headlines, a table of contents is generated automatically -- this can be disabled by including the string `<nowiki>~~NOTOC~~</nowiki>'' in the document.

### Headline Level 3 

#### Headline Level 4 

##### Headline Level 5 


    ==== Headline Level 3 ====
    === Headline Level 4 ===
    == Headline Level 5 ==

By using four or more dashes, you can make a horizontal line:

----

## Images and Other Files 


You can include external and internal <doku>images> with curly brackets. Optionally you can specify the size of them.

Real size:                        {{wiki:dokuwiki-128.png}}

Resize to given width:            {{wiki:dokuwiki-128.png?50}}

Resize to given width and height[^7]: {{wiki:dokuwiki-128.png?200x50}}
[^7]: when the aspect ratio of the given width and height doesn't match that of the image, it will be cropped to the new ratio before resizing

Resized external image:           {{http://de3.php.net/images/php.gif?200x50}}

    Real size:                        {{wiki:dokuwiki-128.png}}
    Resize to given width:            {{wiki:dokuwiki-128.png?50}}
    Resize to given width and height: {{wiki:dokuwiki-128.png?200x50}}
    Resized external image:           {{http://de3.php.net/images/php.gif?200x50}}


By using left or right whitespaces you can choose the alignment.

{{ wiki:dokuwiki-128.png}}

{{wiki:dokuwiki-128.png }}

{{ wiki:dokuwiki-128.png }}

    {{ wiki:dokuwiki-128.png}}
    {{wiki:dokuwiki-128.png }}
    {{ wiki:dokuwiki-128.png }}

Of course, you can add a title (displayed as a tooltip by most browsers), too.

{{ wiki:dokuwiki-128.png |This is the caption}}

    {{ wiki:dokuwiki-128.png |This is the caption}}

If you specify a filename (external or internal) that is not an image (`gif, jpeg, png`), then it will be displayed as a link instead.

For linking an image to another page see <#Image Links> above.

## Lists 


Dokuwiki supports ordered and unordered lists. To create a list item, indent your text by two spaces and use a `*` for unordered lists or a `-` for ordered ones.

  * This is a list
  * The second item
      * You may have different levels
  * Another item

  #.  The same list but ordered
  #.  Another item
      #.  Just use indention for deeper levels
  #.  That's it


```

  * This is a list
  * The second item
      * You may have different levels
  * Another item

  #.  The same list but ordered
  #.  Another item
      #.  Just use indention for deeper levels
  #.  That's it

```


Also take a look at the <doku>faq:lists|FAQ on list items>.

## Text Conversions 


DokuWiki can convert certain pre-defined characters or strings into images or other text or HTML.

### Text to HTML Conversions 


Typography: <DokuWiki> can convert simple text characters to their typographically correct entities. Here is an example of recognized characters.

-> <- <-> => <= <=> >> << -- --- 640x480 (c) (tm) (r)
"He thought 'It's a man's world'..."


```

-> <- <-> => <= <=> >> << -- --- 640x480 (c) (tm) (r)
"He thought 'It's a man's world'..."

```


The same can be done to produce any kind of HTML, it just needs to be added to the <doku>entities|pattern file>.

There are three exceptions which do not come from that pattern file: multiplication entity (640x480), 'single' and "double quotes". They can be turned off through a <doku>config:typography|config option>.

## Quoting 


Some times you want to mark some text to show it's a reply or comment. You can use the following syntax:

    I think we should do it
    
  > No we shouldn't
    
  >> Well, I say we should
    
  > Really?
    
  >> Yes!
    
  >>> Then lets do it!

I think we should do it

> No we shouldn't

>> Well, I say we should

> Really?

>> Yes!

>>> Then lets do it!

## Tables 


DokuWiki supports a simple syntax to create tables.

| Heading 1      | Heading 2       | Heading 3          |
|----------------|-----------------|--------------------|
| Row 1 Col 1    | Row 1 Col 2     | Row 1 Col 3        |
| Row 2 Col 1    | some colspan (note the double pipe) ||
| Row 3 Col 1    | Row 3 Col 2     | Row 3 Col 3        |

Table rows have to start and end with a `|` for normal rows or a `^` for headers.

    ^ Heading 1      ^ Heading 2       ^ Heading 3          ^
    | Row 1 Col 1    | Row 1 Col 2     | Row 1 Col 3        |
    | Row 2 Col 1    | some colspan (note the double pipe) ||
    | Row 3 Col 1    | Row 3 Col 2     | Row 3 Col 3        |

To connect cells horizontally, just make the next cell completely empty as shown above. Be sure to have always the same amount of cell separators!

Vertical tableheaders are possible, too.

|              ^ Heading 1            ^ Heading 2          ^
^ Heading 3    | Row 1 Col 2          | Row 1 Col 3        |
^ Heading 4    | no colspan this time |                    |
^ Heading 5    | Row 2 Col 2          | Row 2 Col 3        |

As you can see, it's the cell separator before a cell which decides about the formatting:

    |              ^ Heading 1            ^ Heading 2          ^
    ^ Heading 3    | Row 1 Col 2          | Row 1 Col 3        |
    ^ Heading 4    | no colspan this time |                    |
    ^ Heading 5    | Row 2 Col 2          | Row 2 Col 3        |

You can have rowspans (vertically connected cells) by adding `:::` into the cells below the one to which they should connect.

| Heading 1      | Heading 2                  | Heading 3          |
|----------------|----------------------------|--------------------|
| Row 1 Col 1    | this cell spans vertically | Row 1 Col 3        |
| Row 2 Col 1    | :::                        | Row 2 Col 3        |
| Row 3 Col 1    | :::                        | Row 2 Col 3        |

Apart from the rowspan syntax those cells should not contain anything else.

    ^ Heading 1      ^ Heading 2                  ^ Heading 3          ^
    | Row 1 Col 1    | this cell spans vertically | Row 1 Col 3        |
    | Row 2 Col 1    | :::                        | Row 2 Col 3        |
    | Row 3 Col 1    | :::                        | Row 2 Col 3        |

You can align the table contents, too. Just add at least two whitespaces at the opposite end of your text: Add two spaces on the left to align right, two spaces on the right to align left and two spaces at least at both ends for centered text.

|           Table with alignment           |||
|------------------------------------------|||
|         right|    center    |left          |
|left          |         right|    center    |
| xxxxxxxxxxxx | xxxxxxxxxxxx | xxxxxxxxxxxx |

This is how it looks in the source:

    ^           Table with alignment           ^^^
    |         right|    center    |left          |
    |left          |         right|    center    |
    | xxxxxxxxxxxx | xxxxxxxxxxxx | xxxxxxxxxxxx |

Note: Vertical alignment is not supported.

## No Formatting 


If you need to display text exactly like it is typed (without any formatting), enclose the area either with `%%<nowiki>%%` tags or even simpler, with double percent signs `<nowiki>%%</nowiki>`.

<nowiki>
This is some text which contains addresses like this: http://www.splitbrain.org and **formatting**, but nothing is done with it.
</nowiki>
The same is true for %%___this__ text_ with a smiley ;-)%%.

    <nowiki>
    This is some text which contains addresses like this: http://www.splitbrain.org and **formatting**, but nothing is done with it.
    </nowiki>
    The same is true for %%___this__ text_ with a smiley ;-)%%.

## Code Blocks 


You can include code blocks into your documents by either indenting them by at least two spaces (like used for the previous examples) or by using the tags `%%
```
%%` or `%%<file>%%`.

    This is text is indented by two spaces.

<code>
This is preformatted code all spaces are preserved: like              <-this

```


<file>
This is pretty much the same, but you could use it to show that you quoted a file.
</file>

Those blocks were created by this source:

      This is text is indented by two spaces.

    
```

    This is preformatted code all spaces are preserved: like              <-this
    
```


    <file>
    This is pretty much the same, but you could use it to show that you quoted a file.
    </file>

### Syntax Highlighting 


<wiki:DokuWiki> can highlight sourcecode, which makes it easier to read. It uses the [GeSHi](http://qbnz.com/highlighter/) Generic Syntax Highlighter -- so any language supported by GeSHi is supported. The syntax uses the same code and file blocks described in the previous section, but this time the name of the language syntax to be highlighted is included inside the tag, e.g. `<nowiki>```java
</nowiki>` or `<nowiki><file java></nowiki>`.

<code java>
/**
 * The HelloWorldApp class implements an application that
 * simply displays "Hello World!" to the standard output.
 */
class HelloWorldApp {
      public static void main(String[] args) {
          System.out.println("Hello World!"); //Display the string.
      }
}

```


The following language strings are currently recognized: _4cs, 6502acme, 6502kickass, 6502tasm, 68000devpac, abap, actionscript-french, actionscript, actionscript3, ada, algol68, apache, applescript, asm, asp, autoconf, autohotkey, autoit, avisynth, awk, bascomavr, bash, basic4gl, bf, bibtex, blitzbasic, bnf, boo, c, c_loadrunner, c_mac, caddcl, cadlisp, cfdg, cfm, chaiscript, cil, clojure, cmake, cobol, coffeescript, cpp, cpp-qt, csharp, css, cuesheet, d, dcs, delphi, diff, div, dos, dot, e, epc, ecmascript, eiffel, email, erlang, euphoria, f1, falcon, fo, fortran, freebasic, fsharp, gambas, genero, genie, gdb, glsl, gml, gnuplot, go, groovy, gettext, gwbasic, haskell, hicest, hq9plus, html, html5, icon, idl, ini, inno, intercal, io, j, java5, java, javascript, jquery, kixtart, klonec, klonecpp, latex, lb, lisp, llvm, locobasic, logtalk, lolcode, lotusformulas, lotusscript, lscript, lsl2, lua, m68k, magiksf, make, mapbasic, matlab, mirc, modula2, modula3, mmix, mpasm, mxml, mysql, newlisp, nsis, oberon2, objc, objeck, ocaml-brief, ocaml, oobas, oracle8, oracle11, oxygene, oz, pascal, pcre, perl, perl6, per, pf, php-brief, php, pike, pic16, pixelbender, pli, plsql, postgresql, povray, powerbuilder, powershell, proftpd, progress, prolog, properties, providex, purebasic, pycon, python, q, qbasic, rails, rebol, reg, robots, rpmspec, rsplus, ruby, sas, scala, scheme, scilab, sdlbasic, smalltalk, smarty, sql, systemverilog, tcl, teraterm, text, thinbasic, tsql, typoscript, unicon, uscript, vala, vbnet, vb, verilog, vhdl, vim, visualfoxpro, visualprolog, whitespace, winbatch, whois, xbasic, xml, xorg_conf, xpp, yaml, z80, zxbasic_

### Downloadable Code Blocks 


When you use the `%%
```
%%` or `%%<file>%%` syntax as above, you might want to make the shown code available for download as well. You can do this by specifying a file name after language code like this:

<code>
```php
%include ../includes/myexample.php
```


```


```php
%include ../includes/myexample.php
```


If you don't want any highlighting but want a downloadable file, specify a dash (`-`) as the language code: `%%<code - myfile.foo>%%`.


## Embedding HTML and PHP 


You can embed raw HTML or PHP code into your documents by using the `%%<html>%%` or `%%<php>%%` tags. (Use uppercase tags if you need to enclose block level elements.)

HTML example:


```

<html>
This is some <span style="color:red;font-size:150%;">inline HTML</span>
</html>
<HTML>
<p style="border:2px dashed red;">And this is some block HTML</p>
</HTML>

```


<html>
This is some <span style="color:red;font-size:150%;">inline HTML</span>
</html>
<HTML>
<p style="border:2px dashed red;">And this is some block HTML</p>
</HTML>
