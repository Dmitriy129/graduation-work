import requests as rs


class GoogleSheetClient:

    def __init__(self, sheetId):
        self.sheetId = sheetId

    def query(self):
        url = f'https://docs.google.com/spreadsheets/d/{self.sheetId}/export?format=csv&id={self.sheetId}&gid=0'
        res = rs.get(url)

        return res.content.decode("utf-8")

    def getDictFromGoogleSheets(self):
        csvTable = self.query()
        tableStrRows = csvTable.split("\r\n")
        arrTableHeader = tableStrRows[0].split(',')
        dictTable = [{
            header: valuesStr.split(",")[idx]
            for idx, header in enumerate(arrTableHeader)
        } for valuesStr in tableStrRows[1:]]

        return dictTable

    def getDictFioGit(self,  fioHeader, gitHeader):
        csvTable = self.query()
        tableStrRows = csvTable.split("\r\n")
        arrTableHeader = tableStrRows[0].split(',')
        dict = {
            valuesStr.split(",")[arrTableHeader.index(fioHeader)]:
            valuesStr.split(",")[arrTableHeader.index(gitHeader)]
            for valuesStr in tableStrRows[1:]
        }
        return dict
