#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
from enum import Enum

import numpy as np
import random
import math
import matplotlib.pyplot as plt
import datetime

gamma = 0.9


class IterationType(Enum):
    POLICY_ITERATION = 1
    VALUE_ITERATION = 2
    IN_PLACE_ITERATION = 3


class Env(object):
    def __init__(self):
        self.world_size = 5
        self.A_pos = [0, 1]
        self.A_n_pos = [4, 1]
        self.B_pos = [0, 3]
        self.B_n_pos = [2, 3]
        # 构建P(s'|s, a)和R(r|s, a)
        # 这是确定性的动态转移矩阵
        # 这里用前两维表示状态，第三维表示动作
        # 本节使用了动态规划的方法，因此P和R对Agent也是已知的
        # 动作上，0:N, 1:S, 2:W, 3:E
        self.P = np.empty(
            (self.world_size, self.world_size, 4), dtype=np.object)
        self.R = np.zeros((self.world_size, self.world_size, 4))
        self.RandomPolicy = np.full(
            (self.world_size, self.world_size, 4), 0.25)

        for i in range(self.world_size):
            for j in range(self.world_size):
                for a in range(4):
                    s = [i, j]
                    if a == 0:  # North
                        if i == 0:
                            s_n = s
                            r = -1
                        else:
                            s_n = [i - 1, j]
                            r = 0
                    elif a == 1:  # South
                        if i == self.world_size - 1:
                            s_n = s
                            r = -1
                        else:
                            s_n = [i + 1, j]
                            r = 0
                    elif a == 2:  # West
                        # 实现自己的逻辑
                        if j == 0:
                            s_n = s
                            r = -1
                        else:
                            s_n = [i, j - 1]
                            r = 0
                    elif a == 3:  # East
                        # 实现自己的逻辑
                        if j == self.world_size - 1:
                            s_n = s
                            r = -1
                        else:
                            s_n = [i, j+1]
                            r = 0
                    else:
                        pass

                    if s == self.A_pos:
                        s_n = self.A_n_pos
                        r = 10
                    elif s == self.B_pos:
                        s_n = self.B_n_pos
                        r = 5

                    self.P[i, j, a] = s_n
                    self.R[i, j, a] = r

    def policy_improvement(self, Q, policy):
        for i in range(self.world_size):
            for j in range(self.world_size):
                    # find max value action
                max_a_value = max(Q[i, j])
                max_a_list = []

                for a, v in enumerate(Q[i, j]):
                    if v == max_a_value:
                        max_a_list.append(a)

                action_probability = Q[i, j].copy()
                for a, v in enumerate(action_probability):
                    if a in max_a_list:
                        action_probability[a] = 1.0 / len(max_a_list)
                    else:
                        action_probability[a] = 0.0
                policy[i, j] = action_probability
        return policy

    def policy_iteration(self, IterationType):
        policy = self.RandomPolicy.copy()
        Q = np.zeros((self.world_size, self.world_size, 4))
        policy_improvement_count = 0
        mean_seq = []
        for k in range(1000):
            last_q = Q.copy()
            # policy evaluation
            if IterationType == IterationType.POLICY_ITERATION:
                Q, _, _ = self.policy_iteration_evaluation(policy)
            elif IterationType == IterationType.VALUE_ITERATION:
                Q = self.policy_once_evaluation(Q, policy)
            elif IterationType == IterationType.IN_PLACE_ITERATION:
                Q = self.policy_inplace_once_evaluation(Q, policy)
            # policy improvement
            policy = self.policy_improvement(Q, policy)
            policy_improvement_count = k
            mean_seq.append(Q.mean())
            # self.print_policy(policy)
            diff = Q - last_q
            if np.sum(np.abs(diff)) == 0.0:
                break

        return Q, policy, policy_improvement_count, mean_seq

    def print_policy(self, policy):
        print('        ', end='')
        for j in range(self.world_size):
            print(j, end='                   \t')
        print('')
        for i in range(self.world_size):
            print('{}|'.format(i), end='')
            for j in range(self.world_size):
                if [i, j] == self.A_pos:
                    print('(A)', end='             |\t')
                elif [i, j] == self.B_pos:
                    print('(B)', end='             |\t')
                else:
                    for a, p in enumerate(policy[i, j]):
                        print(p, end=',')
                    print('|\t', end='')
            print('')

    def backup_v_with_q(self, Q, policy):
        V = np.zeros((self.world_size, self.world_size))
        for i in range(self.world_size):
            for j in range(self.world_size):
                action_probability = Q[i, j]
                v = 0
                for a, p in enumerate(action_probability):
                    v += p * policy[i, j, a]
                V[i, j] = v
        return V

    def policy_iteration_evaluation(self, policy):
        Q = np.zeros((self.world_size, self.world_size, 4))
        iteration_count = 0
        mean_seq = []
        for k in range(1000):
            last_q = Q.copy()
            Q = self.policy_once_evaluation(Q, policy)
            # print('iteration time:{}'.format(k))
            iteration_count = k
            mean_seq.append(Q.mean())
            if np.sum(np.abs(Q - last_q)) == 0.0:
                break

        return Q, iteration_count, mean_seq

    def policy_once_evaluation(self, Q, policy):
        Q_old = Q.copy()
        for i in range(self.world_size):
            for j in range(self.world_size):
                for a in range(4):
                    s_n = self.P[i, j, a]
                    r = self.R[i, j, a]
                    gain = 0.0
                    for a_n in range(4):
                        gain += 1 * policy[s_n[0], s_n[1],
                                           a_n] * Q_old[s_n[0], s_n[1], a_n]
                    Q[i, j, a] = r + gamma*gain
        return Q

    def policy_inplace_once_evaluation(self, Q, policy):
        for i in range(self.world_size):
            for j in range(self.world_size):
                for a in range(4):
                    s_n = self.P[i, j, a]
                    r = self.R[i, j, a]
                    gain = 0.0
                    for a_n in range(4):
                        gain += 1 * policy[s_n[0], s_n[1],
                                           a_n] * Q[s_n[0], s_n[1], a_n]
                    Q[i, j, a] = r + gamma*gain
        return Q


