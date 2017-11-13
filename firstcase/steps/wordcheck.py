#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/11/6

from behave import *

@Given('I have a letter')
def step_impl(context):
    pass

@When('I input letter {letter}')
def step_impl(context,letter):
    context.letter = letter

@Then('the inputed letter is Equal with {TargetLetter}')
def step_impl(context,TargetLetter):
    context.TargetLetter = TargetLetter
    assert context.letter is context.TargetLetter

