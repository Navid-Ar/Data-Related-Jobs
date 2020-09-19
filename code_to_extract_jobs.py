import glassdoor_scraper as gs
import pandas as pd
df = gs.get_jobs("data scientist", 300, False)
df.to_csv('C:\Users\Navid\Documents\ds_salary_proj\data_frame3')