if __name__ == "__main__":
    env = Env()

    print('Policy Evaluation:')
    start = datetime.datetime.now()
    Q, iteration_count, mean_seq = env.policy_iteration_evaluation(
        env.RandomPolicy)
    end = datetime.datetime.now();
    print('total time:{}'.format(end - start))
    V = env.backup_v_with_q(Q, env.RandomPolicy)
    # print('Q-value:')
    # print(Q)
    print('V-value:({})'.format(iteration_count))
    print(V)
    plt.figure(1)
    plt.subplot(221)
    plt.plot(range(iteration_count+1), mean_seq)
    plt.title("Policy Evaluation:")

    print('Greedy Policy Iteration:')
    start = datetime.datetime.now()
    Q, policy, iteration_count, mean_seq = env.policy_iteration(
        IterationType.POLICY_ITERATION)
    end = datetime.datetime.now()
    print('total time:{}'.format(end - start))
    V = env.backup_v_with_q(Q, env.RandomPolicy)
    plt.subplot(222)
    plt.plot(range(iteration_count+1), mean_seq)
    plt.title("Greedy Policy Iteration:")
    # print('Q-value:')
    # print(Q)
    print('V-value:({})'.format(iteration_count))
    print(V)
    print('Best Policy:')
    env.print_policy(policy)

    print('Greedy Value Iteration:')
    start = datetime.datetime.now()
    Q, policy, iteration_count, mean_seq = env.policy_iteration(
        IterationType.VALUE_ITERATION)
    end = datetime.datetime.now()
    print('total time:{}'.format(end - start))
    V = env.backup_v_with_q(Q, env.RandomPolicy)
    plt.subplot(223)
    plt.plot(range(iteration_count+1), mean_seq)
    plt.title("Greedy Value Iteration:")
    # print('Q-value:')
    # print(Q)
    print('V-value:({})'.format(iteration_count))
    print(V)
    print('Best Policy:')
    env.print_policy(policy)

    print('Greedy Value Iteration(in-place):')
    start = datetime.datetime.now()
    Q, policy, iteration_count, mean_seq = env.policy_iteration(
        IterationType.IN_PLACE_ITERATION)
    end = datetime.datetime.now()
    print('total time:{}'.format(end - start))
    V = env.backup_v_with_q(Q, env.RandomPolicy)
    plt.subplot(224)
    plt.plot(range(iteration_count+1), mean_seq)
    plt.title("Greedy Value Iteration(in-place):")
    print('V-value:({})'.format(iteration_count))
    print(V)
    print('Best Policy:')
    env.print_policy(policy)
    plt.show()
