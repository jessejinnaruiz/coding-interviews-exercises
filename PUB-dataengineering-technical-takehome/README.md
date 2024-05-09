# Data Engineering Technical Assesment - SOLUTION

# Solution Components:
## Main module (executable)
## Data Pull
## Exploratory Data Analysis
## Preprocessing
## Feature Engineering
## Reporting analysis findings (ipynb notebook)


# HOW TO USE:
 To execute the pipeline, which will produce a output csv file, please run main() from src directory or alternatively run from the included notebook with jupyter. To review the findings please open the .ipynb notebook:

`cd src/`
`jupyter notebook`

File structure as follows:
    ```
    PUB-dataengineering-technical-takehome
    │   README.md
    │   
    └───data
    │   │   data-log.csv
    └───src
        │   datapull.py
        │   eda.py
        │   feateng.py
        │   main.py
        │   offload.py
        │   preprocess.py
        |   solution-technical-nb.ipynb
        |   requirements.txt
    ```

### TODO:       
- [x] main module
- [x] Exploratory data analysis
- [x] derive watch-time (duration of a stream in minutes) at the asset, device and client ip level
- [x] analysis: 1. top 25 most popular programs
- [x] analysis: 2. avg watch time per tv series
- [ ] analysis: 3. How many times did users who watched SeriesTitle0 not watch whole 45 minutes?
~~data report/chart with findings~~
~~sql file to pull in data~~



-------------------------------------------------------------------------------------------




README:
    Build your solution in the SRC folder. Provide us with source code that we can run on our end to reproduce your results and/or tests/builds. The choice of tools and packaging for building this project are up to you but please don’t use a remotely hosted source-control tool. 

    This test is designed to help us asses your ability to problem solve and prqogram around a relevant data transformation use-case. The provided data sample is anonymized for privacy reasons and it reflects information from our content distribution network, (i.e. how we serve streams).

    Assessment has the following folder structure:
    ```
    fr-de-ta
    │   README.md
    │      
    └───data
    │   │   data-log.csv.zip
    │   │
    └───src
        │   
    ```

SOURCE DATA:

    The 'data' folder houses data-log.csv, the source material for our test. This dataset is a second-by-second log of http requests from clients, including over-the-top streaming devices like RokuTV, that retrieve packets of data which become video streams on TVs and in many cases, mobile devices. The information is logged at the device and client IP (mobile or household network) level and can be summarized to show duration streamed across different content assets which are episodes of series or films.

    DATA DICTIONARY:

        Below is a preview of the extract's structure with some key callouts:

        | date       | time     | original_title          |   sac_status | device   |   node_ID | anon_ip      | anon_cs_user_agent   |
        |:-----------|:---------|:-----------------------|------------:|:---------|---------:|:-------------|:---------------------|
        | 2021-09-29 | 23:57:36 | S06 E05 - SeriesTitle0 |         200 | Roku     | 10294754 | 281.60.67.0  | user-agent0          |
        | 2021-09-30 | 07:07:16 | S03 E04 - SeriesTitle0 |         206 | Roku     | 10294350 | 42.41.600.0  | user-agent1          |
        | 2021-09-30 | 07:18:15 | S03 E04 - SeriesTitle0 |         206 | Roku     | 10294350 | 42.41.600.0  | user-agent1          |
        | 2021-09-30 | 02:51:05 | FilmTitle63            |         200 | Roku     | 10233175 | 943.70.584.0 | user-agent2          |

        anon_ip: This is unique client IP. One IP can serve many devices.
        anon_cs_user_agent: This is device. Naturally, viewers can watch a myriad of content in one device session.
        node_ID: This is a unique identifier of a content asset, which in this case is either an episode in a given season of a TV series or a standalone film.

SRC:

    This folder is your greenfield - we will leave it up to you in terms of tools and packaging for building a project to accomplish the assesment objectives. 


TEST OBJECTIVES:

    We would like to see how you would unpack some of the most granular viewership data we have on hand across our vast content library and OTT audience. 

    1. Aggregation:
        - Summarize the raw data set and derive watch-time (duration of a stream in minutes) at the asset, device and client ip level. 
            - We're not so interested in trends at the episode level, so make sure that we can further aggregate watch-time at both the season and series levels. 

    2. Analysis:
        - Now that you've derived the watch-time dataset, produce the following metrics:
            - What are the top 25 most popular programs?
            - What is the average watch-time for each TV Series across the sample?
            - How many times did users who watched SeriesTitle0 at some point during their session, change programs, either to another film or series, before the end of an approximately 45 minute episode runtime?


