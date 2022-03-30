# Twitter-Crawler
if you don't want read english readme, you can go to file zh-README.md
This project is a crawler program. which can automatically collect information from Twitter by the keywords you set. use this program you can get:
- username
- name
- date
- language
- comments num
- likes num
- forward num
## parameters 
- keywords_path: the keywords you want to search
- stop_num: the number of tweets you want to search
- output_dir: the directory you want to save the result
- date_time: the date you want to search
- limit_language: the language you want to search.it's default value is 'all'
## Usage
- in `main.py` Please set chrome driver path and parameters correctly.
- if you want to get followers of a user, please use file `GetFunsNum.py`. you just need to enter the chrome driver path and the csv file path which is get from `main.py`.
- in fact, the GetFunsNum.py can use a csv file which just contains username.
## To do
- [x] Get follower count from Twitter (here I use a noob method to get it)
## Requirements
- python>=3.6
- chromedriver version need to match your Chrome version
## Contact Information
- Email: serein7z@163.com 

If you have any questions, please contact me.

