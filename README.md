# Model Template v0.1

![Python](https://img.shields.io/badge/python-3.x-blue.svg)
![MIT license](https://img.shields.io/badge/License-MIT-green.svg)

> You should think of GitHub as your modern research journal.
> This repository template is intended to help quick start the model building process.
> Every new model archecture should have its own repository.
> When you are happy with the archecture, evaluate the performance on your dataset.

> This repository should _NOT_ house your academic paper.
> If the model archecture works well, make a [paper repo](https://github.com/MindMimicLabs/paper-template).
> The paper repo should have a script under `~/code` that takes your data source, preprocesses it, and runs the model, saving the results to `~/results`.
> This way others can apply your model to their dataset and more easly: (1) reproduce your work and (2).

> When someone else uses your work, what academic paper should they cite.

{{Repo Name}} is the code embodyment of the model archecture described in [{{Paper Name}}](https://github.com/xxx/yyy).
It is in a seperate repo from the paper to facilate both code reuse and academic compareson.
If you use this network layout in your paper, please use the citation as described in the [references.bib](./references.bib) file.

## Enviormental Setup

TensorFlow networks are notorsully difficult to run when the local enviroment is different than what is expected.
Small differences in the versions of Python/CUDA/cuDNN can have large impacts.
If you are having problems getting the network to _run_ at all, consider setting up your local enviroment to have the following versions:

> When you are finished checking in the initial version of your archecture, make sure to update the versions below 

* [CUDA](https://developer.nvidia.com/cuda-toolkit) (10.1)
* [cuDNN](https://developer.nvidia.com/cudnn) (7.6.5 for CUDA 10.1)
* [Python](https://www.python.org/downloads/) (3.8.4)
* [tensorflow](https://www.tensorflow.org/install) (2.2.0)

## Scripts

Below are the scripts needed to train the classifaction model.
It is expected that any preprocessing steps (I.E. Stopword removal, stemming, ...) the corpus needs should already be applied before the scripts below are run.
The corpus is expected in a [specific folder format](./#corpus-folder).
A [state folder](./#state-folder) is used to keep state between steps.
The [academic boilerplate](./#academic-boilerplate) describing the process is provided as a starting point.
All paths can changed as desired.
PowerShell is used as an overall scripting language to allow the process to be paused easly.

> Remember to copy these steps to your processing script in your academic paper.

01. Open a PowerShell prompt
02. Change into the `~/code` folder
03. Copy the [config](./code/config.yml) file to the state folder
    ```{ps1}
    copy config.yml d:/state/config.yml
    ```
04. Update the config as desired
05. Tokenize the corpus.
    * Remember to cleanup the destenation first.
    ```{ps1}
    Remove-Item "d:/corpus_tok/*.*"
    python tokenize_corpus.py -in d:/corpus_raw -out d:/corpus_tok
    ```
06. Capture the k-folds for reproducability
    ```{ps1}
    python create_corpus_folds.py -in d:/corpus_tok -s d:/state
    ```
07. Create the model.
    ```{ps1}
    python create_model.py -s d:/state
    ```
08. Hyper-tune the model.
    1. Cleanup the working directories
    2. Extract the hyper-tuning subsample
    2. Run the hyper-tuning script
    ```{ps1}
    Remove-Item "d:/corpus_train/*.*"
    Remove-Item "d:/corpus_test/*.*"
    python extract_fold.py -in d:/corpus_tok -out d:/corpus_train -sub d:/state/sub/hypertune.train.csv
    python extract_fold.py -in d:/corpus_tok -out d:/corpus_test -sub d:/state/sub/hypertune.test.csv
    python hyper_tune_model.py -train d:/corpus_train -test d:/corpus_test -s d:/state
    ```
09. Train the model
    For each fold:
    1. Cleanup the working directory
    2. Extract the fold
    3. Train the model
    4. Validate model
    ```{ps1}
    $folds = 10 #get from config.yml
    for($i = 0; $i -lt $folds; $i++) {
       Remove-Item "d:/corpus_train/*.*"
       Remove-Item "d:/corpus_test/*.*"
       python extract_fold.py-in d:/corpus_tok -out d:/corpus_train -sub d:/state/sub/kfold.$i.train.csv
       python extract_fold.py-in d:/corpus_tok -out d:/corpus_test -sub d:/state/sub/kfold.$i.test.csv
       python train_model.py -in d:/corpus_train -s d:/state      
       python validate_model.py -in d:/corpus_test -s d:/state
    }
    ```
10. Collect the overall results.

## Corpus Folder

The corpus is expected to be in the folder format below.
Documents are expected to be in `.txt` format, 1 document per file. 
This layout allows `N` levels of clasifaction, without the need for an external control file.

* Root (`d:/corpus`)
  * Class 1 (`d:/corpus/1`)
  * Class 2 (`d:/corpus/2`)
  * ...
  * Class N (`d:/corpus/#`)

## State Folder

In order to allow for the process to be stoped and re-started a state folder is used.
Reproduceability by design is enabled using a subsample folder that captures the random folds.

* Root (`d:/state`)
  * Config (`d:/state/config.yml`)
  * Subsample
    * Hyper-tuning training split (`d:/state/sub/hypertune.train.csv`)
    * Hyper-tuning test split (`d:/state/sub/hypertune.test.csv`)
    * K-fold training (`d:/state/sub/kfold.#.train.csv`)
    * K-fold test (`d:/state/sub/kfold.#.test.csv`)
  * Model weights (`d:/state/weights`)
  * Validation results (`d:/state/results`)

## Academic boilerplate

Below is the suggested text to add to the Methods and Materials section of your paper when using this arectiture.

> After preprocessing, the corpus was then tokenized.
> Hyper-tuning used a 5% sub-sample evenly distributed accross each class using a training/validation split of 80%/20%.
> The hyper-tuning sample was pre-calculated to aid in reproducability.
> Model building used a 10-fold cross-validation using a training/validation split of 80%/20%.
> Folds for cross-validation were pre-calculated to aid in reproducability.
