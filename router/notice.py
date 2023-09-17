# pylint: disable=E0611,E0401

from fastapi import APIRouter

router = APIRouter(prefix="/notice")


class Dummy(object):
    def __init__(self, body_cntt, brch_id):
        self.body_cntt = body_cntt
        self.brch_id = brch_id


def replace_text(t):
    return t.replace("'", "\"").replace("\n", "")

