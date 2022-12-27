# Leetcode Progress Tracker
This is a repository containing all of my solved problems on Leetcode

## Applications Used
- Uses [LeetHub](https://chrome.google.com/webstore/detail/leethub/aciombdipochlnkbpcbgdpjffcfdbggi?hl=en), developed by Qasim Wani to commit new solved problems
- Uses [Leetcode-Sync](https://github.com/joshcai/leetcode-sync) action developed by Josh Cai for initially syncing old problems

## My Additions
Both Leethub and Leetcode-Sync contain amazing features, but they lack the ability to sync existing content:
- Leethub, as of creating this repo (12-26-22) does not have a feature to sync previously solved problems
- Leetcode-Sync, as of creating this repo (12-26-22), does not pull runtime or memory distribution scores,

I created a method to sync these problems to the repository.
Using [Selenium](https://selenium-python.readthedocs.io/) to extract the runtime and memory distribution percentages, and [GitPython](https://gitpython.readthedocs.io/en/stable/index.html) to add these percentages to commit messages. 

Go to the [sync-problems-template](sync-problems-template) folder for more information