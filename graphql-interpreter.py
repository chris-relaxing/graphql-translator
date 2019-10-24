#!/usr/bin/python
"""
The purpose of this script is to take in a block of graphql and output the graphql's meaning
in plain English.
"""
graphqlInput = """{
  hero {
    name
  }
}"""

graphqlInput = """  liveVideos {
    id
    title
    thumbnail
    isLive
}"""

graphqlInput = """
{
  book(id: "clean-code") {
    name
    authors {
        name
        books {
            name
        }
    }
  }
}
"""

graphqlInput = """ context {
    ... on SectionPage {
      name
      displayId
      rootGroup {
        ... on FrontGroup {
          featured {
            ...teaser
          }
          newsblock {
            ...teaser
          }
          secondary {
            ...secondaryTeaser
          }
          poll {
            ...pollTeaser
          }
          specialSections {
            ...specialSectionsTeaser
          }
        }
      }
    }
  }"""



print(graphqlInput)

# Pattern to look for: 
# Word followed by an opening bracket

queryPieces = graphqlInput.split('\n')

for line in queryPieces:

    if len(line) == 0:
        print(line, "\t\tBlank line before the graphql\n\n")

    # Look for block beginnings { and endings }
    elif len(line) == 1:
        if line.startswith('{'):
            print(line, "\t\tBeginning of a block.", len(line), "\n\n")
        elif line.endswith('}'):
            print("\n")
            print(line, "\t\tEnd of block.", len(line))

    # Body of the graphql query, not a beginning or ending
    else:
        # Split the line into terms
        print("raw line:", line, len(line))
        terms = line.split()
#         print(len(terms), " terms ", terms, len(terms[0]))

#     print(line)
