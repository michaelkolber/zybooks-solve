"""A collection of errors tailored to the zyBooks solver."""

from typing import NoReturn

import requests

import solver


class SolverError(Exception):
    """A common base class for all errors for the zyBooks solver."""
    pass


class NoBuildkeyError(SolverError):
    pass


class SolveFailureError(SolverError):
    def __init__(self, subactivity: solver.zyBookSubActivity, res: requests.Response) -> NoReturn:
        activity = subactivity.activity
        section = activity.section
        chapter = section.chapter
        book = chapter.zyBook
        
        super().__init__(f'Error solving {book.title}: Chapter {chapter.number}: Section {section.number}: Activity {activity.number}: Part {subactivity.number}.\nResponse:\n{res.json()}')