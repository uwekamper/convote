import datetime
import uuid
from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


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

templates = Jinja2Templates(directory=Path(__file__).parent / "templates")


@app.get("/", response_class=HTMLResponse)
async def rooot(request: Request):
    return templates.TemplateResponse(
        request=request, name="index.html", context={"DEBUG": True}
    )


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
    
@app.get("/questions/")
async def questions():
    all_questions = sorted(VOTES, key=lambda x: x.get('created'))
    return all_questions