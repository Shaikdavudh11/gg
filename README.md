Windows PowerShell
Copyright (C) Microsoft Corporation. All rights reserved.

Try the new cross-platform PowerShell https://aka.ms/pscore6

(.venv) PS C:\Users\Welcome\PycharmProjects\GamutGurus> git status
(.venv) PS C:\Users\Welcome\PycharmProjects\GamutGurus> git init
Initialized empty Git repository in C:/Users/Welcome/PycharmProjects/GamutGurus/.git/
origin  https://github.com/Shaikdavudh11/gg.git (fetch)
origin  https://github.com/Shaikdavudh11/gg.git (push)
error: src refspec main does not match any
error: failed to push some refs to 'https://github.com/Shaikdavudh11/gg.git'
(.venv) PS C:\Users\Welcome\PycharmProjects\GamutGurus> git branch -M main
(.venv) PS C:\Users\Welcome\PycharmProjects\GamutGurus> git push -u origin main
error: src refspec main does not match any
error: failed to push some refs to 'https://github.com/Shaikdavudh11/gg.git'
(.venv) PS C:\Users\Welcome\PycharmProjects\GamutGurus> git status
On branch main

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        .idea/
        __pycache__/
        dashboard and contact.py
        devops course
        devops course.py
        gamut..txt
        gamutgurus.py

nothing added to commit but untracked files present (use "git add" to track)
(.venv) PS C:\Users\Welcome\PycharmProjects\GamutGurus> git add .
warning: in the working copy of '.idea/inspectionProfiles/profiles_settings.xml', LF will be replaced by CRLF the next time Git touches it
(.venv) PS C:\Users\Welcome\PycharmProjects\GamutGurus> git config user.name "Davudh"
(.venv) PS C:\Users\Welcome\PycharmProjects\GamutGurus> git config user.email "shaikdavudh973@gmail.com"
(.venv) PS C:\Users\Welcome\PycharmProjects\GamutGurus> git commit -m "Added Test cases for GG website"
 13 files changed, 292 insertions(+)
 create mode 100644 .idea/.gitignore
 create mode 100644 .idea/inspectionProfiles/profiles_settings.xml
 create mode 100644 .idea/misc.xml
 create mode 100644 .idea/modules.xml
 create mode 100644 .idea/vcs.xml
 create mode 100644 __pycache__/devops course.cpython-312-pytest-8.3.2.pyc
 create mode 100644 __pycache__/gamutgurus.cpython-312-pytest-8.3.2.pyc
 create mode 100644 dashboard and contact.py
 create mode 100644 devops course
 create mode 100644 devops course.py
 create mode 100644 gamut..txt
 create mode 100644 gamutgurus.py
(.venv) PS C:\Users\Welcome\PycharmProjects\GamutGurus> git status
On branch main
nothing to commit, working tree clean
(.venv) PS C:\Users\Welcome\PycharmProjects\GamutGurus> git push -u origin main
Enumerating objects: 18, done.
Counting objects: 100% (18/18), done.
Delta compression using up to 4 threads
Compressing objects: 100% (16/16), done.
Writing objects: 100% (18/18), 6.14 KiB | 483.00 KiB/s, done.
Total 18 (delta 3), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (3/3), done.
To https://github.com/Shaikdavudh11/gg.git
 * [new branch]      main -> main
branch 'main' set up to track 'origin/main'.
(.venv) PS C:\Users\Welcome\PycharmProjects\GamutGurus>   
