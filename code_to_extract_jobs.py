import glassdoor_scraper as gs
import pandas as pd
df = gs.get_jobs("data scientist", 1000, False)
df.to_csv('data_frame2')
