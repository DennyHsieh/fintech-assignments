import os
import pandas as pd

data_folder = 'final_demo'
data_csv = os.path.join(data_folder, 'AML_data.csv')
output_csv = os.path.join(data_folder, 'final_demo_result.csv')

df = pd.read_csv(data_csv).drop(['Unnamed: 0'], axis=1)
# print(df.iloc[1])

df['age'] = None
df['title'] = None
# df['profile_id'] = 0
names = []


def add_col(row):
    for idx, val in enumerate(names):
        if row['name'] not in names:
            row['profile_id'] = idx
        else:
            row['profile_id'] = len(names)
        return row


# df = df.apply(add_col, axis=1)

new_df = df.reindex(
    columns=list(['name', 'age', 'title', 'crime', 'crime_risk', 'key_sentence', 'news_title', 'news_link',
                  'other_suspect', 'suspect_probability']))

print(new_df.iloc[1])
new_df.to_csv(output_csv, index=False)
