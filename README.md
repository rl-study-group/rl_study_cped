# CPED: Constrained Policy Optimization with Explicit Behavior Density For Offline Reinforcement Learning 
_________________

This is the official implementation of the offline RL method CPED, which appears in the research paper ''Constrained Policy Optimization with Explicit Behavior Density For Offline Reinforcement Learnig''.

Constrained Policy Optimization with Explicit Behavior Density For Offline Reinforcement Learnig (CPED), is an  offline RL method that utilizes the flow-GAN method to explicitly esimate the behavior density and allows offline exploration within the estimted region.


# Getting Started
_________________
Before running the CPED program, some prerequisite packages and environments need to be installed, including the rlkit (https://github.com/vitchyr/rlkit/) and D4RL environment (https://github.com/rail-berkeley/d4rl).


Please use the following command to run the CPED program:

> python examples/flow_hdf5_d4rl.py --env='halfcheetah-medium-v2' --policy\_lr=1e-4 --model_type='nice' 

where *env* refers to a d4rl environment, *policy_lr* is the policy learning rate, *model_type* is the type of flow-gan model.

# Note
---------
* Due to the tight timeline for organizing the CPED code and uploading to github, some test code hasn't been completely removed. We will make an effort to tidy up all the code as soon as possible.






