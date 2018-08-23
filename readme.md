# What do the Dirichlet Process and the Gaussian Process in common?

As soon as you start in non parametric Bayesian topics, you'll encounter funny names. Stick breaking process, Chinese restaurant process, Indian buffet process. The names that you'll hear most often, however, will be the Dirichlet and Gaussian process. In this small project, we set out to explore what makes these processes so ubiquitous. 

# How do we think about a process?
Wait, we know the Gaussian _distribution_ and the Dirichlet _distribution_. Why change that name to a process? Well, a _distribution_ specifies the behaviour of a random variable. For example, the Poisson distribution specifies the behaviour of a random variable of waiting times. In other words, consider the waiting time a random variable. Then, the Poisson distribution will help to characterise this behavior. Now, a _process_ specifies the behavior of a sequence of random variables. For example, the Poisson process specifies the behaviour of a sequence of random variables of waiting times. In other words, consider the waiting time a random variable. Then, the Poisson process will characterise a sequence of waiting times according to this behavior.

# What makes the GP and DP so special?
GP = Gaussian process
DP = Dirichlet process

Both the Gaussian distribution and the Dirichlet distribution have a special property. Each property enables us to play with its process

  * For the Gaussian distribution, we have the _marginalisation property_
  * For the Dirichlet distribution, we have the _aggregation property_

## Marginalisation property of the Gaussian
The marginalisation property of the Gaussian makes marginalising out a variable of a Gaussian distribution easy. It works as follows. We have a distribution over five dimensions. Our mean vector has five entries and our covariance matrix is a five by five matrix. Now marginalising out the fourth variable amounts to discarding the fourth entry in the mean vector and the fourth row and column in the covariance matrix. The resulting mean vector and covariance matrix again parametrize a Gaussian.

The figure below shows this visually.
![draw_gauss](https://github.com/RobRomijnders/awesome_distributions/blob/master/im/draw_gauss.png?raw=true)

The code in `non_parametrics_gaussian.py` shows some small experiment to play with this property. This code produces the diagram below.
![awesome_gauss](https://github.com/RobRomijnders/awesome_distributions/blob/master/im/awesome_gaussian.png?raw=true)

## Aggregation property of the Dirichlet
The aggregation property of the Dirichlet makes aggregating two dimensions of a Dirichlet easy. It works as follows. We have a distribution over five dimensions. Our alpha vector has five entries. Now aggregating the third and the fourth variable amounts to adding their alphas together. The resulting alphas again parametrize a Dirichlet.

The figure below shows this visually.
![draw_diri](https://github.com/RobRomijnders/awesome_distributions/blob/master/im/draw_dir.png?raw=true)

The code in `non_parametrics_dirichlet.py` shows some small experiment to play with this property. This code produces the diagram below.
![awesome_diri](https://github.com/RobRomijnders/awesome_distributions/blob/master/im/awesome_dirchlet.png?raw=true)

Honestly, I am new to Bayesian non parametrics. These scribbles show my initial thoughts. I would be happy to hear from further insights, help or extensions!

As always, I am curious to any comments and questions. Reach me at romijndersrob@gmail.com