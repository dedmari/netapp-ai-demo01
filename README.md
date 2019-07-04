# NetApp Snaphot for ML Version Control
NetApp snapshot is sophisticated mechanism to capture the point-in-time versions of the data and trained models and logs, which makes it a perfect fit for Machine Learning versioning. Snapshots don't create new copies, but always refers to the original data, hence don’t consume any extra space and are extremely fast (~1sec for PB scale data). 

By design, snapshots only capture the incrementing file changes, that means if data is updated, deleted or inserted, only new changes are recorded. It makes data versioning very efficient when we are dealing with large amount of data. Snapshots keep track of origin and changes associated with data throughout the process, which makes the whole process of ML explainable and data provenance compliant.

ML versioning using NetApp snapshots makes sharing and collaboration between teams easy, as it is the part of the underlined data platform. Nothing needs to be re-engineered, as with the help of inbuilt CLI and API support, it can be integrated with any code versioning platform, like Git (this demo) and automation tools, such as Jenkins. Also, it works out-of-the-box with multiple Machine Learning / Deep Learning frameworks e.g. TensorFlow, PyTorch etc. generating models with different file formats e.g. h5, pickle etc.
___

## Demo Description

As most of the Machine Learning researchers and practitioners are using Git for the versioning of code, we have used GitHub and integrated it with NetApp snapshots for Machine Learning versioning. In this demo, we trained a simple Deep Neural Network on a MNIST dataset and created versions of trained models and respected code. Whenever code is pushed to GitHub, the state of trained models is captured and synched using the snapshots. Snapshots have the same identifier as the Git commit ID, which links the state of code with the associated trained models.

The concept makes it easy to share and collaborate with others, normal git pull is used to get the latest complete Machine Learning version, and not just code. There is no more need of manually copying the data. NetApp snapshots take care of it.

In case, we want to roll-back to the previous best-known model, we just need to pull the specific version from the git, and associated models will be automatically updated. The same concept holds true when trained models are accidentally deleted and needs to be recovered.

If you interested to learn more than don't miss to checkout the demo video. [demo credit: Muneer Ahmad Dedmari, NetApp and Steve Guhr, NetApp] 
___

## Using hooks for versioning

Replace .git/hooks folder with versioning_hooks/hooks in the local repository.

In pre-push hook, you can change configuration settings as per your requirement (e.g. vserver, username etc.) needed for snapshot.
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

For demo video and blog please visit [link](https://www.linkedin.com/pulse/simplify-machine-learning-version-control-muneer-ahmad-dedmari/)


Repository maintained by Muneer Ahmad Dedmari
