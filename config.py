import re

SETTINGS = {

    "ACCOUNTANT": "Darrel", 
    "MONTH" : "nov"

}


REGEX = {

    "FUNDING_PATTERN": (re.compile("fund([\w]+)?|IPAC")),
    "FUNDING_STRING": "fund([\w]+)?|IPAC",
    "CANCEL_PATTERN": (re.compile("cancel([\w]+)?")),
    "CANCEL_STRING": "cancel([\w]+)?",


}