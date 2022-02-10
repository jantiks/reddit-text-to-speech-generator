from Reddit import RedditService
from speechToVoiceService import SpeechToVoiceService
from screenshotService import ScreenshotService
import os

screenshotService = None
speechToVoiceService = None

def mkdirIfExists(path):
    if os.path.isdir(path):
        print("path {} exists".format(path))
        return
    else:
        os.mkdir(path)  # new directory


def makeVideoFrom(submission):
    folderPath = "./videos/new/askReddit_{}".format(submission.id)
    mkdirIfExists(folderPath)
    makePostVideoAt(folderPath + "/post", submission)
    makeCommentsVideosAt(folderPath + "/comments", submission)


def makePostVideoAt(path, submission):
    mkdirIfExists(path)

    screenshotService.screenshotPostAt(path+"/screenshot", submission)
    speechToVoiceService.makeVoiceAt(path+"/speech", submission.title)
    clipTogether(path)


def makeCommentsVideosAt(path, submission):
    mkdirIfExists(path)
    commentPerPostCount = 0
    comments = submission.comments.list()
    print("len is")
    print(len(comments))
    comments = submission.comments.list()
    for comment in comments:
        if commentPerPostCount >= 10:
            break

        if comment.score > 500:
            print("count is {}".format(commentPerPostCount))
            commentPerPostCount += 1
            screenshotService.screenshotCommentAt(path+"/screenshot{}".format(commentPerPostCount), comment)
            # speechToVoiceService.makeVoiceAt(path+"/speech{}".format(commentPerPostCount), comment)


def clipTogether(path):
    pass

if __name__ == '__main__':
    RedditService.startSession()
    submissions = RedditService.getHotSubmissions()
    screenshotService = ScreenshotService()
    speechToVoiceService = SpeechToVoiceService()

    for submission in submissions:
        if submission.num_comments > 2000 and submission.score > 5000:
            print("saving submisiion")
            makeVideoFrom(submission)
    # speechToVoiceService.makeVoiceAt("./videos/new/askReddit_{}".format("skzwrs"), "What is a socially unacceptable thing that you dont like or hate")
    # screenshotService.screenshotPostAt("./videos/new/askReddit_{}".format("skzwrs"), "asd")