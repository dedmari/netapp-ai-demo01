# NetApp Snaphot for ML Version Control


___

## Using hooks for versioning
Replace .git/hooks with versioning_hooks/hooks in the local repository
___

## Setting up environment
Install pipenv:

    pip install pipenv

Inside project directory:

    pipenv install .
  
Activate environment:

    pipenv shell
___

## Training MNIST model

    python train_mnist.py
  
Trained model will be saved in models directory
