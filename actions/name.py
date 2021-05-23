import json
from st2common.runners.base_action import Action


__all__ = ["Name"]


class Name(Action):

    def __init__(self, config) -> None:
        super(Name, self).__init__(config)

    def run(self):
        return {"name": "Printing Name..."}
