# Update definitions test cases
import conftest


# TC 20: /scans/update, description contains standard text -> get 200 { message: "Definitions updated successfully" }
def test_update_definition_request_returns_proper_message(test_data):
    response = test_data.api_requests.update_definitions()

    assert response.status_code == 200
    assert response.json() == {"status": "Definitions updated successfully"}


# TC 21: /scan/history, /scans/update, then /scan/history -> scan history not affected by definitions update

def test_scan_history_not_affected_after_definitions_update(test_data):
    initial_scan_history = test_data.api_requests.get_scan_history()

    test_data.api_requests.update_definitions()

    final_scan_history = test_data.api_requests.get_scan_history()

    conftest.assert_no_change_in_scan_history(initial_scan_history, final_scan_history)


# TC 22: /scans/update, then scan clean file -> verify scan functionality remains the same after updating definitions
def test_scan_functionality_sanity_check_after_definitions_update(test_data):
    test_data.api_requests.update_definitions()

    file_name = "test_file.exe"
    file_content = "Clean content"

    response = test_data.api_requests.scan_file(file_name, file_content)

    assert response.status_code == 200
    assert response.json() == {"status": "clean"}



