# utility_functions.py

def calculate_label_rate(df):
    
    # Get the total number of samples
    total_samples = len(df)
    
    # Count the occurrences of each label in the 'label' column of df dataframe.
    label_counts = df['label'].value_counts()
    # Extract the count of positive labels (label == 1) from the label_counts series.
    positive_count = label_counts.get(1, 0)
    # Extract the count of negative labels (label == 0) from the label_counts series.
    negative_count = label_counts.get(0, 0)
    # Calculate the rate of positive labels to negative labels.
    label_rate = positive_count / negative_count if negative_count != 0 else 0
    
    # Print the sizes of positive and negative samples along with the label rate, formatted to two decimal places.
    print("Total Sample size is {}, Positive Sample size is {}, Negative Sample size is {}, label rate is {:.2f}".format(total_samples, positive_count, negative_count, label_rate))
