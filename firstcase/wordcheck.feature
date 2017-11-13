# Created by jianghailong at 2017/11/6
Feature: word check #Enter feature name here
  # Enter feature description here

  Scenario: Check letters # Enter scenario name here
    Given I have a letter
    When I input letter y
    Then the inputed letter is Equal with y
    # Enter steps here