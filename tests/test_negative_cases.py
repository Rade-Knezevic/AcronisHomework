# Negative Test Cases

# TC 2: /types, .zip file, empty name -> get 400, { status: invalid file}
def test_upload_empty_file_name(test_data):
    file_name = ".zip"
    file_content = "This is a clean file with empty name."
    response = test_data.api_requests.upload_file(file_name, file_content)
    assert response.status_code == 400
    assert response.json() == {"status": "invalid file"}

# TC3: /types, non-existing file type, (e.g. some_file.qwertyyyyy) -> get 400
def test_upload_invalid_file_type(test_data):
    file_name = "some_file.qwertyyyyy"
    file_content = "This is a file with invalid extension."
    response = test_data.api_requests.upload_file(file_name, file_content)
    assert response.status_code == 400
    assert response.json() == {"status": "invalid file"}

# TC 8: /types, file name contains special chars -> get 400 {status: forbidden}
def test_upload_special_chars_in_name(test_data):
    file_name = "!@#$%^^&*(){}\".exe"
    file_content = "This is a file with special chars within name."
    response = test_data.api_requests.upload_file(file_name, file_content)
    assert response.status_code == 400
    assert response.json() == {"status": "forbidden"}

# TC 12: /types, file name contains command injection -> get 400 {status: "Command injection"}
def test_upload_command_injection_within_name(test_data):
    file_name = "ls||id; ls ||id; ls|| id; ls || id"
    file_content = "This is a file that attempts command injection"
    response = test_data.api_requests.upload_file(file_name, file_content)
    assert response.status_code == 400
    assert response.json() == {"status": "forbidden"}

# TC 15: /scans/scan, .bat file, infected file -> get 404 { status: "infected", details: "Virus found" }
def test_scan_infected_file(test_data):
    file_name = "infected-file.bat"
    file_content = "Here should be a malware!!!"
    response = test_data.api_requests.scan_file(file_name, file_content)
    assert response.status_code == 400
    assert response.json() == {"status": "infected", "details": "Virus found"}

