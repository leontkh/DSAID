import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import requests
plt.style.use('seaborn-talk')

country = "Singapore"
case_types = ["confirmed", "recovered", "deaths"] 
rename_dict = {"confirmed": "Confirmed cases", "recovered": "Cases recovered", "deaths": "COVID-19 deaths"}
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
        
main_df.replace(to_replace=0, value=np.nan, inplace=True)

for case_type in case_types:
    plt.plot(main_df["Date"], main_df[case_type], label = rename_dict[case_type])
plt.title("Graph of Cumulative number of COVID-19 cases in Singapore over Time")
plt.legend()
plt.xlabel("Time(Months)")
plt.ylabel("Cumulative number of COVID-19 cases in Singapore")
plt.savefig('sg_covid_cases.png')