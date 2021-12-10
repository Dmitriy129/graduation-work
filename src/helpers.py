def getDictPRGradeInfo(dictFioGradeInfo, dictFioGit, dictGitPR):
    dicPrGradeInfo = {}
    for fioLong in dictFioGit:
        if not fioLong:
            continue
        git = dictFioGit[fioLong]
        arrFioLong = fioLong.split(" ")
        fioShort = " ".join([arrFioLong[1], arrFioLong[0]])
        if fioShort in dictFioGradeInfo and git in dictGitPR:
            grade = dictFioGradeInfo[fioShort]
            pr = dictGitPR[git]
            dicPrGradeInfo[pr] = grade
    return dicPrGradeInfo


def genLabelByGrade(raw, min, max, labelConfig):
    # percent = raw/max*100
    percentConfig = labelConfig["config"]
    defaultTemplate = labelConfig["defaultTemplate"]
    defaultColor = labelConfig["defaultColor"]

    percent = (raw-min)/(max-min)*100
    for [[pMin, pMax], conf] in percentConfig:
        if percent >= pMin and percent < pMax:
            name = f'{defaultTemplate} {conf["template"].format(raw=raw, min=min, max=max)}'
            color = conf["color"]
            description = None
            comment = None
            if "description" in conf:
                description = conf["description"].format(
                    raw=raw, min=min, max=max)
            if "comment" in conf:
                comment = conf["comment"].format(raw=raw, min=min, max=max)
            return name, color, description, comment
    return f'{defaultTemplate}: error', defaultColor, None, None


# add grade labels to prs
def addGradeLabelToPR(dictPRGradeInfo, labelConfig):
    for pr in dictPRGradeInfo:
        grade = dictPRGradeInfo[pr]
        name, color, description, comment = genLabelByGrade(
            raw=grade["raw"],
            min=grade["min"],
            max=grade["max"],
            labelConfig=labelConfig)

    oldLabel = next(
        (l for l in pr.labels
         if labelConfig["defaultTemplate"] in l.name),
        None)
    if oldLabel:
        oldLabel.edit(name=name,
                      color=color,
                      description=description)
    else:
        pr.add_to_labels(name)
        newLabel = next((l for l in pr.labels if l.name == name), None)
        if newLabel:
            newLabel.edit(name=newLabel.name,
                          color=color,
                          description=description)
    if comment:
        pr.create_issue_comment(comment)
