# DESCRIPTION

- platform to discover and submit AI tools for students

## Name

AIForSchool.com

# MVP GOALS

- User can **see submited** AI tools
- User can **submit** new AI tools
- Have authentication
- Furfill the SEO standards

## Maybe Goals

- rating relevance on a scale of 1-5

# Explanation

Two data models are created and added added to the database as tables:

- **Tools** -> Which includes a unique id, a name, description, content and a link, which are all non nullable strings, as well as a creation date, which is auto generated
- **Category** -> Will later be connected to the tools by a relationship, one category can have multiple tools belonging to it. Right now it consists of a unique id and a name which should be a string.
