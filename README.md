## Setup

- copy this repository into your own PRIVATE repository on GitHub (the free plan allows you to has a private repository with up to 3 collaborators)

- invite the GitHub users firemuzzy to your Repository


- verify that you have python3 installed run `python3 --version`

- initalize the python venv `./setup_venv.sh`

- activate the venv `. ./bin/activate`  (later run `deactivate` to deactivate the python environment)

- install the requirements `pip install -r requirements.txt`

## Running the job

- run `./run_pipeline.sh`

## Task

Update the exising processing pipeline to do the following

- Count all the words by letter they start with (treat upper case and lower case as the same)

- Calculate what percentage of the total words start with each letter of the alphabet:  WORD_COUNT/TOTAL_WORD_COUNT * 100

TIP: Look at the side inputs doccumentation for loating the total words count into each calculation (https://beam.apache.org/documentation/programming-guide/#side-inputs)

- Save the the output into `out` folder, file name can anything as long as it is the `out` folder

You file should be lines of triplets

`(LETTER, COUNT_OF_WORDS_STARTING_WITH_THAT_LETTER, PERCENTAGE_OF_WORDS_STARTING_WITH_THAT_LETTER)`

your file should look like the section below but with real counts and precentages

```
('A', 6, 1.0)
('B', 3, 0.5)
('C', 3, 0.5)
('D', 3, 0.5)
('E', 3, 0.5)
('F', 3, 0.5)
....
('W', 3, 0.5)
('X', 3, 0.5)
('Y', 3, 0.5)
('Z', 3, 0.5)
```

All your operations need be written using Apache beam components, here are the ones you will most likely be using. You can use any other ones, but if you are new to Beam don't bother researching them, you will not need to use any other components.

- DoFn
- CombineFn
- ParDo
- Map
- Filter
- CombineGlobally
- CombinePerKey
- CombineValues
- GroupByKey


## Help

`pipeline.py` defines all the pipeline pieces

Beam doccumentation https://beam.apache.org/get-started/quickstart-py/

To load the total cound of all the words into your step of the pypeline https://beam.apache.org/documentation/programming-guide/#side-inputs