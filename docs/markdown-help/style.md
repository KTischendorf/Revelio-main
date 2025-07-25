author: "Vance Stokes"
date: "2025-04-17"
description: "Revelio Style Guide""
tags: ["revelio", "style", "markdown", "documentation" ]
---

# Revelio Style Guide

## Emphasis and Formatting Style

- **When to use bold:** Use bold text sparingly to highlight key terms, UI elements (like button names), or critical warnings. Avoid bolding entire sentences or paragraphs.

- **When to use italics:**
  - Introducing new terms (the first time they appear).
  - Titles of books, articles, or other external works.
  - Slight emphasis when bold might be too strong.

- **Use of inline code:** Employ backticks ` consistently for:
  - Code snippets within sentences.
  - File paths and names.
  - Command-line commands.
  - Specific function or variable names.

- **Avoid excessive formatting:** Overuse of bold, italics, or other formatting can make the text cluttered and harder to read.

## Heading Style

- **Hierarchy is key:** Use heading levels (`#` to `######`) to clearly indicate the structure and hierarchy of your content. Don't skip levels (e.g., going directly from ## to ####).
- **Clarity and conciseness:** Headings should be brief and accurately reflect the content of the section below.
- **Sentence case for headings:** Generally, use sentence case for headings (capitalize only the first word and proper nouns). This tends to be more readable than title case (capitalizing most words).
- **Consistency:** Be consistent in your heading style throughout the documentation.

## List Style

- **Parallel structure:** When items in a list are related, try to maintain parallel grammatical structure. For example, if one item starts with a verb, try to start others with verbs as well.
- **Brevity:** Keep list items concise. If an item requires more detailed explanation, consider breaking it down into a sub-section.
- **Consistent bullet/number style:** Stick to either hyphens (-) or asterisks (*) for unordered lists. For ordered lists, use standard numbers (1., 2., etc.).

## Code Block Style

- **Language specification:** Always specify the programming language or format for syntax highlighting within code blocks (e.g., ```python). This greatly improves readability.
- **Conciseness:** Include only the necessary code to illustrate the point. Avoid large, irrelevant code snippets.
- **Comments:** Use comments within code blocks to explain complex or important parts.
- **Consistency:** Maintain a consistent code style within your examples (though you don't need to enforce the exact style of the documented project).

## Link Style

- **Descriptive link text:** The text you use for a link should clearly indicate where the user will be taken. Avoid generic phrases like "click here."
- **Internal vs. External:** Be clear when you are linking to another part of your documentation versus an external resource. This helps users understand the context of the link.
- **Avoid bare URLs:** Instead of just pasting a URL, always use Markdown link syntax with descriptive text.


## Image Style

- **Meaningful alt text:** Always provide descriptive alt text for images. This is crucial for accessibility and helps users understand the image even if it doesn't load.
- **Appropriate sizing (considerations):** While Markdown doesn't directly control image size, be mindful of the size of the images you include. Optimize images for the web to avoid slow loading times. Your MkDocs theme might offer some control over image sizing.

## General Writing Style (Re-emphasized as Style)

- **Clarity over cleverness:** Prioritize clear and direct language over overly complex or witty prose.
- **Target audience:** Write with your intended audience in mind. Use language and examples that they will understand.
- **Consistency in terminology:** Define key terms and use them consistently throughout the documentation.
- **Tone:** Maintain a consistent tone (e.g., formal, informal, technical).
- **Use of the second person ("you"):** Decide whether to address the reader directly using "you" or to use a more impersonal tone and stick with it.
- **Imperative mood for instructions:**  When providing step-by-step instructions, use the imperative mood (e.g., "Click the button," not "The user should click the button").
