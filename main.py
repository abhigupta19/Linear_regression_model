import tensorflow as tf
x_train=[1.0,2.0,3.0,4.0]
y_train=[-1.0,-2.0,-3.0,-4.0]
m = tf.Variable(initial_value=[1.0],dtype=tf.float32)
b=tf.Variable(initial_value=[1.0],dtype=tf.float32)
x=tf.placeholder(dtype=tf.float32)
y_input=tf.placeholder(dtype=tf.float32)
session=tf.Session()
y_outpout=m*x+b
loss=tf.reduce_sum(input_tensor=tf.square(x=y_outpout-y_input))
optimzires=tf.train.GradientDescentOptimizer(learning_rate=0.01)
train_step=optimzires.minimize(loss=loss)

session.run(tf.global_variables_initializer())
print(session.run(fetches=loss,feed_dict={x:x_train, y_input:y_train}))
for i in range(2000):
    session.run(fetches=train_step, feed_dict={x: x_train, y_input: y_train})
print(session.run(fetches=[loss,m,b],feed_dict={x:x_train, y_input:y_train}))
print(session.run(fetches=y_outpout,feed_dict={x:[4.0,5.0,6.0,7.0]}))




