import requests
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('seaborn-talk')

country = "Singapore"
case_types = ["confirmed", "recovered", "deaths"] 
url = "https://api.covid19api.com/total/country/{}/status/{}"

main_df = None
for case_type in case_types:
    case_url = url.format(country, case_type)
    resp = requests.get(case_url)
    df = pd.DataFrame(resp.json())[["Cases","Status","Date"]]
    df['Date']= pd.to_datetime(df['Date']).dt.date
    df.rename(columns={"Cases": df["Status"][0]},inplace=True)
    df.drop(columns=["Status"],inplace=True)
    if main_df is None:
        main_df = df
    else:
        main_df = main_df.merge(df, how='outer', on="Date")
        
for case_type in case_types:
    plt.plot(main_df["Date"], main_df[case_type], label = case_type)
plt.legend()
plt.savefig('sg_covid_cases.png')