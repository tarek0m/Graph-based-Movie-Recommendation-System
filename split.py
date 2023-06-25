# Open the original file in read mode
with open('datasets/ml-1m/users.dat', 'r') as original_file:
    # Open two new files in write mode
    with open('users_before_5941.dat', 'w') as file_before_5941, \
            open('users_from_5941.dat', 'w') as file_from_5941:

        # Flag to determine if we've encountered the line starting with '5941'
        found_5941 = False

        # Loop through each line in the original file
        for line in original_file:

            # Check if the line starts with '5941'
            if line.startswith('5941'):
                # Set the flag to True
                found_5941 = True

                # Write the line to the second file
                file_from_5941.write(line)

                # Continue to the next line
                continue

            # If we haven't found '5941' yet, write the line to the first file
            if not found_5941:
                file_before_5941.write(line)

            # If we've already found '5941', write the line to the second file
            else:
                file_from_5941.write(line)


# Open the original file in read mode
with open('datasets/ml-1m/ratings.dat', 'r') as original_file:
    # Open two new files in write mode
    with open('ratings_before_5941.dat', 'w') as file_before_5941, \
            open('ratings_from_5941.dat', 'w') as file_from_5941:

        # Flag to determine if we've encountered the line starting with '5941'
        found_5941 = False

        # Loop through each line in the original file
        for line in original_file:

            # Check if the line starts with '5941'
            if line.startswith('5941'):
                # Set the flag to True
                found_5941 = True

                # Write the line to the second file
                file_from_5941.write(line)

                # Continue to the next line
                continue

            # If we haven't found '5941' yet, write the line to the first file
            if not found_5941:
                file_before_5941.write(line)

            # If we've already found '5941', write the line to the second file
            else:
                file_from_5941.write(line)


from sklearn.model_selection import train_test_split
import pandas as pd
import os
import re


dataPath = "data1m"
dir_list = os.listdir(dataPath)

for dir in dir_list:
    alpha_value = float(re.findall("\d+\.\d+", dir)[0])
    X = pd.read_pickle(dataPath+'\\'+dir)
    X_train, X_test = train_test_split(X, test_size=0.2, random_state=25) # test = 20%
    X_train.to_pickle("splitted/x_train_split_alpha(" + str(alpha_value) + ").pkl")
    X_test.to_pickle("splitted/x_test_split_alpha(" + str(alpha_value) + ").pkl")
