# The open question is: 
- How can we classify if a dog is racist?
- If the dog is racist, how can we predict the behavior of the dogs?
- 
For that, you need a dataset of dog's behavior: 

- At what age do dogs start to bark at people?
- At what age do dogs start to bark at people of different races?
- At what age do dogs start to bark at people of different genders?
- At what age do dogs start to bark at people of different skin colors?
- etc

# The purpose of this project is to 
- Create a (fun, synthetic) dataset that demonstrates  dogs’ racism
- Develop a model to predict the behavior of the dogs

# Folder structure:
- data: Save the data here.
- models: Save the models here.
- notebooks: Save the notebooks here. Implement a notebook to train and evaluate the model.
- reports: Save the reports here.
- tests
- utils
 - `generate_data.py`: Generate the data
 - `train_model.py`: Train the model (XGBoost). 
 - `evaluate_model.py`: Evaluate the model. 
 - `raise_awareness.py`: Raise awareness of the problem of racism and the importance of diversity. 
- .gitignore: For this Python project.
- README.md: Describe the project, how to run the code, how to use the dataset, how to train the model, how to evaluate the model, how to use the model, etc.

# Suggested attributes: 
See the "# The situation" below. 

# Requirements:
- Python 3.9
- Use `uv` for dependency management
- Use virtual environment for the project

This project links: NLP, AI, health care 

# The situation
The dogs bark at person depends on their 
- race
- gender
- age
- skin color
- <add more attributes to make it more complex>

# Further steps
(Just mention it, don't implement anything)
- Develop a model to predict the behavior of the dogs
- Develop a drug that cure racist dogs 
- Develop a speech-to-text model to convert the speech of the dogs to text.
- Develop a model to raise awareness of the problem of racism and the importance of diversity
