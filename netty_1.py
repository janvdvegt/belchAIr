import tensorflow as tf
import numpy as np


class Netty(object):
    def __init__(self, game_state, nlayers, nneurons, learning_rate, batch_size):
        self.game_state = game_state
        self.nlayers = nlayers
        self.nneurons = nneurons
        self.learning_rate = learning_rate
        self.batch_size = batch_size

        self.sess = None

        self.experience_buffer = []
        self.game_state_dim = len(game_state.state_space())
        self.action_dim = len(game_state.all_actions())

        self.build_model()

    def build_model(self):
        self.sess = tf.Session()
        self.state_input = tf.placeholder(tf.float32, shape=(None, self.game_state_dim), name = 'state_input')
        self.legal_actions = tf.placeholder(tf.float32, shape=(None, self.action_dim), name='legal_actions')
        self.reward = tf.placeholder(tf.float32, shape=(None, 1), name = 'reward')

        self.W1 = tf.Variable(tf.random_normal([self.game_state_dim, self.nneurons], stddev=0.3), name='W1')
        self.b1 = tf.Variable(tf.random_normal([self.nneurons], stddev=0.3), name='b1')
        self.hidden_layer1 = tf.nn.tanh(tf.matmul(self.state_input, self.W1) + self.b1)

        self.W2 = tf.Variable(tf.random_normal([self.nneurons, self.nneurons], stddev=0.3), name='W2')
        self.b2 = tf.Variable(tf.random_normal([self.nneurons], stddev=0.3), name='b2')
        self.hidden_layer2 = tf.nn.tanh(tf.matmul(self.hidden_layer1, self.W2) + self.b2)

        self.Wout = tf.Variable(tf.random_normal([self.nneurons, self.action_dim], stddev=0.3), name='Wout')
        self.bout = tf.Variable(tf.random_normal([self.action_dim], stddev=0.3), name='bout')
        self.out_layer = tf.matmul(self.hidden_layer2, self.Wout) + self.bout

        self.out_layer_sm = tf.nn.softmax(self.out_layer, name='out_sm')

        self.out_layer_sm_legal = self.out_layer_sm * self.legal_actions
        self.normalization_sum = tf.reduce_sum(self.out_layer_sm_legal)
        self.out_layer_sm_legal = tf.multiply(self.out_layer_sm_legal,
                                              tf.reciprocal(self.normalization_sum))

        self.sess.run(tf.global_variables_initializer())

    def play_game(self):
        self.game_state.reset_game()
        reward = None
        while reward is None:
            legal_actions, all_actions = self.game_state.legal_actions()
            current_game_state = self.game_state.state_space()


def discount_rewards(r):
    """ take 1D float array of rewards and compute discounted reward """
    discounted_r = np.zeros_like(r)
    running_add = 0
    for t in reversed(range(0, r.size)):
        running_add = running_add * 0.99 + r[t]
        discounted_r[t] = running_add
    return discounted_r

#netty = Netty()

print(discount_rewards(np.array([0., 0., 1.])))