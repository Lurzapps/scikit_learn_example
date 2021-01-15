# scikit learn housing prices project
Compares the algorithms Linear Regression, K-Nearest-Neighbours & Random Forest on four city housing prices datasets (Delhi, Bangalore, London, Melbourne)<br><br>
necessary libraries:<br>
(install via `pip install`)
- matplotlib
- scikit-learn
- pandas
<br><br>
`global_variables.py`<br>
Here all global variables like the column names etc. are set. Please change accordingly to your needs.
<br><br>
`visualize_dataset.py`<br>
Visualize the main dataset.
<br><br>
`generate_model.py`<br>
This reads in the training and testing csv, train a model, print out the score this model reaches with the test data and save it in a binary file that can be loaded using `use_dataset.py`.
<br><br>
`use_dataset.py`<br>
Let this run using the python console. It allows you to predict arrays after loading a before generated model.
