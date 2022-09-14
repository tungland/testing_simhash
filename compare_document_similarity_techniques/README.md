# README

## Collect text samples

To test behaviour of simhash similarity, we will compare the behaviour of simhash comparison to other similarity metrics

- Jaccard
- TF-IDF / BoW ??
- Doc2vec
- Bert

TODOs
* Link to ids seem to be wrong for some of the pipelines
* d2v prob wrong
* check all 
* Increase sample size


| Tests 23.03             | Top 20 Jacc dist            |
|---------------------|----------------------|
| simhash - simhash : | 1.0                  |
| simhash - jacc :    | 0.043478260869565216 |
| simhash - tfidf :   | 0.1                  |
| simhash - d2v :     | 0.0                  |
| simhash - sbert :   | 0.09090909090909091  |
| jacc - simhash :    | 0.043478260869565216 |
| jacc - jacc :       | 1.0                  |
| jacc - tfidf :      | 0.5384615384615384   |
| jacc - d2v :        | 0.0                  |
| jacc - sbert :      | 0.5714285714285714   |
| tfidf - simhash :   | 0.1                  |
| tfidf - jacc :      | 0.5384615384615384   |
| tfidf - tfidf :     | 1.0                  |
| tfidf - d2v :       | 0.0                  |
| tfidf - sbert :     | 0.5384615384615384   |
| d2v - simhash :     | 0.0                  |
| d2v - jacc :        | 0.0                  |
| d2v - tfidf :       | 0.0                  |
| d2v - d2v :         | 1.0                  |
| d2v - sbert :       | 0.0                  |
| sbert - simhash :   | 0.09090909090909091  |
| sbert - jacc :      | 0.5714285714285714   |
| sbert - tfidf :     | 0.5384615384615384   |
| sbert - d2v :       | 0.0                  |
| sbert - sbert :     | 1.0                  |
