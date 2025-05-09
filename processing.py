import pandas as pd
import matplotlib.pyplot as plt
from html_table_parser import HTMLTableParser
import urllib.request


def scrape(tier):
    # web scraping
    if tier.lower() != "all":
        url = "https://scoreboard.uscyberpatriot.org/index.php?division=Open&tier="+tier
    else:
        url= "https://scoreboard.uscyberpatriot.org/index.php?division=Open"
    req = urllib.request.Request(url=url)
    f = urllib.request.urlopen(req)
    xhtml = f.read().decode('utf-8')
    p = HTMLTableParser()
    p.feed(xhtml)
    return process(p)


def process(p):
    df = pd.DataFrame(p.tables[0])
    df = df.drop(columns=[3, 4, 5, 6, 8])
    df = df.drop(0)
    df = df.rename(columns={0: "Rank", 1: "Team Number", 2: "Location", 7: "Time", 9: "Image Score", 10: "Adjustment", 11: "Cisco Score", 12: "Total Score"})
    df['Image Score'] = df['Image Score'].astype(float)
    df['Cisco Score'] = df['Cisco Score'].astype(float)
    df['Total Score'] = df['Total Score'].astype(float)
    df.to_csv('data.csv', index=False)
    return df


def process_r2():
    df = pd.read_csv('r2.csv')
    df['R1 Total Score'] = df['R1 Total Score'].astype(float)
    df['R2 Image Score'] = df['R2 Image Score'].astype(float)
    df['R2 Cisco Score'] = df['R2 Cisco Score'].astype(float)
    df['Cumulative Score'] = df['Cumulative Score'].astype(float)
    return df


def plot(df):
    plt.hist(df['Total Score'], color="b")
    plt.xlabel("Score")
    plt.ylabel("Number of Teams")

    plt.savefig('score.png')
