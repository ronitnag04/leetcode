"""
0. Make sure to complete S2_extract_distribution_values step first
1. Make sure there are no unpushed commits before proceding
2. Replace root_path and sync_work_path variables below
3. a. Run script
   b. Some filenames are not formatted correctly, so user input may be necessary
      Reference file directory while giving user input to ensure proper spelling
   c. If running multiple times, update known_mismatches dictionary to avoid repeated input
4. Push Commits with Y or enter n to review changes before pushing
"""

import os
import shutil
import pandas as pd
import numpy as np
from git import Repo

root_path = ""  # Replace with your working directory (e.g 'C:/Users/<YOUR_USER_NAME>/OneDrive/Desktop/leetcode/' )
sync_work_path = '' # default sync-problems/

synced_problems_path =  root_path + 'problems/'
destination_path = root_path

df_migrate_values = pd.read_csv(root_path + sync_work_path + 'sync_values_distributions.csv')

repo = Repo(destination_path)
all_commits = list(repo.iter_commits('main'))
sync_commits = [c for c in all_commits if 'Sync LeetCode submission' in c.message]
sync_commit_by_name = {c.message.split(' - ')[1].split('(')[0][:-1].lower().replace(' ', '_') :c for c in sync_commits}

# Add known mismatches here 
known_mismatches = {} # e.g. 'non_decreasing_array': 'non-decreasing_array', 'implement_trie_prefix_tree': 'implement_trie',                 

commit_column = []

for i, row in df_migrate_values.iterrows():
    old_name = row['Old Filename']
    if old_name in known_mismatches:
        old_name = known_mismatches[old_name]

    while old_name not in sync_commit_by_name:
        # Display all commit keys incase user input needed
        abc_names = list(sorted(sync_commit_by_name.keys()))
        for name in abc_names:
            print('- ' + name)
        old_name = input(old_name + ' not found. Input correct commit name: ')

    commit_column.append(sync_commit_by_name[old_name])

df_migrate_values['commit'] = commit_column

# Make commits
suggest_manual_commit = []
index = repo.index

def migrateCommitFolder(migrate_row):
    source = migrate_row['Old Filename']
    if source in known_mismatches:
        source = known_mismatches[source]

    while not os.path.exists(synced_problems_path + source):
        print('Synced Problem Source not Found: ', synced_problems_path + source)
        print('Please Manually enter synced folder path')
        source = input(synced_problems_path)
    
    dest = destination_path + migrate_row['New Filename']
    proceed = 'Y'
    if os.path.exists(dest):
        print(f'Problem has already been synced to: {dest}')
        proceed = ''
        while proceed != 'Y' and proceed != 'n':
            proceed = input('Override Existing Folder & Commit?: [Y/n]')

    if proceed == 'Y':
        try:
            shutil.copytree(synced_problems_path + source, dest)
            print(f'Moved {synced_problems_path + source} to {dest}')
        except:
            raise Exception(f'Invalid path: {synced_problems_path + source} or {dest}')

        author = migrate_row['commit'].author
        committer = migrate_row['commit'].committer
        time = migrate_row['Runtime']
        timescore = migrate_row['Best Runtime Percentage']
        memory = migrate_row['Memory']
        memoryscore = migrate_row['Best Memory Percentage']
        """
        If time sync is also needed, establish authored/committed date here
        and pass as parameters to index.commit call. See GitPython Docs for more info:
        https://gitpython.readthedocs.io/en/stable/reference.html#module-git.objects.commit 
        """

        if timescore is np.nan or memoryscore is np.nan:
            suggest_manual_commit.append(migrate_row['Old Filename'])
        if timescore is np.nan:
            timescore = 'N/A'
        if memoryscore is np.nan:
            memoryscore = 'N/A'

        commit_message = f'Time: {time} ({timescore}), Space: {memory} ({memoryscore}) - Migrate Sync'
        index.add([migrate_row['New Filename']])
        index.commit(message=commit_message, author=author, committer=committer)


for i, row in df_migrate_values.iterrows():
    migrateCommitFolder(row)


origin = repo.remote(name='origin')

should_push = ''
print()
while should_push != 'Y' and should_push != 'n':
    should_push = input('Push changes?: [Y/n]')

if should_push == 'Y':
    origin.push()
else:
    print('Changes not pushed')

print()
print('The distributions for the following questions could not be extracted')
print('Please manually resubmit these questions to obtain current distribution info:')
for suggest in suggest_manual_commit:
    print(f'- {suggest}')