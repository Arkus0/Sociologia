# Recommended Notion schema

Use Notion as a control layer, not as the final wiki.

## Database 1: Courses

Suggested properties:

- Name (title)
- Semester (select)
- Status (select)
- Professor (text)
- Assessment type (multi-select)
- Priority (select)
- Raw sources count (number)
- Compiled notes count (number)
- Open questions count (number)

## Database 2: Sources

Suggested properties:

- Name (title)
- Course (relation or text)
- Semester (text)
- SourcePath (url or text)
- Type (select: PDF, Article, Notes, Slides, Dataset)
- Processed (checkbox)
- Concepts (multi-select)
- Authors (multi-select)
- Reviewed (checkbox)

## Database 3: Outputs

Suggested properties:

- Name (title)
- OutputType (select: summary, essay, flashcards, slides, map)
- RelatedCourse (relation or text)
- RelatedConcepts (multi-select)
- QualityStatus (select)
- GeneratedAt (date)

## Rule

Do not let Notion become the only place where the knowledge exists.
The markdown repo remains the source of truth.
