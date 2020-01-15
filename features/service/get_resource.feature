# Feature definition for Get operation Scenario defined in Gherkins Language
Feature: Get Resource

  # Scenario definition for Get operation Test
  @get_resource @critical
  Scenario: Get Resource All
    Given a get resource
    When user send the get resource request
    Then user receive the get resource response