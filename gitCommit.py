try:
    from git import Repo

    PATH_OF_GIT_REPO = r'./.git'  # make sure .git folder is properly configured
    COMMIT_MESSAGE = input("Please enther the commit message:\n")

    def git_push():
        try:
            repo = Repo(PATH_OF_GIT_REPO)
            repo.git.add(update=True)
            repo.index.commit(COMMIT_MESSAGE)
            origin = repo.remote(name='origin')
            origin.push()
        except:
            print('Some error occured while pushing the code')    

    git_push()
    
except Exception as e:
    import time
    print(e)
    time.sleep(10)