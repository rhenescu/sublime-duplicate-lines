import sublime, sublime_plugin

class DuplicateLinesCommand(sublime_plugin.TextCommand):
    def run(self, edit, direction = 0):
        for selection in self.view.sel():
            # Exclude trailing newline from non-empty selections
            if not selection.empty() and self.view.substr(selection.end() - 1) == '\n':
                selection = sublime.Region(selection.begin(), selection.end() - 1)

            # Include everything from the beginning of the first line
            # to the end of the last line of the current selection
            lines    = self.view.line(selection)
            begin    = lines.begin()
            end      = lines.end()
            contents = self.view.substr(lines)

            if direction:
                # Duplicate below (keep selection in place, insert above)
                self.view.insert(edit, begin, contents + '\n')
            elif end == self.view.size():
                # Duplicate above, if the selection includes the last line in the document
                self.view.insert(edit, end, '\n' + contents)
                # Reposition the cursor if at EOF, since it remains at EOF after duplication
                if end == selection.begin():
                    self.view.sel().subtract(sublime.Region(self.view.size(), self.view.size()))
                    self.view.sel().add(sublime.Region(end, end))
            else:
                # Duplicate above (keep selection in place, insert below)
                self.view.insert(edit, end + 1, contents + '\n')
