import re

SETTINGS = {

    "ACCOUNTANT": "Steph", 
    "MONTH" : "mar"

}


REGEX = {
    "FUNDING_PATTERN": (re.compile("fund([\w]+)?|IPAC")),
    "FUNDING_STRING": "fund([\w]+)?|IPAC",
    "CANCEL_PATTERN": (re.compile("cancel([\w]+)?")),
    "CANCEL_STRING": "cancel([\w]+)?",
    "COMPLETE_PATTERN": (re.compile("(?<=Not)[\s\w]+complet[a-zA-Z]+ |new|#N\/A")),
    "COMPLETE_STRING": "(?<=Not)[\s\w]+complet[a-zA-Z]+ |new|#N\/A"
}