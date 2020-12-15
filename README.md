# CourseProject

This project is about reproducing the results for latent aspect analysis.



The source code is from the paper provided with the data.

## Software installation

first we should install the nltk tool using the command:

```
import nltk
nltk.download()
```

The project will be base on a mix of java and python


## run the project

first we should generator the key work for our latent aspect analysis by using the code

```
python key_generator.py
```

the stopwords.txt is for the stop work that will like occur in all kinds of documents. Therefore we ignore the exsitence of the those words to produce a better keyword collection.

After that, download the NLP from https://opennlp.apache.org/ to install and put the enviromental variable to path to the folder you installed


Next, we should using java platform to run the analyse.java under src and the final result of the hotel data will be listed under vectors folder in vector_CHI_4000.dat


##

presentation vedio : https://mediaspace.illinois.edu/media/1_64gzbvp4



## Sources


![Review data sets for "Latent Aspect Rating Analysis](http://sifaka.cs.uiuc.edu/~wang296/Data/index.html)
![Welcome to Hongning Wang's Homepage!](http://sifaka.cs.uiuc.edu/~wang296/)
![virginia](https://www.cs.virginia.edu/~hw5x/paper/p618.pdf)
