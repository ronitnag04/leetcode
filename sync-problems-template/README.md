# Migrate Leetcode-Sync with Runtime & Memory Data
Follow the steps below to migrate your files

### Packages Used
Make sure the following packages and libraries are installed on your device. You may need to add packages not listed. here
- Numpy
- Pandas
- Selenium
- GitPython

***

## Step 1: Setting up repository
1. Create repository on your account
2. Open repository on your computer with your favorite editor -- **We all know VSCode is the best though :)**
3. Create a folder called sync-problems, and copy the contents of this folder into this folder
4. Create a .gitignore file and make sure the sync-problems folder is added so your login info, etc is not stored

## Step 2: Sync previously solved problems
Follow steps in [S1_get_submitted_problems.py](S1_get_submitted_problems.py)
1. Copy submissions data in [submissions.json](submissions.json)
2. Create workflow on GitHub, copy provided [workflow code](sync_leetcode.yml). This should add a .github\workflows\sync_leetcode.yml folder and file to the main repo folder
3. There should be a new folder called problems in this workspace containing all of your synced Leetcode solutions
4. There should be a new file called sync_values.csv in the sync-problems folder

## Step 3: Extract distribution scores for solved problems
Follow steps in [S2_extract_distribution_values.py](S2_extract_distribution_values.py)
1. Make sure the chromedriver.exe is downloaded in the sync_problems folder so you don't push the large file to github
2. The path to the driver ends in 'chromedriver' (without .exe)
3. This step may take time 
  - Depends on how many problems you need to sync as the webscraper loads each page
  - Please let me know if you can find the exact api to get the distribution percentages
  - I was able to speed up step 2 by finding the graphql API Leetcode uses, but I was not able to find the API request for the distribution percentages
4. Note that the scores for some distributions may not be available
5. There should be a new file called sync_values_distributions.csv in the sync-problems folder
  

## Step 4: Migrate and commit synced problems with scores
Follow steps in [S3_migrate_sync.py](S3_migrate_sync.py). This step moves the files from the problems folder in Step 2 to the main folder, and commits the change with scores from step 3.
1. This step may require some user input
   - The naming convention LeetCode uses for its problems might cause issues with the synced problems
   - Have the file explorer for your workspace open so you can find the correct folder to reference
2. Look at where your folders have moved before pushing changes

## Step 5: Sync repository with Leethub
Go to [LeetHub](https://chrome.google.com/webstore/detail/leethub/aciombdipochlnkbpcbgdpjffcfdbggi?hl=en) and sync this repository with the extension

***
Your repository should be migrated and synced with LeetCode. Happy Coding!
   
  






