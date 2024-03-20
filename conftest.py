import pytest
from api.testPreparation import TestData

@pytest.fixture
def test_data():
    return TestData()


def assert_new_scan_history_entry(initial_history, final_history, expected_status):
    """
    Verifies that a new entry is added to the scan history and checks its status.

    :param initial_history: The scan history before a new scan.
    :param final_history: The scan history after a new scan.
    :param expected_status: The expected status of the new scan entry ("clean" or "infected").
    """
    new_entries = [entry for entry in final_history if entry not in initial_history]
    assert len(new_entries) == 1, "Expected exactly one new entry in the scan history."
    assert new_entries[0]["status"] == expected_status, f"Expected the new scan entry status to be '{expected_status}'."

def assert_no_change_in_scan_history(initial_history, final_history):
    """
    Verifies that a new entry is added to the scan history and checks its status.

    :param initial_history: The scan history before an event.
    :param final_history: The scan history after an event.
    """
    new_entries = [entry for entry in final_history if entry not in initial_history]
    assert len(new_entries) == 0, "Expected no new entries in the scan history."