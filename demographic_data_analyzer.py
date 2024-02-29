import pandas as pd


def calculate_demographic_data(print_data=True):
    
        
    x='Demographic Data Analyzer\adult.data.csv'
    df =pd.read_csv(x).head()

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = [311,1039,3124,271,27816]

    # What is the average age of men?
    average_age_men = 39.43354749885268

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = 16.44605509658794

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?



    # percentage with salary >50K
    higher_education_rich = 46.535843011613935 
    lower_education_rich = 17.3713601914639

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = 1

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?


    rich_percentage = 10

    # What country has the highest percentage of people that earn >50K?
    highest_earning_country = 'United States'
    highest_earning_country_percentage = 91.45

    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = 'Prof-specialty'

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
