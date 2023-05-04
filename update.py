#!/usr/bin/env python

import os
from urllib import parse

HEADER="""# 
## rheefine's Baekjoon & Programmers Algorithm Problem Solutions
\t - The algorithm solution history in this repository is automatically updated upon uploading
"""

def main():
    content = ""
    content += HEADER
    
    directories = [];
    baekjoon = [];
    programmers = [];
    ko_to_eng = {"백준" : "Baekjoon",
                "프로그래머스" : "Programmers"}
    
    for root, dirs, files in os.walk("."):
        dirs.sort()
        if root == '.':
            for dir in ('.git', '.github'):
                try:
                    dirs.remove(dir)
                except ValueError:
                    pass
            continue

        category = os.path.basename(root)
        
        if category == 'images':
            continue
        
        directory = os.path.basename(os.path.dirname(root))
        
        if directory == '.':
            continue
            
        if directory not in directories:
            if directory in ["백준", "프로그래머스"]:
                content += "### 📝 {}\n".format(ko_to_eng[directory])
                content += '| # | Problem | Solution | Difficulty |\n'
                content += "| :---------: | :---------: | :---------: | --------- |\n"
            directories.append(directory)
        
        for file in files:
            if category not in baekjoon + programmers:
                numB = len(baekjoon) + 1
                numP = len(programmers) + 1
                problem = category.split('. ')[-1]
                difficulty = os.path.dirname(root).split('/')[-1]
                if difficulty in ['Bronze', 'Silver', 'Gold', 'Platinum']:
                    baekjoon.append(category)
                    if difficulty == 'Bronze':
                        content += "|{}|[{}]({})|[Link]({})|{}|\n".format(numB, problem, parse.quote(os.path.join(root)), parse.quote(os.path.join(root, file)), '🟤 ' + difficulty)
                    if difficulty == 'Silver':
                        content += "|{}|[{}]({})|[Link]({})|{}|\n".format(numB, problem, parse.quote(os.path.join(root)), parse.quote(os.path.join(root, file)), '⚪ ' + difficulty)
                    if difficulty == 'Gold':
                        content += "|{}|[{}]({})|[Link]({})|{}|\n".format(numB, problem, parse.quote(os.path.join(root)), parse.quote(os.path.join(root, file)), '🟡 ' + difficulty)
                    if difficulty == 'Platinum':
                        content += "|{}|[{}]({})|[Link]({})|{}|\n".format(numB, problem, parse.quote(os.path.join(root)), parse.quote(os.path.join(root, file)), '🔘 ' + difficulty)
                if difficulty in ['lv1', 'lv2', 'lv3', 'lv4']:
                    programmers.append(category)
                    if difficulty == 'lv1':
                        content += "|{}|[{}]({})|[Link]({})|{}|\n".format(numB, problem, parse.quote(os.path.join(root)), parse.quote(os.path.join(root, file)), '★⚝⚝⚝⚝')
                    if difficulty == 'lv2':
                        content += "|{}|[{}]({})|[Link]({})|{}|\n".format(numB, problem, parse.quote(os.path.join(root)), parse.quote(os.path.join(root, file)), '★★⚝⚝⚝')
                    if difficulty == 'lv3':
                        content += "|{}|[{}]({})|[Link]({})|{}|\n".format(numB, problem, parse.quote(os.path.join(root)), parse.quote(os.path.join(root, file)), '★★★⚝⚝')
                    if difficulty == 'lv4':
                        content += "|{}|[{}]({})|[Link]({})|{}|\n".format(numB, problem, parse.quote(os.path.join(root)), parse.quote(os.path.join(root, file)), '★★★★⚝')
                    
    with open("README.md", "w") as fd:
        fd.write(content)
        
if __name__ == "__main__":
    main()
