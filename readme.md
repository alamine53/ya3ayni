## Run

from the command terminal, navigate to folder and activate environment. 

Set environment variables
``` 
$ python src/config.py 
```
then read in the data and create features and labels
```
$ python src/read_data.py
```

### Inference

To make inference or produce shapley plot
```
$ python src/shapley.py
```
### Train Model

To re-train the model, first create folds. This will generate train-test splits.
Note: the folds do NOT recognize the response variable, they treate the whole dataset as one. Only in the training is the Y vairable identified. 

```
$ python src/create_folds.py
$ python src/train.py
```
