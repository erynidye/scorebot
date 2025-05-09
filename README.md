# CyberPatriot ScoreBot

This discord bot was built to scrape the leaderboard for the CyberPatriot cybersecurity competition as a round progressed, getting information such as team number, location, tier, and current score for all categories, including Windows, Linux, and Cisco. It had the capability to use current scraped data or the downloaded CSV file for final round scores.

By inputting a four-digit team number, the user can get the current position of the team on the leaderboard using the !position [team number] command; and get all information about a team, including image scores, cisco scores, division/category using the !team [team number] command based on final round data. Using the !lb command, the user can get the top 15 teams as well as the time when the data was taken; and using the !stats command, the discord bot would output simple summary statistics, as well as generate a distribution graph.

This bot worked in the 2023-2024 CyberPatriot competition season (CyberPatriot XVI) but no longer works from the 2024-2025 season onward. Hopefully, the bot will be fixed for the 2025-2026 season.

The discord bot uses the discord.py framework. Data processing was done with the Python Pandas module, and graphs are generated with the Python matplotlib module. Web scraping was done with the html_table_parser module.

Example images:

<img width="341" alt="Screenshot 2025-05-08 at 9 57 42 PM" src="https://github.com/user-attachments/assets/fbe95011-b3ed-4539-b0aa-9761f35ad65e" />
<img width="412" alt="Screenshot 2025-05-08 at 9 57 56 PM" src="https://github.com/user-attachments/assets/004f3722-cdaf-4184-826c-648fa7ad05c0" />
<img width="438" alt="Screenshot 2025-05-08 at 9 58 14 PM" src="https://github.com/user-attachments/assets/ef1d9c83-8d70-451e-8663-23988d0e312f" />
<img width="515" alt="Screenshot 2025-05-08 at 9 58 05 PM" src="https://github.com/user-attachments/assets/ab8848fe-7e8a-43a2-8663-6920c6c6593e" />



