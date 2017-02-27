import tensorflow as tf
import numpy as np
from util import one_hot


class Netty(object):
    def __init__(self, game_state, nlayers, nneurons, learning_rate, batch_size, buffer_size, batch_games, epsilon):
        self.game_state = game_state
        self.nlayers = nlayers
        self.nneurons = nneurons
        self.learning_rate = learning_rate
        self.batch_size = batch_size
        self.epsilon = epsilon
        self.buffer_size = buffer_size
        self.batch_games = batch_games

        self.sess = None

        self.experience_buffer = []
        self.game_state_dim = len(game_state.state_space())
        self.action_dim = len(game_state.all_actions())

        self.build_model()

    def build_model(self):
        self.sess = tf.Session()
        self.state_input = tf.placeholder(tf.float32, shape=(None, self.game_state_dim), name = 'state_input')
        self.legal_actions = tf.placeholder(tf.float32, shape=(None, self.action_dim), name='legal_actions')
        self.action_taken = tf.placeholder(tf.int32, shape=(None, self.action_dim), name='action_taken')

        self.W1 = tf.Variable(tf.random_normal([self.game_state_dim, self.nneurons], stddev=0.3), name='W1')
        self.b1 = tf.Variable(tf.random_normal([self.nneurons], stddev=0.3), name='b1')
        self.hidden_layer1 = tf.nn.tanh(tf.matmul(self.state_input, self.W1) + self.b1)

        self.W2 = tf.Variable(tf.random_normal([self.nneurons, self.nneurons], stddev=0.3), name='W2')
        self.b2 = tf.Variable(tf.random_normal([self.nneurons], stddev=0.3), name='b2')
        self.hidden_layer2 = tf.nn.tanh(tf.matmul(self.hidden_layer1, self.W2) + self.b2)

        self.Wout = tf.Variable(tf.random_normal([self.nneurons, self.action_dim], stddev=0.3), name='Wout')
        self.bout = tf.Variable(tf.random_normal([self.action_dim], stddev=0.3), name='bout')
        self.out_layer = tf.matmul(self.hidden_layer2, self.Wout) + self.bout

        self.zero = tf.constant(0, dtype=tf.float32)
        self.action_mask = tf.not_equal(self.legal_actions, self.zero)

        print('action_mask', self.action_mask.get_shape())

        self.out_layer_masked = tf.boolean_mask(self.out_layer, self.action_mask)
        print('out_layer_masked', self.out_layer_masked.get_shape())
        self.action_taken_masked = tf.boolean_mask(self.action_taken, self.action_mask)
        print('action_taken_masked', self.action_taken_masked.get_shape())

        self.out_layer_masked_sm = tf.nn.softmax(self.out_layer_masked, name='out_masked_sm')
        print('out_layer_masked_sm', self.out_layer_masked_sm.get_shape())

        self.out_layer_sm = tf.nn.softmax(self.out_layer, name='out_sm')
        print('out_layer_sm', self.out_layer_sm.get_shape())
        self.out_layer_sm_legal = self.out_layer_sm * self.legal_actions
        print('out_layer_sm_legal', self.out_layer_sm_legal.get_shape())
        self.normalization_sum = tf.reduce_sum(self.out_layer_sm_legal)
        print('normalization_sum', self.normalization_sum.get_shape())
        self.out_layer_sm_legal = tf.multiply(self.out_layer_sm_legal,
                                              tf.reciprocal(self.normalization_sum))
        print('out_layer_sm_legal', self.out_layer_sm_legal.get_shape())

        self.loss = tf.nn.softmax_cross_entropy_with_logits(labels=self.action_taken_masked,
                                                            logits=self.out_layer_masked, name='loss_function') # * self.reward
        self.optimizer = tf.train.AdamOptimizer()
        self.train_op = self.optimizer.minimize(self.loss)

        self.sess.run(tf.global_variables_initializer())

    def play_game(self):
        self.game_state.reset_game()
        reward = None
        actions_taken = []
        state_inputs = []
        legal_actions_list = []
        while reward is None:
            legal_actions, all_actions = self.game_state.possible_actions()
            current_game_state = self.game_state.state_space()
            legal_actions_list.append(legal_actions)
            state_inputs.append(current_game_state)
            policy_probs = self.sess.run(self.out_layer_sm_legal,
                                         feed_dict={self.state_input: [current_game_state],
                                                    self.legal_actions: [legal_actions]})
            action_to_take = np.argmax(policy_probs)
            if np.random.rand() < self.epsilon:
                #action_to_take = np.random.randint(len(policy_probs))
                action_to_take = np.random.choice([index for index, action in enumerate(legal_actions) if action == 1])
            actions_taken.append(action_to_take)
            reward = all_actions[action_to_take].resolve(self.game_state)
        total_rewards = np.concatenate((np.zeros(len(actions_taken) - 1), [reward]))
        total_rewards_disc = discount_rewards(total_rewards)
        return actions_taken, total_rewards_disc, legal_actions_list, state_inputs


    def train(self):
        actions_taken, total_rewards_disc, legal_actions_list, state_inputs = self.play_game()
        losses = []
        for i in range(100):
            for action_taken, disc_reward, legal_actions, state_input in zip(actions_taken, total_rewards_disc, legal_actions_list, state_inputs):
                print(disc_reward)
                #print(action_taken)
                #action_taken = tf.one_hot([action_taken], self.action_dim)
                #print(action_taken)
                self.sess.run(self.train_op, feed_dict={self.state_input: [state_input],
                                                        self.legal_actions: [legal_actions],
                                                        self.action_taken: [action_taken]})
                                                        #self.reward: np.array([disc_reward])})
                losses.append(self.sess.run(self.loss, feed_dict={self.state_input: [state_input],
                                                        self.legal_actions: [legal_actions],
                                                        self.action_taken: [action_taken]}))
                                                        #self.reward: np.array([disc_reward])}))
        return losses



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