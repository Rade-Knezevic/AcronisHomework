


    # ID 26: /quarantine/quarantine, specify an existing fileId and run -> get 200
def test_retrieve_quarantined_file(test_data):
    file_id = "234"
    # Precondition: make sure infected file is uploaded
    # I do not have a clear structure how to get a file id, but if this is possible,
    # id should be retrived from newly uploaded file and provided to test further for checks

    response = test_data.api_requests.retrieve_from_quarantine(file_id)

    assert response.code == 200
    assert response.json() == { "fileId": f"{file_id}", "name": "quarantined_file.txt" }


    # ID 27: /quarantine/quarantine, try to retrieve already retrieved file -> get 200, then 404
def test_retrieve_previously_retrieved_file(test_data):
    file_id = "458"
    # Precondition: make sure infected file is uploaded
    # I do not have a clear structure how to get a file id, but if this is possible,
    # id should be retrived from newly uploaded file and provided to test further for checks

    response = test_data.api_requests.retrieve_from_quarantine(file_id)

    assert response.code == 200
    assert response.json() == {"fileId": f"{file_id}", "name": "quarantined_file.txt"}

    response = test_data.api_requests.retrieve_from_quarantine(file_id)

    assert response.code == 404
    assert response.json() == {f"file with id: {file_id} not found"}

    # ID 28: /quarantine/delete, specify an existing file -> get 200 { message: "File deleted from quarantine" }
def test_delete_quarantined_file(test_data):
    file_id = "704"

    # Precondition: make sure infected file is uploaded
    # I do not have a clear structure how to get a file id, but if this is possible,
    # id should be retrived from newly uploaded file and provided to test further for checks

    response = test_data.api_requests.delete_from_quarantine(file_id)

    assert response.code == 200
    assert response.json() == {"message": "File deleted from quarantine"}

    # ID 29: /quarantine/delete, specify a non-existing file -> get 404 { error: "File not found in quarantine" }
def test_delete_non_quarantined_file(test_data):
    file_id = "9707"

    # Precondition: make sure there is no file with  such id
    response_precondition = test_data.api_requests.delete_from_quarantine(file_id)

    response = test_data.api_requests.delete_from_quarantine(file_id)

    assert response.code == 404
    assert response.json() == {"message": "File not found in quarantine"}

