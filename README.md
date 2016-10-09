## Synopsis

Mimir is a simple, command line based note taking application. Designed with git syntax and usage in mind, its aim is to
provide quick, concise notes, that can be easily included in the project/directory where they are created.

## Code Example

Mimir can be initialized within any directory. Each mimir instance keep track of its own notes.

Initialize mimir within a directory:
```bash
mimir init
```

This will create a new directory, .mimir, and a config file, .mimir/.mimir-config

Delete mimir from a directory:
```bash
mimir delete
```

This deletes the mimir present in the working directory. It will also delete any config files and all notes.

To create a new note, simply:
```bash
mimir This is my brand new note!
```

The note will be added to `.mimir/mimir_notes.txt`

To show notes:
```bash
mimir -s 2
mimir -s 1
```
Will show the last one and two notes, respectively.

To edit notes:
```bash
mimir edit
```
This will open the mimir notes file in your specified editor (this must be set in .mimir-config)

## Installation

Once working code exists, you will be able to install Mimir via pip

## Tests

Mimir uses Pytest for testing.

From the root project directory, simply run `pytest`

## License

Copyright (c) 2016 Jeremy Cerise

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:
The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.