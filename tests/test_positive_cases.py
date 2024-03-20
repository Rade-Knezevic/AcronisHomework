# Positive Test Cases

# TC 1: /types, .txt file, proper name -> get 200, { status: upload successful}
def test_upload_clean_file(test_data):
    file_name = "cleanFile.exe"
    file_content = "This is a clean file."
    response = test_data.api_requests.scan_file(file_name, file_content)
    assert response.status_code == 200
    assert response.json() == {"status": "upload successful"}

# TC 13: /scans/scan, .dll file, clean file -> get 200 { status: "clean" }
def test_scan_clean_file(test_data):
    file_name = "anotherCleanFile.dll"
    file_content = "This is a clean dll file."
    response = test_data.api_requests.scan_file(file_name, file_content)
    assert response.status_code == 200
    assert response.json() == {"status": "clean"}


