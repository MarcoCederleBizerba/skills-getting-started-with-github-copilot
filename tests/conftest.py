from copy import deepcopy

import pytest

from src import app as app_module

_ORIGINAL_ACTIVITIES = deepcopy(app_module.activities)


@pytest.fixture(autouse=True)
def reset_activities_state():
    # Ensure each test starts with the initial activities state.
    app_module.activities.clear()
    app_module.activities.update(deepcopy(_ORIGINAL_ACTIVITIES))
    yield
