#!/usr/bin/env python3

import time

from cortexutils.analyzer import Analyzer


class Template(Analyzer):

    def __init__(self):
        Analyzer.__init__(self)

    def artifacts(self, raw):
        artifacts = []

        artifacts.append(
          self.build_artifact(self.data_type, self.getData(), tags=["template"], tlp=self.tlp)
        )

        return artifacts

    def run(self):
        if self.data_type not in ['domain', 'ip']:
            self.notSupported()

        time.sleep(self.getParam("config.delay", 60))

        self.report({'data': self.getData(), 'input': self._input})

    def summary(self, raw):
        taxonomies = []

        taxonomies.append(
            self.build_taxonomy('info', 'Cortex-Analyzer-Template', 'Records', time.time())
        )
        taxonomies.append(
            self.build_taxonomy('info', 'Cortex-Analyzer-Template', self.data_type, self.getData())
        )

        return {"taxonomies": taxonomies}


if __name__ == '__main__':
    Template().run()
