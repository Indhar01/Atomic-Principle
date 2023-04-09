# md Ref
_____________________________________________
# The largest heading
## The second largest heading
###### The smallest heading

## Create Table
| FirstName     | LastName      | City     |
| ------------- | ------------- | -------- |
| John          | Test1         | NewYork  |
| Bob           | Test2         | Toronto  |

| FirstName     | LastName      | City   
| ------------- | ------------- | --------    |
| `John`        | Test1         | `NewYork`   |
| `Bob`         | Test2         | `Toronto`   |

Right align     ---:
Left align       :---
Center align    :---:

| FirstName     | LastName      | City  |
| :------------ |   :---:       | --------: |
| `John`        | Test1         | `NewYork`   |
| `Bob`         | Test2         | `Los Angeles`   |

[**Styling text**](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax#styling-text)


|Style	|Syntax	|Keyboard shortcut	|Example|	Output|
|-------|-------| --------------- | ------|-------|
|Bold	|** ** or __ __	|Command+B (Mac) or Ctrl+B (Windows/Linux)	|** This is bold text **	|**This is bold text**|
|Italic|	* * or _ _    | 	Command+I (Mac) or Ctrl+I (Windows/Linux)	|* This text is italicized * |	*This text is italicized* |
|Strikethrough|	~~ ~~	|	| ~~ This was mistaken text ~~ |	~~This was mistaken text~~ |
|Bold and nested italic |	** ** and _ _	 | |	** This text is _extremely_ important ** |	**This text is _extremely_ important** |
|All bold and italic	| *** ***	| |	*** All this text is important *** |	***All this text is important*** |

**Quoting text**

Text that is not a quote

> Text that is a quote

**Quoting code**

Use `git status` to list all new or modified files that haven't yet been committed.
Some basic Git commands are:
```
git status
git add
git commit
```
**Links**

```This site was built using [ GitHub Pages ](https://pages.github.com/).```
This site was built using [GitHub Pages](https://pages.github.com/).

*Relative links*
A relative link is a link that is relative to the current file. For example, if you have a README file in root of your repository, and you have another file in docs/CONTRIBUTING.md, the relative link to CONTRIBUTING.md in your README might look like this:

```[Contribution guidelines for this project](docs/CONTRIBUTING.md)```
GitHub will automatically transform your relative link or image path based on whatever branch you're currently on, so that the link or path always works. You can use all relative link operands, such as ./ and ../.

Relative links are easier for users who clone your repository. Absolute links may not work in clones of your repository - we recommend using relative links to refer to other files within your repository.

**Images**
```![This is an image](https://myoctocat.com/assets/images/base-octocat.svg)```
or You can drag the image to readme directly

**Specifying the theme an image**
|Context|	URL|
|-------|----|
|Dark Theme|	```![GitHub Light](https://github.com/github-light.png#gh-dark-mode-only)```|
|Light Theme|	```![GitHub Dark](https://github.com/github-dark.png#gh-light-mode-only)```|

**Lists**
```
- George Washington
- John Adams
- Thomas Jefferson
```
- George Washington
- John Adams
- Thomas Jefferson

```
1. James Madison
2. James Monroe
3. John Quincy Adams
```
1. James Madison
2. James Monroe
3. John Quincy Adams

**Nested Lists**

```
1. First list item
   - First nested list item
     - Second nested list item
```
1. First list item
   - First nested list item
     - Second nested list item
     
     
**Task lists**
```
- [x] #739
- [ ] https://github.com/octo-org/octo-repo/issues/740
- [ ] Add delight to the experience when all tasks are complete :tada:
```
- [x] #739
- [ ] https://github.com/octo-org/octo-repo/issues/740
- [ ] Add delight to the experience when all tasks are complete :tada:

**Using emoji**
```@octocat :+1: This PR looks great - it's ready to merge! :shipit:```
@octocat :+1: This PR looks great - it's ready to merge! :shipit:

**Footnotes**

```
Here is a simple footnote[^1].
[^1]: My reference.
```
Here is a simple footnote[^1].
[^1]: My reference.

**comments**
```<!-- This content will not appear in the rendered Markdown -->```
**Ignoring Markdown formatting**
```Let's rename \*our-new-project\* to \*our-old-project\*.```
Let's rename \*our-new-project\* to \*our-old-project\*.

### credits: [Indhar](https://github.com/Indhar01)
