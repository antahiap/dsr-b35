## Portfolio

### Consider value with
- Learn
- Impress, easy to present 
- Social impact
- product/company


### What matters
- Demonstrate skills
- value/impact
- original
- data availability
- demonstrate visually
- suppervised learning, have standard
- No 3rd party


## Python
- Why: packaging, quick for prototyping, big community, R is specific for statistic,
- Object oriented programming, everything can be defined as an object (class) > so due to can it is not a fully-object oriented > java is
- Learning python OREILLY

- JupyterNotebook, good for visualization 
- python comprehention is quicker (one line for loop)


### PEP 8

PEP = Python Enhancement Proposal

[Python style guide - PEP 8](https://www.python.org/dev/peps/pep-0008/)

[Code Style - The Hitchhiker’s Guide to Python!](https://docs.python-guide.org/writing/style/)

[Chapter 2 of Effective Python - Brett Slatkin](https://effectivepython.com/)

Imports at the top of the `.py` file (each section in alphabetical order)
- standard library
- third party modules
- your own modules

Limits line length to 79 characters

### Using an API

Learning outcomes

- difference between API & webscraping
- what JSON is (and why it's like a Python `dict`)
- how to properly handle files in Python
- what a REST API is
- how to use the `requests` library

#### API versus web-scraping

**Both are ways to sample data from the internet**

API
- structured
- provided as a service (you are talking to a server via a REST API)
- limited data / rate limits / paid / require auth (sometimes)
- most will give back JSON (maybe XML or CSV)

Web scraping
- less structure
- parsing HTML meant for your browser

Neither is better than the other


- API developer can limit what data is accessible through the API
- API developer can not maintain the API
- website page can change HTML structure
- website page can have dynamic (Javascript) content that requires execution (usually done by the browser) before the correct HTML is available

Much of the work in using an API is figuring out how to properly construct URLs for `GET` requests
- requires looking at their documentation (& ideally a Python example!)

#### Where to find APIs

- [ProgrammableWeb](https://www.programmableweb.com/apis/directory) - a collection of available API's
- For the *Developer* or *For Developers* documentation on your favourite website
- [public-apis/public-apis](https://github.com/public-apis/public-apis)

#### Using APIs

Most APIs require authentication

- so they API developer knows who you are
- can charge you
- can limit access
- commonly via key or OAuth (both of which may be free)

All the APIs we use here are unauthenticated - this is to avoid the time of you all signing up

If your app requries authentication, it's usually done by passing in your credentials into the request (as a header)

```python
response = requests.get(url, auth=auth)
```

#### JSON strings

JSON (JavaScript Object Notation) is a:
- lightweight data-interchange format (text)
- easy for humans to read and write 
- easy for machines to parse and generate
- based on key, value pairs

You can think of the Python `dict` as JSON like:

- dict to json string: json.dumps(data)
- json string to dict: json.loads(data)

#### Using `open`

`open(path, mode)`
- use encoding = 'UTF-8'

Common values for the mode:
- `r` read
- `rb` read binary
- `w+` write (`+` to create file if it doesn't exist)
- `a` append

- Reading files with context management, with or use close()

#### REST APIs

[REST - Wiki](https://en.wikipedia.org/wiki/Representational_state_transfer)

REST is a set of constraints that allow **stateless communication of text data on the internet**

- REST = REpresentational State Transfer
- API = Application Programming Interface

REST
- communication of resources (located at URLs / URIs)
- requests for a resource are responded to with a text payload (HTML, JSON etc)
- these requests are made using HTTP (determines how messages are formatted, what actions (methods) can be taken)
- common HTTP methods are `GET` and `POST`

HTTP methods
- GET - retrieve information about the REST API resource
- POST - create a REST API resource
- PUT - update a REST API resource
- DELETE - delete a REST API resource or related component

RESTful APIs enable you to develop any kind of web application having all possible CRUD (create, retrieve, update, delete) operations

- can do anything we would want to do with a database

*Further reading*
- [Web Architecture 101](https://medium.com/storyblocks-engineering/web-architecture-101-a3224e126947) for more detail on how the web works

![](img\web_src.png)

- CDN = Content Delivery Network
- DNS =  domain name system
- H vs V scaling: horizontal scaling means that you scale by adding more machines into your pool of resources whereas “vertical” scaling means that you scale by adding more power (e.g., CPU, RAM) to an existing machine.
    - **In web development, you (almost) always want to scale horizontally because, to keep it simple, stuff breaks**
    - **your app is “fault tolerant.”**
    - **minimally couple different parts of your application backend**
- load balancers = They’re the magic sauce that makes scaling horizontally possible.


#### Example - sunrise API

Docs - https://sunrise-sunset.org/api

First we need to form the url
- use `?` to separate the API server name from the parameters for our request
- use `&` to separate the parameters from each other
- use `+` instead of space in the parameter

# getting sunrise & sunset for Berlin today
res = requests.get("https://api.sunrise-sunset.org/json?lat=52.5200&lng=13.4050")
data = res.json()
data

[item for item in dir(response) if '__' not in item]

#### NEW
```
from collections.abc import Iterable

for k, v in item.items():
    if isinstance(v, Iterable) and len(v) < 100:
        print(f'{k}: {v}')
```

#### String formating Date time
Here use `strptime` to convert the integer into a proper datetime:
- ([Python's strftime directives](http://strftime.org/) is very useful!)

#### Get images

```
url = 'https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png'
res = requests.get(url)
res.text[:100]

with open('./data/google-logo.png', 'wb') as fi:
    fi.write(res.content)

```


### Numpy

- why: list can have any data type, list has (head, length and type), numpy has constrains on type and will store on memory all together,
- broadcasting

#### 4. How to find the memory size of any array (★☆☆)
`hint: size, itemsize`

```python
Z = np.zeros((10,10))
print("%d bytes" % (Z.size * Z.itemsize))
```
#### 7. Create a vector with values ranging from 10 to 49 (★☆☆)
`hint: arange`

```python
Z = np.arange(10,50)
print
```

#### 8. Reverse a vector (first element becomes last) (★☆☆)
`hint: array[::-1]`

#### 9. Create a 3x3 matrix with values ranging from 0 to 8 (★☆☆)
`hint: reshape`

#### 11. Create a 3x3 identity matrix (★☆☆)
`hint: np.eye`

#### 12. Create a 3x3x3 array with random values (★☆☆)
`hint: np.random.random`

#### 13. Create a 10x10 array with random values and find the minimum and maximum values (★☆☆)
`hint: min, max, amin is for axis`


- np.full, np.full((3,5), 3.14)
- np.linspace(0, 1, 5)

- np.random.random((3,3)) # uniform distibution
- np.random.normal(0, 1, (3, 3)) # normal dis
- np.random.randint(0, 10, (3,3)) 

- np.zeros()
- np.ones()
- np.eye()
- np.empty()
- np.ones_like()

#### 15. Create a 2d array with 1 on the border and 0 inside (★☆☆)
`hint: array[1:-1, 1:-1]`

```python
Z = np.ones((10,10))
Z[1:-1,1:-1] = 0
print(Z)
```
# Using fancy indexing
Z[:, [0, -1]] = 0
Z[[0, -1], :] = 0
print(Z)
```

#### 16. How to add a border (filled with 0's) around an existing array? (★☆☆)
`hint: np.pad`

```python
Z = np.ones((5,5))
Z = np.pad(Z, pad_width=1, mode='constant', constant_values=0)
print(Z)
```


#### 18. Create a 5x5 matrix with values 1,2,3,4 just below the diagonal (★☆☆)
`hint: np.diag`

```python
Z = np.diag(1+np.arange(4),k=-1)
print(Z)
```

#### 20. Consider a (6,7,8) shape array, what is the index (x,y,z) of the 100th element? (★☆☆)
`hint: np.unravel_index`

```python
print(np.unravel_index(99,(6,7,8)))
```

#### 21. Create a checkerboard 8x8 matrix using the tile function (★☆☆)
`hint: np.tile`

```python
Z = np.tile( np.array([[0,1],[1,0]]), (4,4))
print(Z)
```

#### 24. Multiply a 5x3 matrix by a 3x2 matrix (real matrix product) (★☆☆)
`hint:`

```python
Z = np.dot(np.ones((5,3)), np.ones((3,2)))
print(Z)
```


#### 26. What is the output of the following script? (★☆☆)
```python
# Author: Jake VanderPlas

print(sum(range(5),-1))
from numpy import *
print(sum(range(5),-1))
```
#### 28. What are the result of the following expressions? (★☆☆)
```python
np.array(0) / np.array(0)
np.array(0) // np.array(0)
np.array([np.nan]).astype(int).astype(float)
```

nan
0
[-9.22337204e+18]

#### 30. How to find common values between two arrays? (★☆☆)
`hint: np.intersect1d`

```python
Z1 = np.random.randint(0,10,10)
Z2 = np.random.randint(0,10,10)
print(np.intersect1d(Z1,Z2))
```

#### 30. How to find common values between two arrays? (★☆☆)
`hint: np.intersect1d`

```python
Z1 = np.random.randint(0,10,10)
Z2 = np.random.randint(0,10,10)
print(np.intersect1d(Z1,Z2))
```

#### 32. Is the following expressions true? (★☆☆)
```python
np.sqrt(-1) == np.emath.sqrt(-1)
- For negative input elements, a complex value is returned (unlike numpy.sqrt which returns NaN).
```

#### 33. How to get the dates of yesterday, today and tomorrow? (★☆☆)
`hint: np.datetime64, np.timedelta64`

#### 34. How to get all the dates corresponding to the month of July 2016? (★★☆)
`hint: np.arange(dtype=datetime64['D'])`

```python
Z = np.arange('2016-07', '2016-08', dtype='datetime64[D]')
print(Z)
```


### Visualization
- D3js, low level 
- Dasg, streamlit 
- life server extention for vscode


### Probabiilty

- Probability vs Liklihood, the presenvce of condition, [link](https://youtu.be/pYxNSUDSFH4)
- Random variables, the outputs depond on random phenomena > probability theory

<img src="img\rndm_vr.png" style="width:200px;"/>

-probabiity distribution

<img src="img\prb_distrb.png" style="width:200px;"/>

- pribability distribution, continues variable, density function. Probability distribution:
  - continues, distribution function
  - discrete, mass function . 
- Marginal probability (can't go back to each single probability) vs conditional probability
- joint distribution, can't go back into signel distribution as marginal distribution.
  - chain rule 
- Probabality dependnece/Independence vs conditional indpendence
- expection, expected value > summation of all probabillity > for normal distribution equal to the mean
- Variance > how close are we to the expected value, same as spread
- covariance, > how much two item  
- Bionomial Distribution
- Bernouli destribution
- Multinoulli Distribution & Categorical distribution
- Gaussian distribution
- neumann's random generator
- Dirac distribution
- Nistaure of distribution
- Bayes Rule 
  
<img src="img\bayes.png" style="width:200px;"/>

 
<img src="img\fb_rain.png" style="width:200px;"/>

<img src="img\fb_rain_rp.png" style="width:200px;"/>

<img src="img\googl_bayse.png" style="width:200px;"/>

<img src="img\googl_rp.png" style="width:200px;"/>

<img src="img\mic.png" style="width:200px;"/>

<img src="img\mic_rp.png" style="width:200px;"/>

- Structured probabilistic. directed vs undirected
- directed vs directed probability chain
- Monto carlo, maximize the probability with structured probability
- Marcov chain, don't need to know the path, you are always in a state, and have the probability of going to a state    



### Stattistics
- Median is outlier resistance
- Why using varainace- population and variance-sample, (n-1) in sample to consider the bias and genedr one column instead of 2.

<img src="img\stat_variance.png" style="width:200px;"/>

-skewness and Kurtosis of the destribution

<img src="img\stat_dist.png" style="width:200px;"/>

- Permutation, n!
- K-permutation, n!/(n-k)!
- combination, P(n,k) = n!/(n-k)!/k!
- Pascal's triangle

<img src="img\stat_pascal.png" style="width:200px;"/>

#### Distribution

<img src="img\stat_dist_02.png" style="width:200px;"/>

- bionomial dist, need to have two, for unfairness it works onli with coin not dice as dice has more than two choice 

<img src="img\stat_dist_bion.png" style="width:200px;"/>


- Poisson Distribution, works for situation with binomial situation and number of occurance is little, good for extreme events.

<img src="img\stat_dist_poison.png" style="width:200px;"/>


<img src="img\stat_dist_tdist.png" style="width:200px;"/>


<img src="img\stat_dist_x2.png" style="width:200px;"/>


##### Functions,
- BIONOMIAL, scipy.stats.binom.pmf(k, n, p)
- POISSON, scipy.stats.poisson.pmf(k, mu)
- NORMAL, scipy.stats.norm.cdf(x, mu, sigma)
- T-DIST, scipy.stats.t.cdf(t_score, df), t_score = (x - mu) / (s / (df + 1) ** 0.5)
- x2, scipy.stats.chi2.cdf(x, df)


#### Sampling
- central limit theorem
<img src="img\stat_cent_limittheory.png" style="width:200px;"/>

- Confidence interval, at least 30
<img src="img\stat_conf_intrvl.png" style="width:200px;"/>

<img src="img\stat_conf_intrvl_02.png" style="width:200px;"/>

<img src="img\stat_resampling.png" style="width:200px;"/>

<img src="img\stat_bootstrap.png" style="width:200px;"/>


#### Hypothesis

- one sided, vs two sided hypothesis testing. Man taller than women vs MAn with diff height than women.
- P value, the integral of distribution

<img src="img\stat_bootstrapstat_AB_testing.png" style="width:200px;"/>


#### Model
- White noise
- error, estimation Blue, best linear unbiased estimateor

### DS-Fundamentals
- Cleaning data: quality, quantity, diversity, cardinality (No unique values), dimensionality, sparsity
- Data Charachter: Stationarity (iterating, new, environment, model effect on data), duplicates, class imbalance, Biased sampling
- test-validation, k-fault, the validation is moving
- bi-variant analysis, variable corolate to the variable or the target
- visualization:
  - correlation matrix
  - plot the target

- Data Encoding, sklearn, ctaegorical encoder
  - one-hot encoding, each category get a column and give 0, 1 to it, memory issue and sparse issue
  - category encoding, add 1,2,3 to each category
  - ordinal encoding, same as category but it consider the target value prediction in the ordering
  - frequency encoding
  - Binary encoding
  - Mean encoding, directly using the mean value kof the target value of the categories, target encoding

- NLP model and data, [link](https://becominghuman.ai/nlp-with-real-estate-advertisements-part-1-55200e0cb33c)    
    -  Tokenize the data
    -  Lemmatize the data, NLTK, spacy
    -  Get n-grams
    -  Visualize, histogram, word cloud
    -  Repeat
    -  TF-IDF Vectorization of Text Features, Text Frequency-Inverse Document Frequency
 - Sound data building, [link](https://medium.com/@data4help.contact/signal-processing-engine-sound-detection-a88a8fa48344)

#### Model Selection
- [more info](https://www.kdnuggets.com/2017/06/which-machine-learning-algorithm.html)
<img src="img\machine-learning-cheet-sheet.png" style="width:200px;"/>
<img src="img\dsf_models.png" style="width:200px;"/>
<img src="img\dsf_eval_01.png" style="width:200px;"/>
<img src="img\dsf_eval_02.png" style="width:200px;"/>
<img src="img\dsf_eval_03.png" style="width:200px;"/>

#### Deployment

<img src="img\dfs_deployment.png" style="width:200px;"/>

#### Packages
- ML flow,
- panda profiling, [link](https://pypi.org/project/pandas-profiling/)


### Databse
- practice i, https://sqlbolt.com/
- interview q : https://leetcode.com/problemset/all/, pramp, levels.fyi
- Data warehouse vs data lakes > datawarehouse supposed to be cleaner
- ACID, atomic, consistant, isolate durable needed for data warehouse not data lake
- ZOR, exlusive, place only for one
- Left table, is the first table, Right table is the second one with join. many sql don't have a right join.
- Building schema: snowflake (finer good for operational, more normalize) vs star(good for opration, more duplicate data).
- kafka: web service to transfer huge data, can be directly connected to warehouse or just to spark (Hadoop) or just dumping to data storage (e.g mango db)
- spark for graph: GRAPHx and kafka also work with it
- spark replacement: Snowflake.AWS Redshift.Azure Synapse.Google BigQuery.
- schema: relation of the tables with forgen key and data types
- primary key vs foreign key, primery is unique id but foreig key is for connecting

#### Normalization
- technique of reducing redundanty and duplicate data. 
- important for Insert, update, delete (annomally)
- important to think how we can denormalize the data > into different table
- 

  
<img src="img\db_lake.png" style="width:200px;"/>


- UUID, universal unique identifier, 128 bit > hasshing > SHA  hashing common but not secure longer
- Computational complexity, [link](https://stackoverflow.com/questions/14093816/computational-complexity-of-sql-query), [course](https://www.coursera.org/specializations/algorithms) recommended first lectures, e.g why order by makes the request slow (n rows * log of (n rows))
- Index optimization, 

### ETL
- assess tools: ease of use, scalability, security, documentation and support, advance fts, cost
- ETL vs ELT (extract transfer load), ELT new for small data with less sequrity
- OLAP, online analytical processing > optimize for reading
- OLTP, businuss use online transactional processing > optimize for write, update, edit
  
#### ETL + data Warehouse
- OLTP + ETL > OLAP
  - E, extracted from OLTP or RDBM 
- OLD ETL, hand cde in e.g. python
- NEw ETL, auto intergatre, integrate.io

#### ELT + Data lakes
- high-powered processing offered by modern, cloud-based data warehousing solutions


### AWS data engineering
- corpus data: text data
-  data sources like Kaggle or Reddit or Google data Search or the University of California Irvine machine learning repository.
-  scaling data: normalization, standardization (mean=0, sd=1 > more gaussian), bining



### DS fundamentls

#### Entropy
- [link](https://towardsdatascience.com/understanding-binary-cross-entropy-log-loss-a-visual-explanation-a3ac6025181a)
- all ds is using the cross entropy, Entropy is a measure of the randomness or unpredictability in a set of data.
- [entropy](https://www.khanacademy.org/computing/computer-science/informationtheory/moderninfotheory/v/information-entropy), measure of disorder.
  
  H(X) = - sum(p(A) log(p(A)))

- cross entropy,
  
  H(x) = - sum(p(A) log(Q(A)))

log2(1) = 0

- depth of three is log2 of number of branches
- sometime we use log on base e, and it behaves smoother
- equal probability of options has the max entropy

- Cross-entropy is a measure of the difference between two probability distributions. It is commonly used in machine learning to measure the dissimilarity between the predicted and actual distributions.
The cross-entropy H(P, Q) between two probability distributions P and Q is: H(P, Q) = - ∑ [ P(xi) * log2 Q(xi) ] for all i

- nagative log liklihood
- confusion matrix, 
  
<img src="img\confusion_matrix.png" style="width:200px;"/>
<img src="img\confusion_matrix_02.png" style="width:200px;"/>

accuracy = (TN + TP) / (all)
precision = (TP) / (TP + FP)
Recal = (TP )/(TP + FN)
f1_score = 2 * (recall + per) / (recall + per)

- the information, statistical mechanics
- Seth Loyed, informational theory complexity explore

- Softmax is used for multi-classification in logistic regression model (multivariate) whereas Sigmoid is used for binary classification in logistic regression model.

- covariate, same as feature
- Loss function needs to be defrentioable

#### Regression

- use cross validation set for hyper parameter training
- R2 score shows how good our model is compared to just using the mean value, close to 1 better
- if R2 is smaller in test than train > underfitting
- Basian works with a believe and it needs less data > [statistical rethinking](https://fehiepsi.github.io/rethinking-numpyro/), [online course](https://www.youtube.com/watch?v=BYUykHScxj8&list=PLDcUM9US4XdMROZ57-OIRtIK0aOynbgZN), book: the rule that never dies

[Lecture 8: Troubleshooting Deep Neural Networks - Full Stack Deep Learning - March 2019](https://youtu.be/GwGTwPcG0YM):


<img src="img\arch.png" style="width:200px;"/>

the parts of regularization
- lasso, l1, devided by absolut
- rich, l2 , squeared sum
- elastic net, has both l1+l2
- example, https://cs231n.github.io/neural-networks-case-study/

#### NLP
- use lime for explainabilty, [toturial](https://marcotcr.github.io/lime/tutorials/Lime%20-%20basic%20usage%2C%20two%20class%20case.html)

#### Tree
- Gradient boosting
  
#### PCA
- normaliaztion, sklearn standard scale
- use pd.sample(5) instead of heasd()
- changing number of PCA component form 2> 3 still 2 first component will stay the same (the computation is not stochastic) 
- sns-pairplot() good view of variable comparison, `sns.pairplot(penguins, hue="species")`
- sklarn.metrices.classification_report() returns F1 score, Recall and Percision

#### Suppervised
- avoid leackage, split data train, test, cv, normalized the train, save its transfomer and use it on test and cv to avoid the leakage

#### clustring
- pd.crosstab()
- pip install scikit-learn-extra
- k-miedoids

#### MLFLOW
- run command ` mlflow ui --backend-store-uri sqlite:///mlflow.db`
  
### Trees
- lower the varience beetter the split will be.
- Puning, contoled with the hyper parameter 
- sklearn.tree.plot_tree()

#### Criterion 
- entropy computation is just used for classification, never used for regresseion
- Gini:  Sum(p_{i}^2) gini more efficent in computetion than entropy, the probability is probability of two items being in the same class

#### Errors

### Error in Supervised learning

Error = bias + variance + noise
- noise = unmanageable
- variance = fitting to noise
- bias = missing signal

##### Bias
Bias is the difference between the average prediction of our model and the correct value which we are trying to predict. Model with high bias pays very little attention to the training data and oversimplifies the model(underfitting).

Bias are the simplifying assumptions made by a model to make the target function easier to learn.Generally, linear algorithms have a high bias making them fast to learn and easier to understand but generally less flexible. Examples of high-bias machine learning algorithms include: Linear Regression, Logistic Regression.

##### Variance
Variance is the variability of model prediction for a given data point or a value which tells us spread of our data. Model with high variance pays a lot of attention to training data and does not generalize on the data which it hasn’t seen before. As a result, such models perform very well on training data but has high error rates on test data. (Overfitting). 

Variance is the amount that the estimate of the target function will change if different training data was used.

High variance may result from an algorithm modeling the random noise in the training data


<img src="img\bias_variance_02.png" style="width:200px;"/>

##### Bias and Variance Tradeoff

The bias-variance tradeoff is a central problem in supervised learning. 

Ideally, one wants to choose a model that both accurately captures the regularities in its training data, but also generalizes well to unseen data. 

Unfortunately, it is typically impossible to do both simultaneously. High-variance learning methods may be able to represent their training set well but are at risk of overfitting to noisy or unrepresentative training data. 

In contrast, algorithms with high bias typically produce simpler models that may fail to capture important regularities (i.e. underfit) in the data. (Wikipedia)


<img src="img\bias_var_tradeoff.png" style="width:200px;"/>


These different ensemble methods tackle the tradeoff in different ways
- forests = high variance, low bias base learners
- boosting = low variance, high bias base learners

** The component / individual learner of the ensemble which are combined strategically is referred to as Base learners.


Further Reading: 
1. https://bit.ly/3Oi3cmH  (Overfitting and Underfitting With Machine Learning Algorithms)
2. https://bit.ly/3aLv4Su  (Understanding the Bias-Variance Tradeoff)


### Docker
- command cheat shit, [link](https://github.com/antahiap/dsr-db/blob/master/docker/1_Docker_Introduction/docker_cheat_sheet.sh)

- simple code to run flask app: `FLASK_APP=myapp:app flask run --host 0.0.0.0`

- then making the docker file, buiding it and runing it 

```
docker build -t myflaskapp .
docker run -it --rm -p 8989:8989 myflaskapp
```

- for production better to use the gunicorn, uswgi, fastapior uvicorn to run uwsgi server instead of production
- runing several servers: using dockerfile for each and then set them together with dockercomposer,dsr-db/databases/6_Redis_Exercise
 example`

- nginx, reverse proxy, used for security between public internet and the app
- docker composer a wrpper of severa docker
- kubernetes, for advance setup with many users same as docker composer but handles much more complex mixing of the containers and images

- cool cloring, use zsh and oh my zsh, [link](https://ohmyz.sh/), to check it the $SHELL should return /bin/zsh >rubyrussel > define the color code [theme](https://github.com/ohmyzsh/ohmyzsh/wiki/Themes)

### Unstructred DB, [nosql](https://github.com/antahiap/dsr-db/blob/master/databases/4_NoSQL/NoSQL_DSR_new.pdf)
- Appachee Avro (for Hadop large dataset), still used between kafka. python lib `fastavro`. file.avro, 10 times smaller than csv. 
 - needs an schema, stored in the file as a metadata

- .npy numpy dependence, on version
- pickle also python dpendence, not good for long time data storage
- orjson, faster than json reader

- Apache paraquet, 2-3 times smaller than avro and can read it with oanda, fastparaquet > best togo format


#### NoSQL
- NoSQL means not only SQL DB
- relational db
- document db, mangodb, coachdb, TerminusDB(bunch of json files)
- CAP theory, Consistancy, Availability, Performance > all don't go together



<img src="img\disadv_nosql.png" style="width:200px;"/>
<img src="img\rel_vs_col_db_wr.png" style="width:200px;"/>
<img src="img\rel_vs_col_db.png" style="width:200px;"/>


<img src="img\nosql_db.png" style="width:200px;"/>
<img src="img\db_exampl.png" style="width:200px;"/>


### Back Prop
- stocastic gradiant decent
- Relu vs sigmoid: computaton efficeny and issue with vanishing gradiant that computers don't have enough percisions and small numbers become zero in gradient computation.
- leaky relU: When the data has a lot of noise or outliers, Leaky ReLU can provide a non-zero output for negative input values, which can help to avoid discarding potentially important information, and thus perform better than ReLU in scenarios where the data has a lot of noise or outliers
- GELU, Gaussian Error Linear Unit,diffrentiable at zero, better for complex learning, e in-practice disadvantage of being much, much more complex to compute. it makes a difference between negative values that are close to zero.

- hyperparmeter tuning, [link](https://pytorch.org/tutorials/beginner/hyperparameter_tuning_tutorial.html)
- **Shatterin dataset** ability to perfectly classfy the data.

### Image Kernel
- explore article, [link](https://setosa.io/ev/image-kernels/)
- AI history, [link](https://people.idsia.ch/~juergen/deep-learning-history.html)
- Latest ML artucles, [DISTIL](https://distill.pub/)


# DeepL 
## PyTorch
- most of functions are the same as numpy and broad casting works (extending operation to all cells). 


### DEbug
```
class Network(nn.Module):
    def __init__(self):
        super().__init__()
        # Defining the layers, 128, 64, 10 units each
        self.fc1 = nn.Linear(784, 128)
        self.fc2 = nn.Linear(128, 64)
        # Output layer, 10 units - one for each digit
        self.fc3 = nn.Linear(64, 10)

    def forward(self, x):
        ''' Forward pass through the network, returns the output logits '''
        import pdb; pdb.set_trace()
        x = self.fc1(x)
        x = F.relu(x)
        x = self.fc2(x)
        x = F.relu(x)
        x = self.fc3(x)
        x = F.softmax(x, dim=1)

        return x

model = Network()
model
```

Commands for the python debugger:
```
ll - shows context
n - goes to the next line
c - runs to the next breakpoint
q - quits the debugger
```

more, (link)[https://www.youtube.com/watch?v=P0pIW5tJrRM]

### Computer vision
- 2012, Alex net, last big award
- 1989, MINST (digits)
- ResNet, it has sjortcot/skip connection to avoid gradient vanishing by adding the f(x) after calculationg the gradient. vanishing gradient comming from manipulation of small value in gradient calculation.
- in transfer learning, removing last year, > freezing parametr > replacing the last layer, part 8

#### Use-cases
- Image generation, 
- Image Segmentation
- Colorization
- Denoising
- Super sampling
- Image captioning-imag2 text
- Imafe2vec
- Object identification
- Object detetion
- object recognition
- object classification
- pose detection, use LSTM for classification or more data use transformers

#### Methods
##### Image generation
- GANs,  to network 1, Adversarial/discrimination (fake no fake) 2, generator
- Defusion models, denoiser-autoencoder (data: img+ added noise, image)
- Variational Autoencoder(encoder-decoder: in and out same image), generate normal distribution from latent space representation.
- Wavenet, first used for audio processing
- CNN, the filter is also learned
- VIT, vision transformer.
- Few shot learning, handful of data
- zero-shot learning, NN with seeing no example


#### Improving performance-transfer learning
Architecture: filter, kernel size, sequence, dropout, FC layer size
data: input image size, augmentation, new data

- Augmentation: yes/no
- Dropout: yes/no, how much
- FC size
- which pretrained network, Other Models: [link](https://keras.io/api/applications/)

- Dropout: dont freeze wait and biase, some of the output values are set to zero
- Increasing image shape, add computation due to change of FC layers size
- number of parameters: filter, kernelw-h, 3rd deimention of the image
- limit of arcitectures, vaishing gradient, adding residual connection.

#### Audio Processing
Digital Signal processing, audio or picture




```
# Freeze parameters so we don't backprop through them
for param in model.parameters():
    param.requires_grad = False

from collections import OrderedDict
fc = nn.Sequential(OrderedDict([
                          ('fc1', nn.Linear(512, 500)),
                          ('relu', nn.ReLU()),
                          ('fc2', nn.Linear(500, 2)),
                          ('output', nn.LogSoftmax(dim=1))
                          ]))
    
model.fc = fc
```
- difference of segmentation and classificiation , labaling is more costly and has localization
- one, one convolution, resizing in z dierection and adding non-linearity
- one-cyle policy, having differnt learning rate between batches


<img src="img\cyclc_lrn_rt.png" style="width:200px;"/>
- in each epoch add augmentation on training set but not to the validation set
- closer to the end of the network, higher learning rate
- Hessian, 2nd deriavtive
- Jacobian, 1st derivative

### Data split
- 60-20-20, train-validation-test
- to make the ratio of classes equal in th data set use stratified, [link](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.StratifiedShuffleSplit.html)
- if the number of images is not possible to startify, you can calibrate the, [link](https://machinelearningmastery.com/threshold-moving-for-imbalanced-classification/)

#### FastAI
- transferlearning, freezing the parameters 
```
learn = vision_learner(dls, resnet34, metrics=error_rate)
```

## Severless
### AWS
- lambda: do the computation
- couldwatch: assess the computation
- Identity, acess mngmn, IAM: who or what can access services and resources
- CloudFormation: model, provision, and manage AWS and third-party resources
- Mngmnt Consule
- Polly: uses deep learning technologies to synthesize natural-sounding human speech
- Commanf line interface CLI
- Budgets
- Tools and SDKs
- Simple Storage service: images, ...

### Lambda
- 

#### user
- make user group > administrator
- make user
- make ssh key, access key >cli command


## Portfolio Project

- kg+llm, [link](https://colab.research.google.com/drive/1G6pcR0pXvSkdMQlAK_P-IrYgo-_staxd?usp=sharing#scrollTo=5mHzFSTbPbWf)


# Reinforcement Learning
- Terminology: 
 - what is the situation: State, 
 - what are the possible options: Action space
 - What are the consequences of each environment: Environment
  - how rewarding / costly: reward
  - where do you end up after: next state
 - Policy: what we are learn, learning state to action



# Time series
- autoregressive model (same as NLP) works the best, but the difference is that :
1- the pattern is not catchable for human, so hard to judge the result (hard to describe)
2- it is not same pattern, the pattern can totally change

- hardest to bit, null-baseline, predcting tomorrow based on today
- model overview, may 2023, slide 7
- Autocorrelation = correlation with itself in the past

- flat line (sine curve), has no trend, ARIMA method takes away the trend to be stationary. Trended is if mean is changing by time.
- Metrices: slide 84
- Review question: slide 100-104

## Analyses:
- Anomaly detection
- Forcasting
- classification

- keywords: Trend, Seasonality, Residual aka Noise, Stationarity, Autoregressive, Autocorrelation and Partial Autocorrelation, Differencing, Backtesting, Exogenous variable, Look-ahead problem, Multivariate vs univariate, Recursive forecasting, Exponential moving average, Exponential smoothing, LSTM, ARIMA

## Inputation
- NAN: always consider the lag values, never look in the future, not future influcing the past, just te past affecting the future. 
- anomalies, defining a percentage or a window in a past and if above that the use the window values for replacing that value

## Links
- Scipy overview, [link](https://www.youtube.com/watch?v=v5ijNXvlC5A)
- kaggle, [link](https://www.kaggle.com/learn/time-series)
- numer.ai, anonymus kaggle for stock market
- hugging face, [link](https://huggingface.co/blog/time-series-transformers)
- DARTS
- online course, [link](https://online.stat.psu.edu/stat510/lesson/1)
- PROPHET, [link](https://facebook.github.io/prophet/docs/quick_start.html#python-api)
- KATS, [link](https://facebookresearch.github.io/Kats/)


# Interview
## Lesson learned
- Look into classical computer science problem
- Give 10-20% time to analyse the problem before solving it
- Don't share unnecessary input (start day, different interests and so on)
- Don't get stuck in the emotional challenges of waiting to hear back.
- Do research on the type of their peoblem, question what you assume you know