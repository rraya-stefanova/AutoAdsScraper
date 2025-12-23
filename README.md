# Automobile-Ads-Scraper
Job Ads Analyzer is a tool that allows users to analyze and explore job advertisements data. It provides features for viewing job trends, filtering ads, sorting, and more. This README provides information on how to use and install the project.

Table of Contents
Features
Installation
Usage
Tests
License
Features
Word Cloud for job titles
Distribution plots for date posted and count of job ads
Filtering and sorting job ads based on different criteria
Distribution of job ads by the date companies were founded
Displaying job and company data in the terminal
more...
Installation
Clone the repository:
git clone 
cd Job-Ads-Analyzer
Install dependencies:
# create virtual environment
python3 -m venv .venv 
pip install -r requirements.txt
Set up the database:
Initialize your SQLite database with job ads and company data.
touch .env #create .env file

# add this lines in the file .env and chnage db path to desired from you location 
# DB_PATH="/home/semir/python-project/Job-Ads-Analyzer/src/job_ads.db"
# COMPANY_URL="https://dev.bg/company/"
# SITE_URL="https://dev.bg"

cd src/dbsqlite
python3 create_tables.py
cd ../../
Scrape data for job ads and companies
This commands will take more time for execution
export PYTHONPATH="$PYTHONPATH:$PWD"
cd src/scraper
python3 company_scraper.py
python3 ads_scraper.py
Usage
Run the Job Ads Analyzer CLI (from project directory):
python main.py
Follow the on-screen instructions to log in or register.
Use the available commands to analyze job ads data.
Tests
Run all test with the following command (from project directory):
python3 test.py
License
This project is licensed under the Apache License.
