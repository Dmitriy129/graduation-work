import requests as rs
from urllib.parse import unquote


class MoodleClient:

    def __init__(self, baseUrl, token):
        self.baseUrl = baseUrl
        self.token = token

    def getGradesByCourseId(self, courseid):
        url = f'{self.baseUrl}/webservice/rest/server.php'
        params = {
            "courseid": courseid,
            "wstoken": self.token,
            "wsfunction": "gradereport_user_get_grade_items",
            "moodlewsrestformat": "json",
        }
        res = rs.get(url, params=params).json()
        return res["usergrades"]

    def getUsersByIds(self,  ids):
        url = f'{self.baseUrl}/webservice/rest/server.php'
        params = {
            "values[]": ids,
            "field": "id",
            "wstoken": self.token,
            "wsfunction": "core_user_get_users_by_field",
            "moodlewsrestformat": "json",
        }
        res = rs.get(url, params=params).json()
        return res

    def getDictFioGradeInfo(self, courseid, quizId):
        courseGrades = self.getGradesByCourseId(courseid)
        dictFioGradeInfo = {}
        for user in courseGrades:
            grade = next(
                (x for x in user["gradeitems"] if x["iteminstance"] == quizId), None)
            if(grade and grade["graderaw"] != None):
                dictFioGradeInfo[unquote(user["userfullname"])] = {
                    "id": grade["id"],
                    "raw": grade["graderaw"],
                    "min": grade["grademin"],
                    "max": grade["grademax"],
                    "userId": user["userid"],
                    "submittedAt": grade["gradedatesubmitted"],
                    "gradedAt": grade["gradedategraded"],
                }
        return dictFioGradeInfo

    # def _getDictFioGradeInfo(self, courseid, quizId, raw):
    #     dictFioGradeInfo = self.getDictFioGradeInfo(courseid, quizId)
    #     for fio in dictFioGradeInfo:
    #         dictFioGradeInfo[fio]["raw"] = raw
    #     return dictFioGradeInfo

