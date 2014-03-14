# coding=utf-8
"""
help.py - Willie Help Module
Copyright 2008, Sean B. Palmer, inamidst.com
Copyright © 2013, Elad Alfassa, <elad@fedoraproject.org>
Licensed under the Eiffel Forum License 2.

http://willie.dftba.net
"""
from willie.module import commands, rule, example, priority
from willie.tools import iterkeys


@rule('$nick' '(?i)(help|doc) +([A-Za-z]+)(?:\?+)?$')
@example('!help tell')
@commands('help')
@priority('low')
def help(bot, trigger):
    """Shows a command's documentation, and possibly an example."""
    if not trigger.group(2):
        bot.reply('Say !help <command> (for example !help c) to get help for a command, or !commands for a list of commands.')
    else:
        name = trigger.group(2)
        name = name.lower()

        if name in bot.doc:
            bot.reply(bot.doc[name][0])
            if bot.doc[name][1]:
                bot.say('e.g. ' + bot.doc[name][1])


@commands('commands','komennot')
@priority('low')
def commands(bot, trigger):
    """Return a list of bot's commands"""
    banned = ['blocks', 'join', 'tell', 'load', 'mangle', 'me', 'mode', 'msg', 'part', 'quit', 'reload', 'save', 'set', 'update']
    list = sorted(iterkeys(bot.doc))
    names = ''
    for name in list:
        if name not in banned:
            names += name + ', '
    bot.say('Commands: ' + names[:-2] + '.')


@rule('$nick' r'(?i)help(?:[?!]+)?$')
@priority('low')
def help2(bot, trigger):
    response = (
        'Hi, I\'m a bot. Say "!commands" to me in private for a list ' +
        'of my commands, or see http://willie.dftba.net for more ' +
        'general details. My owner is %s.'
    ) % bot.config.owner
    bot.reply(response)
