# Benchmarking biorXiv

## General

This is the end-to-end benchmarking result for GROBID version **0.7.1** against the `bioRxiv` test set (`biorxiv-10k-test-2000`), see the [End-to-end evaluation](End-to-end-evaluation.md) page for explanations and for reproducing this evaluation. 

The following end-to-end results are using:
- **BidLSTM-CRF-FEATURES** as sequence labeling for the citation model
- **CRF Wapiti** as sequence labelling engine for all other models. 

Header extractions are consolidated by default with [biblio-glutton](https://github.com/kermitt2/biblio-glutton) service (the results with CrossRef REST API as consolidation service should be similar but much slower). 

Other versions of these benchmarks with variants and **Deep Learning models** (e.g. newer master snapshots) are available [here](https://github.com/kermitt2/grobid/tree/master/grobid-trainer/doc). Note that Deep Learning models might provide higher accuracy, but at the cost of slower runtime and more expensive CPU/GPU resources. 

Evaluation on 1999 PDF preprints out of 2000 (1 PDF parsing "too many blocks" failure).

Runtime for processing 2000 PDF: **1169s** (1,71 PDF per second) on Ubuntu 16.04, 4 CPU i7-4790K (8 threads), 16GB RAM (workstation bought in 2015 for 1600 euros) and with a GeForce GTX 1050 Ti GPU.

## Header metadata 

Evaluation on 1999 random PDF files out of 2000 PDF (ratio 1.0).

#### Strict Matching (exact matches)

**Field-level results**

| label            |  precision |   recall  |     f1     | support |
|---               |---         |---        |---         |---      |
| abstract | 2.24 | 2.16 | 2.2 | 1989 |
| authors | 82.84 | 81.93 | 82.39 | 1998 |
| first_author | 96.46 | 95.49 | 95.97 | 1996 |
| keywords | 59.84 | 60.91 | 60.37 | 839 |
| title | 80.59 | 78.09 | 79.32 | 1999 |
|                  |            |           |            |         |
| **all fields (micro avg.)** | **65.3** | **64.14** | **64.71** | 8821 |
| all fields (macro avg.) | 64.39 | 63.72 | 64.05 | 8821 |



#### Soft Matching (ignoring punctuation, case and space characters mismatches)

**Field-level results**

| label            |  precision |   recall  |     f1     | support |
|---               |---         |---        |---         |---      |
| abstract | 57.44 | 55.51 | 56.46 | 1989 |
| authors | 83.3 | 82.38 | 82.84 | 1998 |
| first_author | 96.61 | 95.64 | 96.12 | 1996 |
| keywords | 65.69 | 66.87 | 66.27 | 839 |
| title | 84.62 | 81.99 | 83.28 | 1999 |
|                  |            |           |            |         |
| **all fields (micro avg.)** | **79.16** | **77.76** | **78.45** | 8821 |
| all fields (macro avg.) | 77.53 | 76.48 | 76.99 | 8821 |



#### Levenshtein Matching (Minimum Levenshtein distance at 0.8)

**Field-level results**

| label            |  precision |   recall  |     f1     | support |
|---               |---         |---        |---         |---      |
| abstract | 76.95 | 74.36 | 75.63 | 1989 |
| authors | 91.5 | 90.49 | 90.99 | 1998 |
| first_author | 96.91 | 95.94 | 96.42 | 1996 |
| keywords | 78.22 | 79.62 | 78.91 | 839 |
| title | 91.48 | 88.64 | 90.04 | 1999 |
|                  |            |           |            |         |
| **all fields (micro avg.)** | **88.19** | **86.63** | **87.41** | 8821 |
| all fields (macro avg.) | 87.01 | 85.81 | 86.4 | 8821 |



#### Ratcliff/Obershelp Matching (Minimum Ratcliff/Obershelp similarity at 0.95)

**Field-level results**

| label            |  precision |   recall  |     f1     | support |
|---               |---         |---        |---         |---      |
| abstract | 73.93 | 71.44 | 72.67 | 1989 |
| authors | 86.99 | 86.04 | 86.51 | 1998 |
| first_author | 96.46 | 95.49 | 95.97 | 1996 |
| keywords | 71.19 | 72.47 | 71.83 | 839 |
| title | 89.21 | 86.44 | 87.8 | 1999 |
|                  |            |           |            |         |
| **all fields (micro avg.)** | **85.19** | **83.69** | **84.43** | 8821 |
| all fields (macro avg.) | 83.56 | 82.38 | 82.96 | 8821 |


#### Instance-level results

```
Total expected instances:   1999
Total correct instances:    34 (strict) 
Total correct instances:    698 (soft) 
Total correct instances:    1128 (Levenshtein) 
Total correct instances:    982 (ObservedRatcliffObershelp) 

Instance-level recall:  1.7 (strict) 
Instance-level recall:  34.92   (soft) 
Instance-level recall:  56.43   (Levenshtein) 
Instance-level recall:  49.12   (RatcliffObershelp) 
```


## Citation metadata 

Evaluation on 1999 random PDF files out of 2000 PDF (ratio 1.0).

#### Strict Matching (exact matches)

**Field-level results**

| label            |  precision |   recall  |     f1     | support |
|---               |---         |---        |---         |---      |
| authors | 86.88 | 78.41 | 82.43 | 97138 |
| date | 91.28 | 83.07 | 86.98 | 97585 |
| doi | 72.95 | 80.77 | 76.66 | 16893 |
| first_author | 93.57 | 84.4 | 88.75 | 97138 |
| inTitle | 81.95 | 77.43 | 79.63 | 96384 |
| issue | 93.99 | 83.23 | 88.29 | 30282 |
| page | 96.32 | 78.67 | 86.6 | 88558 |
| pmcid | 63.67 | 64.06 | 63.87 | 807 |
| pmid | 67.66 | 75.06 | 71.17 | 2093 |
| title | 84.46 | 80.78 | 82.58 | 92423 |
| volume | 95.55 | 92.71 | 94.11 | 87671 |
|                  |            |           |            |         |
| **all fields (micro avg.)** | **89.35** | **82.09** | **85.57** | 706972 |
| all fields (macro avg.) | 84.39 | 79.87 | 81.91 | 706972 |



#### Soft Matching (ignoring punctuation, case and space characters mismatches)

**Field-level results**

| label            |  precision |   recall  |     f1     | support |
|---               |---         |---        |---         |---      |
| authors | 88.14 | 79.55 | 83.63 | 97138 |
| date | 91.28 | 83.07 | 86.98 | 97585 |
| doi | 77.52 | 85.83 | 81.47 | 16893 |
| first_author | 94.04 | 84.82 | 89.19 | 97138 |
| inTitle | 91.45 | 86.4 | 88.85 | 96384 |
| issue | 93.99 | 83.23 | 88.29 | 30282 |
| page | 96.32 | 78.67 | 86.6 | 88558 |
| pmcid | 74.14 | 74.6 | 74.37 | 807 |
| pmid | 72.05 | 79.93 | 75.79 | 2093 |
| title | 92.68 | 88.64 | 90.61 | 92423 |
| volume | 95.55 | 92.71 | 94.11 | 87671 |
|                  |            |           |            |         |
| **all fields (micro avg.)** | **92.19** | **84.71** | **88.29** | 706972 |
| all fields (macro avg.) | 87.92 | 83.41 | 85.44 | 706972 |



#### Levenshtein Matching (Minimum Levenshtein distance at 0.8)

**Field-level results**

| label            |  precision |   recall  |     f1     | support |
|---               |---         |---        |---         |---      |
| authors | 92.86 | 83.81 | 88.1 | 97138 |
| date | 91.28 | 83.07 | 86.98 | 97585 |
| doi | 79.95 | 88.52 | 84.02 | 16893 |
| first_author | 94.18 | 84.95 | 89.33 | 97138 |
| inTitle | 92.41 | 87.31 | 89.79 | 96384 |
| issue | 93.99 | 83.23 | 88.29 | 30282 |
| page | 96.32 | 78.67 | 86.6 | 88558 |
| pmcid | 74.14 | 74.6 | 74.37 | 807 |
| pmid | 72.09 | 79.98 | 75.83 | 2093 |
| title | 95.32 | 91.17 | 93.2 | 92423 |
| volume | 95.55 | 92.71 | 94.11 | 87671 |
|                  |            |           |            |         |
| **all fields (micro avg.)** | **93.41** | **85.83** | **89.46** | 706972 |
| all fields (macro avg.) | 88.92 | 84.37 | 86.42 | 706972 |


#### Ratcliff/Obershelp Matching (Minimum Ratcliff/Obershelp similarity at 0.95)

**Field-level results**

| label            |  precision |   recall  |     f1     | support |
|---               |---         |---        |---         |---      |
| authors | 89.99 | 81.22 | 85.38 | 97138 |
| date | 91.28 | 83.07 | 86.98 | 97585 |
| doi | 79.15 | 87.64 | 83.18 | 16893 |
| first_author | 93.62 | 84.44 | 88.79 | 97138 |
| inTitle | 90.13 | 85.16 | 87.58 | 96384 |
| issue | 93.99 | 83.23 | 88.29 | 30282 |
| page | 96.32 | 78.67 | 86.6 | 88558 |
| pmcid | 63.67 | 64.06 | 63.87 | 807 |
| pmid | 67.66 | 75.06 | 71.17 | 2093 |
| title | 94.6 | 90.48 | 92.49 | 92423 |
| volume | 95.55 | 92.71 | 94.11 | 87671 |
|                  |            |           |            |         |
| **all fields (micro avg.)** | **92.48** | **84.97** | **88.57** | 706972 |
| all fields (macro avg.) | 86.91 | 82.34 | 84.4 | 706972 |


#### Instance-level results

```
Total expected instances:       98753
Total extracted instances:      103537
Total correct instances:        41366 (strict) 
Total correct instances:        51943 (soft) 
Total correct instances:        55911 (Levenshtein) 
Total correct instances:        52865 (RatcliffObershelp) 

Instance-level precision:   39.95 (strict) 
Instance-level precision:   50.17 (soft) 
Instance-level precision:   54 (Levenshtein) 
Instance-level precision:   51.06 (RatcliffObershelp) 

Instance-level recall:  41.89   (strict) 
Instance-level recall:  52.6    (soft) 
Instance-level recall:  56.62   (Levenshtein) 
Instance-level recall:  53.53   (RatcliffObershelp) 

Instance-level f-score: 40.9 (strict) 
Instance-level f-score: 51.35 (soft) 
Instance-level f-score: 55.28 (Levenshtein) 
Instance-level f-score: 52.27 (RatcliffObershelp) 

Matching 1 :    75743

Matching 2 :    4069

Matching 3 :    6070

Matching 4 :    2250

Total matches : 88132
```


#### Citation context resolution
```

Total expected references:   98751 - 49.4 references per article
Total predicted references:      103537 - 51.79 references per article

Total expected citation contexts:    142796 - 71.43 citation contexts per article
Total predicted citation contexts:   133903 - 66.98 citation contexts per article

Total correct predicted citation contexts:   110798 - 55.43 citation contexts per article
Total wrong predicted citation contexts:     23105 (wrong callout matching, callout missing in NLM, or matching with a bib. ref. not aligned with a bib.ref. in NLM)

Precision citation contexts:     82.74
Recall citation contexts:    77.59
fscore citation contexts:    80.09
```

## Fulltext structures 

Fulltext structure contents are complicated to capture from JATS NLM files. They are often normalized and different from the actual PDF content and are can be inconsistent from one document to another. The scores of the following metrics are thus not very meaningful in absolute term, in particular for the strict matching (textual content of the srtructure can be very long). As relative values for comparing different models, they seem however useful.


Evaluation on 1999 random PDF files out of 2000 PDF (ratio 1.0).

#### Strict Matching (exact matches)

**Field-level results**

| label            |  precision |   recall  |     f1     | support |
|---               |---         |---        |---         |---      |
| figure_title | 4.12 | 3.57 | 3.83 | 13162 |
| reference_citation | 71.05 | 70.76 | 70.9 | 147404 |
| reference_figure | 73.73 | 65.94 | 69.61 | 47965 |
| reference_table | 48.14 | 80.66 | 60.29 | 5951 |
| section_title | 71.29 | 71.05 | 71.17 | 32384 |
| table_title | 4.54 | 4.09 | 4.3 | 2957 |
|                  |            |           |            |         |
| **all fields (micro avg.)** | **66.8** | **65.78** | **66.28** | 249823 |
| all fields (macro avg.) | 45.48 | 49.34 | 46.69 | 249823 |



#### Soft Matching (ignoring punctuation, case and space characters mismatches)

**Field-level results**

| label            |  precision |   recall  |     f1     | support |
|---               |---         |---        |---         |---      |
| figure_title | 67.36 | 58.33 | 62.52 | 13162 |
| reference_citation | 83.01 | 82.67 | 82.84 | 147404 |
| reference_figure | 74.42 | 66.56 | 70.27 | 47965 |
| reference_table | 48.57 | 81.38 | 60.83 | 5951 |
| section_title | 75.06 | 74.81 | 74.93 | 32384 |
| table_title | 50.69 | 45.72 | 48.08 | 2957 |
|                  |            |           |            |         |
| **all fields (micro avg.)** | **78** | **76.81** | **77.4** | 249823 |
| all fields (macro avg.) | 66.52 | 68.24 | 66.58 | 249823 |

Evaluation metrics produced in 1144.846 seconds
