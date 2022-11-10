from git import Repo
import time
try:

    PATH_OF_GIT_REPO = r'./.git'  # make sure .git folder is properly configured
    COMMIT_MESSAGE = input("Please enther the commit message:\n")

    def git_push():
        try:
            repo = Repo(PATH_OF_GIT_REPO)
    #         repo.git.add(update=True)
            repo.git.add(all=True)
            repo.index.commit(COMMIT_MESSAGE)
            origin = repo.remote(name='origin')
            origin.push()
        except Exception as e:
            print('Some error occured while pushing the code:')
            print(e)

    git_push()
    print("Successed.")
    time.sleep(3)
    
    
except Exception as e:

    print(e)
    time.sleep(10)