import os
import pandas as pd

data_folder = 'final_demo'
data_csv = os.path.join(data_folder, 'AML_data_all.csv')
# data_csv = os.path.join(data_folder, 'AML_data.csv')
output_csv = os.path.join(data_folder, 'final_demo_result.csv')

df = pd.read_csv(data_csv).drop(['Unnamed: 0'], axis=1)
# print(df.iloc[1])

names = []

# print(df['name'][6220:])

# Drop len(name) = 1
df = df[df['name'].apply(lambda x: len(x) > 1)]

# print(df.columns)
new_df = df.reindex(
    columns=list(['name', 'age', 'title', 'crime', 'crime_risk', 'key_sentence', 'news_title', 'news_link',
                  'other_suspect', 'suspect_probability']))

print(new_df.iloc[1])
new_df.to_csv(output_csv, index=False)
