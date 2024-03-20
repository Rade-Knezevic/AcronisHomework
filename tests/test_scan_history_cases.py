import conftest

# TC 16: /scan/history, then scan clean file, /scan/history again -> verify history updated with new entry: clean file
def test_scan_history_updates_after_scanning_clean_file(test_data):
    initial_scan_history = test_data.api_requests.get_scan_history()

    file_name = "clean_file.java"
    file_content = "test file"
    expected_result = "clean"
    test_data.api_requests.scan_file(file_name, file_content)

    final_scan_history = test_data.api_requests.get_scan_history()

    conftest.assert_new_scan_history_entry(initial_scan_history, final_scan_history, expected_result)


# TC 17: /scan/history, then scan infected file, /scan/history again -> verify history updated with new entry: infected file

def test_scan_history_updates_after_scanning_infected_file(test_data):
    initial_scan_history = test_data.api_requests.get_scan_history()

    file_name = "infected_file.xlsx"
    file_content = "test file that contains a virus"
    expected_result = "infected"
    test_data.api_requests.scan_file(file_name, file_content)

    final_scan_history = test_data.api_requests.get_scan_history()

    conftest.assert_new_scan_history_entry(initial_scan_history, final_scan_history, expected_result)