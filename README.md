Duplicate Lines (Sublime Text 3 plugin)
=======================================
A plugin that duplicates the selected lines above or below. The behavior is similar to that of Eclipse, but allows multiple selections/cursors.

Installation
------------
1. Download the repository as a zip file
2. In Sublime, go to Preferences > Browse Packages
3. Extract the "sublime-duplicate-lines-master" folder in the zip file to the "Packages" folder that just opened
4. Rename the extracted folder to "Duplicate Lines"
5. Back in Sublime, go to Preferences > Key Bindings (User) and add the following bindings
```
    { "keys": ["ctrl+alt+up"],   "command": "duplicate_lines", "args": { "direction": 0 } },
    { "keys": ["ctrl+alt+down"], "command": "duplicate_lines", "args": { "direction": 1 } },
```
6. (Optional) Replace ctrl+alt+up and ctrl+alt+down with your own key bindings
