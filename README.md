Licence Snippets for Sublime Text
=================================

This package provides the full text (for LICENCE files) as well as 
the recommended header text for several popular open-source licences 
as [Sublime Text](http://www.sublimetext.com/) snippets. It makes 
inserting licence text in your source files quick and easy. 

The licences included in this package are all 
[OSI-Approved](http://opensource.org/licenses/category).

Feel free to submit an 
[issue](https://github.com/sijk/sublime-licence-snippets/issues/new) or 
[pull request](https://github.com/sijk/sublime-licence-snippets/pulls) 
if there's a licence you'd like added.


### Installation

##### Package Control
The easiest and best way to manage Sublime Text packages is with 
[Package Control][].

1. Install [Package Control][] if you haven't already.
2. Choose *Install Package* from the command palette.
3. Select *Licence Snippets* and press Enter. Easy.

[Package Control]: http://wbond.net/sublime_packages/package_control

##### Git

You can clone [this repository](https://github.com/sijk/sublime-licence-snippets) 
into your Sublime Text *Packages* directory. You really should use 
Package Control, though.

##### Zip

You can download a zip file from 
[here](https://github.com/sijk/sublime-licence-snippets/archive/master.zip) 
and extract it to your Sublime Text *Packages* directory. But seriously, 
just install Package Control.

### Usage

To insert, for example, the MIT licence in a source file, open the 
command palette, type *mit* and choose *Licence Snippet: MIT [Header] 
[Full Text]* (or choose *Licence Snippet: MIT [Header] [Full Text]* from 
the snippets menu). The licence text will be inserted at the cursor. The 
copyright details (year, author, organization, etc.) will be highlighted 
in turn so that you can easily tab between them and modify them if 
necessary. 

- Licences suffixed with *[Header]* are intended to be used in the header 
section of a file in your project.
- Licences suffixed with *[Full Text]* are ideally used to fill LICENCE or 
LICENCE.txt files.

### Configuration

Two settings are available to configure the behaviour of this plugin. 
To set them, choose *Preferences > Settings - User* and add a line 
for the setting you want to change.

- *licence_comment_style* = *none*, *line*, or *block* (default: *line*)
- *licence_wrap_lines* = *True* or *False* (default: *False*)
