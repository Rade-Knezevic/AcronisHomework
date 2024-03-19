import requests

class APIRequests:
    def __init__(self, base_url):
        self.base_url = base_url

    def scan_file(self, file_name, file_content):
        url = f"{self.base_url}/scans/scan"
        data = {"name": file_name, "content": file_content}
        response = requests.post(url, json=data)
        return response

    def update_definitions(self):
        url = f"{self.base_url}/scans/update"
        response = requests.put(url)
        return response

    def get_scan_history(self):
        url = f"{self.base_url}/scans/history"
        response = requests.get(url)
        return response

    def retrieve_from_quarantine(self, file_id):
        url = f"{self.base_url}/quarantine/quarantine?file_id={file_id}"
        response = requests.get(url)
        return response

    def delete_from_quarantine(self, file_id):
        url = f"{self.base_url}/quarantine/delete"
        response = requests.delete(url, json={"fileId": file_id})
        return response
