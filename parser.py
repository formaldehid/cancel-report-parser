import pandas as pd

dfs = pd.read_html('CancelReport.xls')
df = dfs[1]
df[:-5].to_csv('CancelReport.csv', header=False, encoding='utf-8')
