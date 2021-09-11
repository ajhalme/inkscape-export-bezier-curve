#!/usr/bin/env python3
#
# Export the Bezier curve segments of the selected object.

import inkex
import sys

from inkex import paths
from inkex.utils import debug

class ExportBezierCurve(inkex.Effect):
        
    def effect(self):
        for id, node in self.svg.selected.items():
            if node.tag != inkex.addNS('path','svg'):
                continue
            
            node.apply_transform()
            d = node.get('d')
            p = paths.CubicSuperPath(d)
            for path in p.to_segments():
                debug(path)

ExportBezierCurve().run()
sys.exit(0)
