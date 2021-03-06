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

Or, to add a new note with tags:
```bash
mimir This is a note with a @tag
```

The note will be added to `.mimir/mimir_notes.txt`

To show notes:
```bash
mimir -s 1
mimir -s 2
```
Will show the last one and two notes, respectively.

```bash
mimir @tag1
mimir @tag1 @tag2
```
If only tags are provided to mimir, it will assume you want to search by tags, rather than create a new note

Notes can also be searched via date fences:
```bash
mimir --since 2010 --until october
mimir --since june
mimir --until 2015
```
Date fences can be mixed with tags and the -s option for more fine grained searching.

To edit notes:
```bash
mimir edit
```
This will open the mimir notes file in your specified editor (this must be set in .mimir-config)

All notes in your Mimir notes file can be synced to an Evernote account. This requires an evernote account, as well as api keys.
Instuctions to acquire these are provided in the app:
```bash
mimir sync -- syncs your notes file with the Evernote folder specified in your config file (MimirNotes by default)
mimir generate_evernote_token -- Walks you through creating an access token for syncing
```

Finally, you can also view the status of your mimir, view a count of all tags present, or delete it entirely:
```bash
mimir status
mimir tags
mimir delete
```

## Installation

Install via pip:
```bash
pip install mimirnotes
```

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