# NetApp Snaphot for ML Version Control


___

## Using hooks for versioning
Replace .git/hooks folder with versioning_hooks/hooks in the local repository
___

## Setting up environment
Install pipenv:

    pip install pipenv

Inside project directory, install project dependencies:

    pipenv install .
  
Activate environment:

    pipenv shell
___

## Training MNIST model

    python train_mnist.py
  
Trained model will be saved in models directory and upon git push, model version associated with commit ID is stored in models.version directory.
