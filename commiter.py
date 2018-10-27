import base64
from github import Github, InputGitTreeElement
from os import getcwd
from auth import auth

cred = auth()

def commiter(dirPath):
	g = Github(
		cred['user'],
		cred['passw']
	)
	repo = g.get_repo('heIlo-world/hello-world')

	fileList = ['{}/text.txt'.format(dirPath),]
	fileNames = ['text.txt',]
	commitMessage = 'first commit'
	masterRef = repo.get_git_ref('heads/master')
	masterSha = masterRef.object.sha
	baseTree = repo.get_git_tree(masterSha)
	elementList = list()

	for idx, entry in enumerate(fileList):
		with open(entry) as inputFile:
			data = inputFile.read()

		element = InputGitTreeElement(fileNames[idx], '100644', 'blob', data)
		elementList.append(element)


	tree = repo.create_git_tree(elementList, baseTree)
	parent = repo.get_git_commit(masterSha)
	commit = repo.create_git_commit(commitMessage, tree, [parent])
	masterRef.edit(commit.sha)


cwd = getcwd()
commiter(cwd)