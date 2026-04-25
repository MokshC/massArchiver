#!/usr/bin/env python

# Created by: Moksh Chitkara
# Last Update: April 24th 2026
# v0.1.0
# Copyright (C) 2026  Moksh Chitkara
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

# Global Variables
projectManager = resolve.GetProjectManager()

def main_ui():

	# vertical group
	window = [ui.VGroup({"Spacing": 10,},[			

			# Prefix and Suffix
			ui.HGroup({"Spacing": 10}, [

        ui.Tree({"ID": "proj_browser", 'SortingEnabled': 'true', 'AlternatingRowColors': True, 'SelectionMode': 'ExtendedSelection',
					'Events': {'ItemDoubleClicked': True, 'ItemClicked': True}, "Weight": 10}),

			]),

			# browser for projects and timelines
			ui.Tree({"ID": "proj_browser", 'SortingEnabled': 'true', 'AlternatingRowColors': True, 'SelectionMode': 'ExtendedSelection',
					'Events': {'ItemDoubleClicked': True, 'ItemClicked': True}, "Weight": 10}),

			# Buttons
			ui.HGroup({"Spacing": 20}, [
				ui.Button({"ID": "archive","Text": "Archive", "Weight": 1}),
        ui.Button({"ID": "list","Text": "Add Selected", "Weight": 1}),
			]),
		])]

	return window

################################################################################################
# Window creation #
###################

ui = fu.UIManager # get UI utility from fusion
disp = bmd.UIDispatcher(ui) # gets display settings?

# window definition
window = disp.AddWindow({"WindowTitle": "Mass Archiver",
			"ID": "MAWin", 
			'WindowFlags': {'Window': True,'WindowStaysOnTopHint': True},
			"Geometry": [100,700,480,500], # x-position, y-position, width, height
			}, 
			main_ui())


itm = window.GetItems() # Grabs all UI elements to be manipulated

################################################################################################
# Functions #
#############


# needed to close window
def _close(ev):
	disp.ExitLoop()

################################################################################################
# GUI Elements #
# manipulations
_treeBuild("databases")
# button presses
window.On.MAWin.Close = _close
window.On.proj_browser.ItemDoubleClicked = _treeBuild
window.On.archive.Clicked = _main
# window loops
window.Show()
disp.RunLoop()
window.Hide()
#################################################################################################
