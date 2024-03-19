# Negative Test Cases

# TC 2: /types, .zip file, empty name -> get 400, { status: invalid file}
def test_upload_empty_file_name(test_data):
    file_name = ".zip"
    file_content = "This is a clean file with empty name."
    response = test_data.api_requests.scan_file(file_name, file_content)
    assert response.status_code == 400
    assert response.json() == {"status": "invalid file"}

# TC3: /types, non-existing file type, (e.g. some_file.qwertyyyyy) -> get 400
def test_upload_invalid_file_type(test_data):
    file_name = "some_file.qwertyyyyy"
    file_content = "This is a file with invalid extension."
    response = test_data.api_requests.scan_file(file_name, file_content)
    assert response.status_code == 400
    assert response.json() == {"status": "invalid file"}

