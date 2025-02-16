import datetime
import uuid

from fastapi import FastAPI

app = FastAPI()

VOTES = [
    {
        "id": uuid.uuid4(),
        "created": datetime.datetime.now(),
        "is_active": True,
        "q": "Will the armadillo make it across the road?",
        "opts": {
            "a": "I pray that he does.",
            "b": "Yes, he's moving fast.",
            "c": "I don't bet on roadkill.",
            "d": "He doesn't stand a chance",
        },
        "resps": [],
    }
]


@app.get("/")
async def root():
    return {"helo": "HALL 1"}


@app.get("/current/")
async def current():
    active = sorted([el for el in VOTES if el.get('is_active') == True], key=lambda x: x.get('created'))
    if len(active) > 0:
        vote = active[0]
        return {
            'q': vote['q'],
            'opts': vote.get('opts'),
        }
    else:
        return {
            'q': None,
            'opts': None,
        }