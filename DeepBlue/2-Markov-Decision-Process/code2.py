#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import numpy as np
import collections

class Env(object):
    def __init__(self):
        self.S = ['s1', 's2', 's3', 's4', 's5']  # 状态集合
        self.R = {
            's1': {
                'phone': -1,
                'quit': 0
            },
            's2': {
                'phone': -1,
                'study': -2
            },
            's3': {
                'sleep': 0,
                'study': -2
            },
            's4': {
                'review': 10,
                'noreview': -5
            }
        }
        self.S_A_S = {
            's1': {
                'phone': {
                    's1': 1
                },
                'quit': {
                    's2': 1
                }
            },
            's2': {
                'phone': {
                    's1': 1
                },
                'study': {
                    's3': 1
                }
            },
            's3': {
                'sleep': {
                    's5': 1
                },
                'study': {
                    's4': 1
                }
            },
            's4': {
                'review': {
                    's5': 1
                },
                'noreview': {
                    's2': 0.2,
                    's3': 0.4,
                    's4': 0.4
                }
            }
        }
    def _compute_state_transformation_matrix_by_policy(self, policy):
        st_matrix = np.zeros((5,5), dtype = float)
        state_index_dict = {}
        for index, state in enumerate(self.S):
            state_index_dict[state] = index

        for index, state in enumerate(policy.keys()):
            action = policy[state]
            next_state = self.S_A_S[state][action]
            if len(next_state.keys()) == 1:
                st_matrix[index, state_index_dict[next_state.keys()[0]]] = 1
            else:
                for next_possible_state in next_state.keys():
                    st_matrix[index, state_index_dict[next_possible_state]] = next_state[next_possible_state]
        return st_matrix

    def compute_value(self, policy, gamma):
        state_trans_matrix = self._compute_state_transformation_matrix_by_policy(policy)
        reward_vector = np.zeros(5)
        for index, state in enumerate(policy.keys()):
            reward_vector[index] = self.get_reward(state, policy[state])
        print('reward_vector:{}'.format(reward_vector))
        print('state_trans_matrix:{}'.format(state_trans_matrix))
        print(policy)
        print(np.eye(5) - gamma * state_trans_matrix)
        inv = np.linalg.inv(np.eye(5) - gamma * state_trans_matrix)
        return inv.dot(reward_vector)



    def step(self, s, a):  # 状态转移函数和奖励函数
        s_n = None
        r = None
        terminal = False   # 是否进入终止状态
        # 实现自己的代码
        s_n_p = self.S_A_S[s][a]

        s_n = self.sample_state_by_probability(s_n_p)

        r = self.get_reward(s,a)

        if s_n == 's5':
            terminal = True

        return s_n, r, terminal

    def get_reward(self, s, a):
        return self.R[s][a]

    def sample_state_by_probability(self, p_dict):
        if len(p_dict.keys()) == 1:
            return p_dict.keys()[0]
        else:
            seed = random.random()
            start = 0
            for _ , key in enumerate(p_dict.keys()):
                if seed >= start and seed < start + p_dict[key]:
                    return key
                start = start + p_dict[key]

class Agent(object):
    def __init__(self):
        self.A = ['quit', 'phone', 'study', 'sleep', 'review', 'noreview']
        self.available_actions = {
            's1': ['phone', 'quit'],
            's2': ['phone', 'study'],
            's3': ['study', 'sleep'],
            's4': ['review', 'noreview']
        }
        self._fixed_policy = None

    def random_policy(self, s):
        a = None
        # 实现自己的代码
        index = random.randint(0, len(self.available_actions[s])-1)
        a = self.available_actions[s][index]
        # print(index)
        # print('current state:{}'.format(s))
        return a

    def set_fixed_policy(self, policy):
        self._fixed_policy = policy

    def get_fixed_policy(self):
        return self._fixed_policy

    def fixed_policy(self, s):
        return self._fixed_policy[s]



if __name__ == "__main__":
    # 仿真随机策略
    # 寻找最优策略
    # 我这里给出一次仿真的示例, 假设初始状态是s2
    env = Env()
    agent = Agent()
    gamma = 1
    max_time_step = 1000
    for evaluated_s in env.S:
        if evaluated_s == 's5':
            continue

        average_g = 0
        for i in range(max_time_step):
            curr_gamma = 1
            g = 0  # 这次实验的回报值, 多次实验后平均，即得到v(s2)的估计
            s = evaluated_s
            for i in range(max_time_step):
                a = agent.random_policy(s)
                s, r, term = env.step(s, a)
                g += curr_gamma * r
                curr_gamma *= gamma
                if term:
                    break
            # print('v(s2):{}'.format(g))
            average_g += g

        average_g = average_g / max_time_step
        print('average v({}):{}'.format(evaluated_s,average_g))

    # enum all fixed policy to find optimal policy
    available_actions = agent.available_actions
    policy = collections.OrderedDict()
    max_value = np.full(5, -10000)
    optimal_policy = None
    for action_s1 in available_actions['s1']:
        policy['s1'] = action_s1
        for action_s2 in available_actions['s2']:
            policy['s2'] = action_s2
            for action_s3 in available_actions['s3']:
                policy['s3'] = action_s3
                for action_s4 in available_actions['s4']:
                    policy['s4'] = action_s4
                    # agent.set_fixed_policy(policy)
                    value = env.compute_value(policy, gamma)
                    if (value >= max_value).all():
                        optimal_policy = policy.copy()
                        max_value = value
                        # print('policy:{}'.format(policy))
                        # print('value:{}'.format(value))
                        # print('current max_value:{}'.format(max_value))
                        # print(value >= max_value)
    print('optimal_policy:{}'.format(optimal_policy))
    print('optimal_value:{}'.format(max_value))

