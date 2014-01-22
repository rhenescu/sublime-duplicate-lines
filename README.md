Duplicate Lines (Sublime Text 3 plugin)
=======================================
A plugin that duplicates the selected lines above or below. The behavior is similar to that of Eclipse, but allows multiple selections/cursors.

Installation
------------
* Download the repository as a zip file
* In Sublime, go to Preferences > Browse Packages
* Extract the "sublime-duplicate-lines-master" folder in the zip file to the "Packages" folder that just opened
* Rename the extracted folder to "Duplicate Lines"
* Back in Sublime, go to Preferences > Key Bindings (User) and add the following bindings

```
    { "keys": ["ctrl+alt+up"],   "command": "duplicate_lines", "args": { "direction": 0 } },
    { "keys": ["ctrl+alt+down"], "command": "duplicate_lines", "args": { "direction": 1 } },
```

* (Optional) Replace ctrl+alt+up and ctrl+alt+down with your own key bindings
