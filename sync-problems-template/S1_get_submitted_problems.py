"""
1. Go to https://leetcode.com/api/problems/all/ and copy content into file called submissions.json
2. Prepare get_submissions.py file with proper request cookies, headers, and json_data 
3. a. Run https://github.com/joshcai/leetcode-sync workflow and have problems folder in root directory. 
   b. Note that the CSRFTOKEN and LEETCODE_SESSION cookie values were found in step 2
   c. Template of sync_leetcode.yml is included, but make sure this yml file is not copied directly by added 
      to the .github folder via Github -> Actions -> Creat New Workflow
4. Replace root_path and sync_work_path variables below
5. Run this script and ensure sync_values.csv is in the sync work path folder
6. Move on to S2_extract_distribution_values.py
"""

import pandas as pd
from get_submissions import getSubmissionDetails


root_path = "" # Replace with your working directory (e.g 'C:/Users/<YOUR_USER_NAME>/OneDrive/Desktop/leetcode/' )
sync_work_path = '' # default sync-problems/

submissions_path = root_path + sync_work_path + 'submissions.json'

question_list = pd.read_json(submissions_path)

migrate_values = []
for question in question_list['stat_status_pairs']:
    if question["status"] == "ac":
        slug = question['stat']['question__title_slug']
        id = question['stat']['frontend_question_id']
        num = str(id)
        new_filename = '0'*(4-len(num)) + num + '-' + slug
        old_filename = slug.replace('-', '_')
        details = getSubmissionDetails(slug)
        values = [old_filename, new_filename] + details
        migrate_values.append(values)
        print('Found Accepted Problem: ' , str(values[0]) , str(values[2]) , str(values[3]))

df_migrate_values = pd.DataFrame(migrate_values, columns=['Old Filename', 'New Filename', 'Runtime', 'Memory', 'Best Score Url'])
df_migrate_values.to_csv(root_path + sync_work_path + 'sync_values.csv')