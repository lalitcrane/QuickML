
Encoding Cardinal Values

Label Encoding
  Labels are given numeric values.
One Hot Encoding
  Why Use One Hot Encoding? Some algorithms associate some hierarchy/relationships with the encoding 
  that is achieved using Label Encoding. So we use One Hot enclding.
  
Sklearn has simple routines to handle both.
https://towardsdatascience.com/categorical-encoding-using-label-encoding-and-one-hot-encoder-911ef77fb5bd

from sklearn.preprocessing import LabelEncoder
labelencoder = LabelEncoder()
bridge_df['Bridge_Types_Cat'] = labelencoder.fit_transform(bridge_df['Bridge_Types'])

from sklearn.preprocessing import OneHotEncoder
enc = OneHotEncoder(handle_unknown='ignore')

enc_df = pd.DataFrame(enc.fit_transform(bridge_df[['Bridge_Types_Cat']]).toarray())
bridge_df = bridge_df.join(enc_df)




