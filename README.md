# inkscape-export-bezier-curve

Inkscape extension for exporting Bezier curve segments.

## Installation

Copy `ExportBezierCurve.{py,inx}` to your Inkscape extension directory.

The default directory is something like: `~/.config/inkscape/extensions`.

You can configure Inkscape directories through Preferences: `Edit > Preferences > System > User extensions`.

## Operation

 1. Select curve object
 2. Click `Extensions > Export > Export Bezier Curve`
 
This should bring up a popup window, the extension debug dialog. The dialog box should show Bezier curve segments in the main text area.

See, for example, [MDN documentation on SVG curves](https://developer.mozilla.org/en-US/docs/Web/SVG/Tutorial/Paths#line_commands) for details on how to parse the raw curve path data.
