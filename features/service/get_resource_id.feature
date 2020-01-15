# Feature definition for Get operation Scenario defined in Gherkins Language
Feature: Get Resource

  # Scenario Outline definition for GetId operation Test
  @get_resource
  Scenario Outline: Get Resource Id
    Given a get <resource_id>
    When user send the get resource_id request
    Then user receive the get resource_id response <result>

    # Each row in examples imply a execution of a different TestCase, mapping the <variable> name for the value in the row
    Examples:
      | resource_id | result    |
      | 1           | OK        |
      | 999         | NOT_FOUND |