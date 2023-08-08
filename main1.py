from os import system

system("git init")
system("git add .")
system("git commit -m 'all'")
system("git remote add origin git@github.com:Qainarr/main.git")
system("git push -u origin master")