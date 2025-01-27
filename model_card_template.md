# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details

In this project, I will be developing a classification model on publicly available Cencure 
Bureau data.  It will use demographic and employment categorical features of individuals 
from the Census Bureau data, that will be listed below, to test the split data of 80% training
set and 20% test set.  This will be based on a binary measurement of less than 50k and more 
than 50k.

## Intended Use

It will be used to predict whether income exceeds $50/yr based on census data or is less.  The 
most useful scenario would be for analyzing socioeconomic disparaties based on the given 
categorical features from the Census Bureau dataset.

## Training Data

The model was trained on the Census Bureau's "Adult" dataset, which contains category features 
such as Workclass, Education, Marital-status, Occupation, Relationship, Race, Sex, Native-country, 
Age, and Hours-per-week.  The extraction was by Barry Becker from the 1994 Census database.The link 
to the datasets is https://archive.ics.uci.edu/dataset/20/census+income.  The citation is Kohavi, R. 
(1996). Census Income [Dataset]. UCI Machine Learning Repository. https://doi.org/10.24432/C5GP7S.

## Evaluation Data

The evaluation of the model was done on the 20% test data that was held out from the training.  It 
ensures that the evaluation on the 20% test data (on a small scale), can also be applied on the 80% 
training data (a large scale).

## Metrics
_Please include the metrics used and your model's performance on those metrics._

The overall metrics are Precision: 0.7419, Recall: 0.6384, and F1 Score: 0.6863.

This is an example of the results:

Precision: 0.7419 | Recall: 0.6384 | F1: 0.6863
workclass: ?, Count: 389
Precision: 0.6538 | Recall: 0.4048 | F1: 0.5000
workclass: Federal-gov, Count: 191
Precision: 0.7971 | Recall: 0.7857 | F1: 0.7914
workclass: Local-gov, Count: 387
Precision: 0.7576 | Recall: 0.6818 | F1: 0.7177
workclass: Private, Count: 4,578
Precision: 0.7376 | Recall: 0.6404 | F1: 0.6856
workclass: Self-emp-inc, Count: 212
Precision: 0.7807 | Recall: 0.7542 | F1: 0.7672
workclass: Self-emp-not-inc, Count: 498
Precision: 0.7064 | Recall: 0.4904 | F1: 0.5789
workclass: State-gov, Count: 254
Precision: 0.7424 | Recall: 0.6712 | F1: 0.7050
workclass: Without-pay, Count: 4
Precision: 1.0000 | Recall: 1.0000 | F1: 1.0000
education: 10th, Count: 183
Precision: 0.4000 | Recall: 0.1667 | F1: 0.2353
education: 11th, Count: 225
Precision: 1.0000 | Recall: 0.2727 | F1: 0.4286
education: 12th, Count: 98
Precision: 1.0000 | Recall: 0.4000 | F1: 0.5714
education: 1st-4th, Count: 23
Precision: 1.0000 | Recall: 1.0000 | F1: 1.0000
education: 5th-6th, Count: 62
Precision: 1.0000 | Recall: 0.5000 | F1: 0.6667
education: 7th-8th, Count: 141
Precision: 0.0000 | Recall: 0.0000 | F1: 0.0000
education: 9th, Count: 115
Precision: 1.0000 | Recall: 0.3333 | F1: 0.5000
education: Assoc-acdm, Count: 198
Precision: 0.7000 | Recall: 0.5957 | F1: 0.6437
education: Assoc-voc, Count: 273
Precision: 0.6471 | Recall: 0.5238 | F1: 0.5789
education: Bachelors, Count: 1,053
Precision: 0.7523 | Recall: 0.7289 | F1: 0.7404
education: Doctorate, Count: 77
Precision: 0.8644 | Recall: 0.8947 | F1: 0.8793
education: HS-grad, Count: 2,085


## Ethical Considerations

This dataset is from 1994 and does not reflect the current socioeconomic and demographic 
accuracy of the current times.  There could be biases in the predictions of certain groups
of people - biases that reflect the prejudices of that time.  The data contains personal
information that could be privacy concerns.  There needs to be more refinement of the data
before using it for decision-making purposes, such as lending for banks or for distributing
resources.

## Caveats and Recommendations

This is not to be used for real world decision making, since there's much more contextual
data that is needed for real world application.  This should only be used for educational
purposes, such as it is no in this course.  This dataset needs to be updated to reflect
unbiased and current 2024 to 2025 timeframe.
