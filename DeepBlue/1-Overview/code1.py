#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import random

BOARD_LEN = 3


class TicTacToeEnv(object):
    def __init__(self):
        # data 表示棋盘当前状态，1和-1分别表示x和o，0表示空位
        self.data = np.zeros((BOARD_LEN, BOARD_LEN))
        self.winner = None  # 1/0/-1表示玩家一胜/平局/玩家二胜，None表示未分出胜负
        self.terminal = False  # true表示游戏结束
        self.current_player = 1  # 当前正在下棋的人是玩家1还是-1

    def reset(self):
        # 游戏重新开始，返回状态
        self.data = np.zeros((BOARD_LEN, BOARD_LEN))
        self.winner = None
        self.terminal = False
        state = self.getState()
        return state

    def getState(self):
        # 注意到很多时候，存储数据不等同与状态，状态的定义可以有很多种，比如将棋的位置作一些哈希编码等
        # 这里直接返回data数据作为状态
        return self.data

    def getReward(self):
        """Return (reward_1, reward_2)
        """
        if self.terminal:
            if self.winner == 1:
                return 1, -1
            elif self.winner == -1:
                return -1, 1
        return 0, 0

    def getCurrentPlayer(self):
        return self.current_player

    def getWinner(self):
        return self.winner

    def switchPlayer(self):
        if self.current_player == 1:
            self.current_player = -1
        else:
            self.current_player = 1

    def checkState(self):
        # 每次有人下棋，都要检查游戏是否结束
        # 从而更新self.terminal和self.winner
        # ----------------------------------
        # 实现自己的代码
        # ----------------------------------
        for row in self.data:
            if np.sum(row) == 3:
                self.winner = 1
            elif np.sum(row) == -3:
                self.winner = -1
            else:
                pass
        for col in np.transpose(self.data):
            if np.sum(col) == 3:
                self.winner = 1
            elif np.sum(col) == -3:
                self.winner = -1
            else:
                pass
        diagonal = np.sum(self.data.diagonal())
        if diagonal == 3:
            self.winner = 1
        elif diagonal == -3:
            self.winner = -1
        else:
            pass

        diagonal = np.sum(np.fliplr(self.data).diagonal())
        if diagonal == 3:
            self.winner = 1
        elif diagonal == -3:
            self.winner = -1
        else:
            pass

        if self.winner is not None:
            self.terminal = True
            return

        unfilled = np.transpose(np.where(self.data == 0.))
        if len(unfilled) == 0:
            self.terminal = True
            return

    def step(self, action):
        """action: is a tuple or list [x, y]
        Return:
            state, reward, terminal
        """
        # ----------------------------------
        # 实现自己的代码
        # ----------------------------------
        self.data[action[0]][action[1]]= self.current_player
        self.switchPlayer()
        self.checkState()
        return self.getState(), self.getReward(), self.terminal


class RandAgent(object):
    def policy(self, state):
        """
        Return: action
        """
        # ----------------------------------
        # 实现自己的代码
        # ----------------------------------
        unfilled = np.transpose(np.where(state == 0.))
        index = random.randint(0, len(unfilled)-1)
        return unfilled[index]


def main():
    env= TicTacToeEnv()
    agent1= RandAgent()
    agent2= RandAgent()
    state= env.reset()

    # 这里给出了一次运行的代码参考
    # 你可以按照自己的想法实现
    # 多次实验，计算在双方随机策略下，先手胜/平/负的概率
    test_num = 0
    player1_win_num = 0
    player2_win_num = 0
    draw_num = 0
    while 1:
        if test_num > 9999:
            break
        current_player= env.getCurrentPlayer()
        if current_player == 1:
            action= agent1.policy(state)
        else:
            action= agent2.policy(state)
        next_state, reward, terminal= env.step(action)
        print(next_state)
        if terminal:
            if env.getWinner() == 1:
                winner = 'Player1'
                player1_win_num = player1_win_num + 1
            elif env.getWinner() == -1:
                player2_win_num = player2_win_num + 1
                winner = 'Player2'
            else:
                winner = 'None'
                draw_num = draw_num + 1
            print('Winner: {}'.format(winner))
            test_num = test_num + 1
            print('Player1 winning probability:{}'.format(float(player1_win_num) / test_num))
            print('Player2 winning probability:{}'.format(float(player2_win_num) / test_num))
            print('Draw probability:{}'.format(float(draw_num) / test_num))
            state= env.reset()
            continue
        state= next_state



if __name__ == "__main__":
    main()
