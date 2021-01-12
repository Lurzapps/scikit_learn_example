# scikit learn example
###necessary libraries
(install via `pip install`)
- matplotlib
- scikit-learn
- pandas

##global_variables.py
Here all global variables like the column names etc. are set. Please change accordingly to your needs.

##visualize_dataset.py
Visualize the main dataset.

##generate_model.py
This reads in the training and testing csv, train a model, print out the score this model reaches with the test data and save it in a binary file that can be loaded using `use_dataset.py`.

##use_dataset.py
Let this run using the python console. It allows you to predict arrays after loading a before generated model.
