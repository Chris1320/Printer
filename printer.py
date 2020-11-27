#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
MIT License

Copyright (c) 2020 Chris1320

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import sys

import colorama

class Printer:
    """
    Print an object to the screen using a number of methods.
    """

    def __init__(self):
        """
        Initialization method of Printer() class.
        """

        self.VERSION = [0, 0, 1, 1]
        self.__initialized = False

    def init(self):
        """
        Do necessary things before use.

        :returns void:
        """

        colorama.init()
        self.__initialized = True

    def deinit(self):
        """
        Do cleanup before exit.

        :returns void:
        """

        colorama.deinit()
        self.__initialized = False

    def print_with_status(self, obj, status=None, limit_length=None, return_output=False):
        """
        Print <obj> with status icon/prompt <status>.

        :param obj: Object to print.
        :param int status: Status number.
        :param str status: Status name.
        :param int limit_length: The character limit to print.
        :param bool return_output: If True, the method will return the output instead of printing it.

        :returns void: Returns nothing of return_output is False
        :returns str: The output/formatted version of <obj>. (If return_output is True)

        Status names and numbers:

        `inf`, 0: Information prompt `[i] <obj>`
        `warn`, 1: Warning prompt `[!] <obj>`
        `err`, 2: Error prompt `[E] <obj>`
        `crit`, 3: Critical prompt `[CRITICAL] <obj>`
        `que`, 4: Question prompt `[?] <obj>`
        `deb`, 5: Debug prompt `[...] <obj>`
        """

        if not self.__initialized:
            raise NotImplementedError("Printer is not yet initialized")

        if limit_length is None:
            pass

        elif type(limit_length) is int:
            if len(obj) > limit_length:
                newobj = ""
                _ = 0
                while _ < (len(obj) - 3):
                    # We removed 3 on `limit_length` to include the
                    # three dots in the string length.
                    if (_+1) > (limit_length - 3):
                        break

                    newobj += obj[_]
                    _ += 1

                newobj += "..."

                obj = newobj
                del newobj

        else:
            raise TypeError("limit_length must be an integer")

        if type(status) is str:
            if status == "inf":
                status = 0

            elif status == "warn":
                status = 1

            elif status == "err":
                status = 2

            elif status == "crit":
                status = 3

            elif status == "que":
                status = 4

            elif status == "deb":
                status = 5

            else:
                raise ValueError("Unknown status name")

        if type(status) is int:
            if status == 0:
                prompt = "{1}{3}[{2}i{3}] {1}{0}{1}".format(obj, colorama.Style.RESET_ALL, colorama.Fore.LIGHTGREEN_EX, colorama.Fore.LIGHTBLACK_EX)

            elif status == 1:
                prompt = "{1}{3}[{2}!{3}] {1}{0}{1}".format(obj, colorama.Style.RESET_ALL, colorama.Fore.YELLOW, colorama.Fore.LIGHTBLACK_EX)

            elif status == 2:
                prompt = "{1}{3}[{2}E{3}] {1}{0}{1}".format(obj, colorama.Style.RESET_ALL, colorama.Fore.RED, colorama.Fore.LIGHTBLACK_EX)

            elif status == 3:
                prompt = "{1}{3}{4}[{2}CRITICAL{4}] {1}{0}{1}".format(obj, colorama.Style.RESET_ALL, colorama.Fore.LIGHTRED_EX, colorama.Style.BRIGHT, colorama.Fore.LIGHTBLACK_EX)

            elif status == 4:
                prompt = "{1}{3}[{2}?{3}] {1}{0}{1}".format(obj, colorama.Style.RESET_ALL, colorama.Fore.CYAN, colorama.Fore.LIGHTBLACK_EX)

            elif status == 5:
                prompt = "{1}{3}[{2}...{3}] {1}{0}{1}".format(obj, colorama.Style.RESET_ALL, colorama.Fore.LIGHTBLACK_EX, colorama.Style.DIM)

            else:
                raise ValueError("Unknown status number")

        else:
            raise ValueError("status must be an integer or string")

        if return_output:
            return prompt

        else:
            print(prompt)
