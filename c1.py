#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class A:

    def __init__(self) -> None:
        self.a = None

    def haha(self):
        self.a = 1
    def hehe(self):
        return self.a

if __name__ == '__main__':
    a = A()
    print(a.hehe())
    