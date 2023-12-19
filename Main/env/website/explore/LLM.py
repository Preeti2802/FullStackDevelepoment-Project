import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder

# Step 1: Read the Data
# Assuming your uploaded data is in a format that pandas can read like CSV.
data = pd.read_csv(r'C:\Users\jayana abhigna sree\Documents\CSE-AI\VS codes\.vscode\ENV2\website\explore\engineering_dataset.csv')

# Step 2: Pre-process the Data
# Convert the 'Preferred_Course' column to numerical values
label_encoder = LabelEncoder()
data['Preferred_Course'] = label_encoder.fit_transform(data['Preferred_Course'])
data


# Step 3: Split the Data
# Define your features and labels
y = data['Preferred_Course']
data=data.drop('Preferred_Course', axis=1)
X = data  # Features   
# Split the data into a training set and a testing set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)
print(len(X_train), len(X_test))
# Step 4: Train the Model
# Use a RandomForestClassifier, but you can choose other classifiers too
classifier = RandomForestClassifier(n_estimators=100, random_state=42)
classifier.fit(X_train, y_train)

# Step 5: Evaluate the Model
# Make predictions on the test set
y_pred = classifier.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy:.2%}")
y_pred
import joblib
model_filename = 'FSD.pkl'

joblib.dump(classifier, model_filename)
print(f"Model saved as {model_filename}")
X_test
X_test.iloc[0]
y_test.iloc[0]
# Step 6: Make Predictions
# Function to make new predictions
def make_recommendation(new_data):
    new_data = pd.DataFrame([new_data])
    #display(new_data)
    prediction = classifier.predict(new_data)
    return label_encoder.inverse_transform(prediction)[0]

# You should also ensure that the 'classifier' and 'label_encoder' are properly trained and fitted with the entire set of features before calling `make_recommendation`.
#print(X_test)
i=2
recommended_course = make_recommendation(X_test.iloc[i])
print(y_test.iloc[i])
print(f"Recommended Course: {recommended_course}")

















'''import openai
import json

openai.api_key = "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"

function_descriptions = [{
    "name": "course",
    "description": "recommends course based on the users response to the questions asked",
    "parameters": {
        "type": "object",
        "properties": {
            "course": {
                "type": "object",
                "properties": {
                    "value": {
                        "type": "string",
                        "description": "Given a set of questions and their respective binary responses (0 for yes and 1 for no), interpret the answers and recommend a suitable course. The available courses are EEE (Electrical and Electronics Engineering), ECE (Electronics and Communication Engineering), AI (Artificial Intelligence), CSE (Computer Science and Engineering), ME (Mechanical Engineering), and Civil Engineering stictly do not consider any other course other than thos ementioned in here"
                    }
                }
            }
        }
    }
}]

def ask_function_calling(query):
  messages = [{'role': 'user', 'content': "Do u like coding? 0, Do u like maths? 0, Do u like low-level coding? 1, Do u like circuits and its design? 0, Do u like communications technologies? 1, Do u like material sciences? 1, Do u like machine designs and manufacturing? 1, Do you like urban planning and development? 0"},
                {'role': 'assistant', 'content': None,'function_call':{"name": function_descriptions[0]["name"], "arguments": json.dumps({"course":"BTech Electronics and Communication Engineering"},indent=2,ensure_ascii=False,)}},
                {'role': 'user', 'content': "Do u like coding? 1, Do u like maths? 0, Do u like low-level coding? 1, Do u like circuits and its design? 0, Do u like communications technologies? 0, Do u like material sciences? 0, Do u like machine designs and manufacturing? 0, Do you like urban planning and development? 1"},
                {'role': 'assistant', 'content': None,'function_call':{"name": function_descriptions[0]["name"], "arguments": json.dumps({"course":"BTech Civil Engineering"},indent=2,ensure_ascii=False,)}},
                {'role': 'user', 'content': "Do u like coding? 1, Do u like maths? 1, Do u like low-level coding? 1, Do u like circuits and its design? 0, Do u like communications technologies? 1, Do u like material sciences? 0, Do u like machine designs and manufacturing? 1, Do you like urban planning and development? 0"},
                {'role': 'assistant', 'content': None,'function_call':{"name": function_descriptions[0]["name"], "arguments": json.dumps({"course":"B.Tech Computer Science Engineering"},indent=2,ensure_ascii=False,)}},
                {'role': 'user', 'content': "Do u like coding? 0, Do u like maths? 1, Do u like low-level coding? 1, Do u like circuits and its design? 1, Do u like communications technologies? 0, Do u like material sciences? 0, Do u like machine designs and manufacturing? 1, Do you like urban planning and development? 0"},
                {'role': 'assistant', 'content': None,'function_call':{"name": function_descriptions[0]["name"], "arguments": json.dumps({"course":"B.Tech Artificial Intelligence"},indent=2,ensure_ascii=False,)}},
                {'role': 'user', 'content': query}]
  response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo-0613",
    messages=messages,
    functions=function_descriptions,
    function_call="auto", # this forces calling `function`
    )
  response_message = json.loads((response["choices"][0]["message"]['function_call']['arguments']))
  print(response["choices"][0]["message"]['function_call']['name'], response_message)'''
