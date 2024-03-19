# Positive Test Cases

# TC 1: /types, .txt file, proper name -> get 200, { status: clean}
# Steps: Upload valid file
# Expected: Status code = 200
def test_upload_clean_file(test_data):
    file_name = "cleanFile.exe"
    file_content = "This is a clean file."
    response = test_data.api_requests.scan_file(file_name, file_content)
    assert response.status_code == 200
    assert response.json() == {"status": "clean"}


