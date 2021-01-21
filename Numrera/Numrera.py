# By: Oscar Lundqvist https://github.com/lunk/SublimePlugins

import sublime
import sublime_plugin


class NumreraCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        sels = self.view.sel()
        counter = 0
        for sel in sels:
            counter += 1
            pos = sel.end()
            self.view.insert(edit, pos, str(counter))

        self.view.set_status("numrera", "Numrerade {} markeringar".format(counter))


# asdf1
# asdf2
# asdf3
# asdf4
# asdf5
