#---------- Theme and UI Configuration -----------#

# The primary theme color for the application background
THEME_COLOR = "#15616d"

# Colors used for indicating correct and incorrect answers
WRONG_COLOR = "#c1121f"
RIGHT_COLOR = "#70e000"

#---------- Image Paths -----------#

# File paths for the images used in the GUI
TRUE_IMG = "images/true.png"
FALSE_IMG = "images/false.png"
SCORE_IMG = "images/score.png"

#---------- API Parameters -----------#

# Parameters for the Open Trivia Database API request
# "amount": Number of questions to fetch
# "type": "boolean" ensures only True/False questions are retrieved
PARAMETERS = {
    "amount": 25,
    "type": "boolean"
}
