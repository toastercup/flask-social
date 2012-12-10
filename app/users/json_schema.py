import re

register_schema = {"type": "object",
                   "properties": {
                       "email": {"type": "string", "pattern": re.compile(r"(?:^|\s)[-a-z0-9_.]+@(?:[-a-z0-9]+\.)+[a-z]{2,6}(?:\s|$)",re.IGNORECASE)},
                       "password": {"type": "string", "minLength": 5},
                       "name": {"type": "string"}
                   }
}