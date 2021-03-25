from urllib.request import urlretrieve
import pandas as pd
urlretrieve('https://hub.jovian.ml/wp-content/uploads/2020/09/countries.csv',
            'countries.csv')
countries_df = pd.read_csv('countries.csv')
#Q: How many countries does the dataframe contain?
num_countries = countries_df.shape[0]
print('There are {} countries in the dataset'.format(num_countries))
#Q: Retrieve a list of continents from the dataframe?
E=countries_df['continent']
continents = pd.unique(E)
#Q: What is the total population of all the countries listed in this dataset?
total_population = countries_df['population'].sum()
print('The total population is {}.'.format(int(total_population)))
#Q: (Optional) What is the overall life expectancy across in the world?
weighted_sum = (countries_df.population * countries_df.life_expectancy).sum()
weighted_average = weighted_sum / countries_df.population.sum()
print ('The overall life expectancy across the world is {:.3f}'.format(weighted_average))

#Q: Create a dataframe containing 10 countries with the highest population.
most_populous_df =countries_df.sort_values(by=['population'], ascending=False).head(10)
print(most_populous_df)
#Q: Add a new column in countries_df to record the overall GDP per country (product of population & per capita GDP)
countries_df['gdp'] = countries_df.population *countries_df.gdp_per_capita
#Q: Create a data frame that counts the number countries in each continent?
country_counts_df=countries_df.groupby(by=['continent'])['location'].count()
urlretrieve('https://hub.jovian.ml/wp-content/uploads/2020/09/covid-countries-data.csv',
            'covid-countries-data.csv')
covid_data_df = pd.read_csv('covid-countries-data.csv')
#Q: Count the number of countries for which the total_tests data is missing
total_tests_missing = covid_data_df.total_tests.isna().sum()
print("The data for total tests is missing for {} countries.".format(int(total_tests_missing)))
#Q: Merge countries_df with covid_data_df on the location column.
combined_df = countries_df.merge(covid_data_df,on='location')
#Q: Add columns tests_per_million, cases_per_million and deaths_per_million into combined_df.
combined_df['tests_per_million'] = combined_df['total_tests'] * 1e6 / combined_df['population']
combined_df['cases_per_million'] = combined_df['total_cases'] * 1e6 / combined_df['population']
combined_df['deaths_per_million'] = combined_df['total_deaths'] * 1e6 / combined_df['population']
#Q: Create a dataframe with 10 countires that have highest number of tests per million people.

highest_tests_df =combined_df.sort_values(by=['tests_per_million'],ascending=False).head(10)
print("highest_tests_df",highest_tests_df)
#Q: Create a dataframe with 10 countires that have highest number of positive cases per million people

highest_cases_df=combined_df.sort_values(by=['cases_per_million'],ascending=False).head(10)
#(Optional) Q: Count number of countries that feature in both the lists of "highest number of tests per million" and "highest number of cases per million".
highest_cases_df.head(10).merge(highest_tests_df.head(10), on='location')
count=highest_cases_df.head(10).merge(highest_tests_df.head(10), on='location').location.count()
print(' Count number of countries that feature in both the lists of "highest number of tests per million" and "highest number of cases per million"',count)
#(Optional) Q: Count number of countries that feature in both the lists "20 countries with lowest GDP per capita" and "20 countries with the lowest number of hospital beds per thousand population". Only consider countries with a population higher than 10 million while creating the list
#male_student=student_dt.gender == 'M'
pop_more_than_10=combined_df.population>10000000
popul=combined_df[pop_more_than_10]

lowest_GDP=popul.sort_values(by=['gdp_per_capita'],ascending='True').head(20)
print('Count number of countries that feature in both the lists "20 countries with lowest GDP per capita" and "20 countries with the lowest number of hospital beds per thousand population". Only consider countries with a population higher than 10 million while creating the list.',lowest_GDP)
lowest_no_beds = popul.sort_values('hospital_beds_per_thousand',ascending=True).head(20)
#lowest_no_beds


countries_features_both = lowest_GDP.merge(lowest_no_beds, on ='location')
#print(countries_features_both)
count2=countries_features_both.location.count()
#print(count2)
print("countries_features_both")
print(countries_features_both)
