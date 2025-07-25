---
author: "Vance Stokes"
date: "2024-10-05"
description: "A cheatsheet for building objects in Markdown."
tags:
---

# Markdown Cheatsheet

## Headings

```md
# Heading 1
## Heading 2
### Heading 3
#### Heading 4
##### Heading 5
###### Heading 6
```

## Emphasis

```md
*Italic* or _Italic_
**Bold** or __Bold__
***Bold and Italic*** or ___Bold and Italic___
```

## Lists

### Unordered List

```md
- Item 1
- Item 2
  - Subitem 2.1
  - Subitem 2.2
```

### Ordered List

```md
1. Item 1
2. Item 2
   1. Subitem 2.1
   2. Subitem 2.2
```

## Links

```md
[Link Text](http://example.com)
```

## Images

```md
![Alt Text](http://example.com/image.jpg)
```

## Blockquotes

```md
> This is a blockquote.
```

## Code

### Inline Code

```md
`inline code`
```

### Code Block

```md
{
  "firstName": "John",
  "lastName": "Doe"
}
```

## Tables

```md
| Header 1 | Header 2 |
|----------|----------|
| Row 1 Col 1 | Row 1 Col 2 |
| Row 2 Col 1 | Row 2 Col 2 |
```

## Horizontal Rule

```md
---
```

## Task Lists

```md
- [x] Task 1
- [ ] Task 2
- [ ] Task 3
```

## Front Matter (for MkDocs or Jekyll)

```md
---
title: "Document Title"
author: "Author Name"
date: "2023-10-05"
description: "A brief description of the document."
tags: ["tag1", "tag2"]
---
```

## Footnotes

```md
Here is a footnote reference[^1].

[^1]: Here is the footnote.
```

## Definition Lists

```md
Term 1
: Definition 1

Term 2
: Definition 2
```

## Strikethrough

```md
~~Strikethrough~~
```

## Emoji

```md
:smile: :+1: :heart:
```

## Admonitions (for MkDocs Material Theme)

```md
!!! note
    This is a note.

!!! warning
    This is a warning.
```

## Example Document

> Here's an example document using various elements:

```md
---
title: "Markdown Cheatsheet"
author: "Your Name"
date: "2023-10-05"
description: "A cheatsheet for building objects in Markdown."
tags: ["markdown", "cheatsheet"]
---

# Markdown Cheatsheet

## Headings
# Heading 1
## Heading 2
### Heading 3

## Emphasis
*Italic*, **Bold**, ***Bold and Italic***

## Lists
- Unordered Item 1
- Unordered Item 2
  - Subitem 2.1

1. Ordered Item 1
2. Ordered Item 2
   1. Subitem 2.1

## Links and Images
[Example Link](http://example.com)

![Example Image](http://example.com/image.jpg)

## Blockquotes
> This is a blockquote.

## Code
Inline `code`

```

```md

## Tables
| Header 1 | Header 2 |
|----------|----------|
| Row 1 Col 1 | Row 1 Col 2 |
| Row 2 Col 1 | Row 2 Col 2 |

## Horizontal Rule
---

## Task Lists
- [x] Task 1
- [ ] Task 2

## Footnotes
Here is a footnote reference[^1].

[^1]: Here is the footnote.

## Definition Lists
Term 1
: Definition 1

Term 2
: Definition 2

## Strikethrough
~~Strikethrough~~

## Emoji
:smile: :+1: :heart:

## Admonitions
!!! note
    This is a note.

!!! warning
    This is a warning.
```
