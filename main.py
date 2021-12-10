import json

from src.github import GithubClient
from src.googleSheets import GoogleSheetClient
from src.moodle import MoodleClient
from src.helpers import addGradeLabelToPR, getDictPRGradeInfo

mainConfig = json.load(open('./configs/main.json'))
runConfig = json.load(open('./configs/run.json'))

# git - ok
ghclient = GithubClient(mainConfig["github"]["credentials"]["accessToken"])


dictGitPR = ghclient.getDictGitPR(
    runConfig["github"]["repo"],
    runConfig["github"]["prRegex"])

# google sheets - ok
gsclient = GoogleSheetClient(mainConfig["googleSheet"]["id"])
dictFioGit = gsclient.getDictFioGit(
    mainConfig["googleSheet"]["headers"]["fio"], mainConfig["googleSheet"]["headers"]["github"])

# moodle - ok
mdclient = MoodleClient(
    baseUrl=mainConfig["moodle"]["baseUrl"],
    token=mainConfig["moodle"]["credentials"]["token"])

dictFioGradeInfo = mdclient.getDictFioGradeInfo(
    runConfig["moodle"]["courseId"], runConfig["moodle"]["quizId"])


# get link pr - grade
dictPRGradeInfo = getDictPRGradeInfo(dictFioGradeInfo, dictFioGit, dictGitPR)

# add grade labels to prs
addGradeLabelToPR(dictPRGradeInfo, mainConfig["github"]["label"])





# change grade.raw (all)
# def mockGrade(num):
#     print(f"start _{num}_")
#     dictFioGradeInfo = mdclient._getDictFioGradeInfo(
#         runConfig["moodle"]["courseId"], runConfig["moodle"]["quizId"], num)
#     dictPRGradeInfo = getDictPRGradeInfo(
#         dictFioGradeInfo, dictFioGit, dictGitPR)
#     addGradeLabelToPR(dictPRGradeInfo, mainConfig["github"]["label"])
#     print(f"end _{num}_")
# mockGrade(1)

print("all end")
