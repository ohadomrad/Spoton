import deezer_callect_data
import google_collect_data
import acoustic_brainz_collect_data
import pandas as pd

def build_dataset():
    pd.set_option('display.max_columns', None)
    acoustic_brainz = acoustic_brainz_collect_data.build_dataset()
    print('-------------------- acoustic brainz frame --------------------')
    print(acoustic_brainz.head())
    print(acoustic_brainz.columns)

    #print(acoustic_brainz['recordings'].iloc[0])

    deezer_df = deezer_callect_data.build_dataset()
    print('-------------------- deezer data frame --------------------')
    print(deezer_df)
    print('-------------------- google data frame --------------------')
    google_df =google_collect_data.build_dataset()
    print(google_df)
    merged_df = pd.merge(deezer_df, google_df, on='track_title', how='inner')
    print('------------------------------------------------------------')
    return merged_df

df = build_dataset()
print('-------------------- final data frame --------------------')
print(df)