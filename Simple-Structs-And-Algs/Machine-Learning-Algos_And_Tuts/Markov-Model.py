import tensorflow_probability as tfp 
import tensorflow as tf

tfd = tfp.distributions
initial_distribution = tfd.Categorical(probs=[0.8, 0.2]) # refer to point 2. the initial distribution of being cold is 80%
transition_distribution = tfd.Categorical(probs=[[0.5 , 0.5], [0.2, 0.8]]) 

observation_distribution = tfd.Normal(loc=[0., 15.], scale=[5., 10.]) 
# the loc arg represents the mean and teh scale is standard deviation

model = tfd.HiddenMarkovModel(
	initial_distribution=initial_distribution,
	transition_distribution=transition_distribution,
	observation_distribution=observation_distribution,
	num_steps=7)

mean = model.mean()

with tf.compat.v1.Session() as sess:
	print(mean.numpy())
