import json
from st2common.runners.base_action import Action


__all__ = ["Desc"]


class Desc(Action):

    def __init__(self, config) -> None:
        super(Desc, self).__init__(config)

    def run(self):
        return json.dumps({"desc": "Printing Desc..."})
