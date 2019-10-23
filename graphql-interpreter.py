#!/usr/bin/python
"""
The purpose of this script is to take in a block of graphql and output the graphql's meaning
in plain English.
"""


graphqlInput = """
{
  hero {
    name
  }
}
"""

print('Test that the script is running..', graphqlInput)
