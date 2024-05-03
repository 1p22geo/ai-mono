**Markdown**[1] is a [lightweight markup
language](lightweight_markup_language "wikilink") for creating
[formatted text](formatted_text "wikilink") using a [plain-text
editor](text_editor "wikilink"). [John Gruber](John_Gruber "wikilink")
and [Aaron Swartz](Aaron_Swartz "wikilink")[2][3] created Markdown in
2004 as a [markup language](markup_language "wikilink") that is intended
to be easy to read in its source code form.[4] Markdown is widely used
for [blogging](blog "wikilink") and [instant
messaging](instant_messaging "wikilink"), and also used elsewhere in
[online forums](online_forums "wikilink"), [collaborative
software](collaborative_software "wikilink"),
[documentation](documentation "wikilink") pages, and [readme
files](README "wikilink").

The initial description of Markdown[5] contained ambiguities and raised
unanswered questions, causing implementations to both intentionally and
accidentally diverge from the original version. This was addressed in
2014 when long-standing Markdown contributors released
[CommonMark](#Standardization "wikilink"), an unambiguous specification
and test suite for Markdown.[6]

## History

Markdown was inspired by pre-existing
[conventions](Convention_(norm) "wikilink") for marking up [plain
text](plain_text "wikilink") in [email](email "wikilink") and
[usenet](usenet "wikilink") posts, such as the earlier markup languages
[setext](setext "wikilink") (),
[Textile](Textile_(markup_language) "wikilink") (c. 2002), and
[reStructuredText](reStructuredText "wikilink") (c. 2002).[7]

In 2002 [Aaron Swartz](Aaron_Swartz "wikilink") created
[atx](atx_(markup_language) "wikilink") and referred to it as "the true
structured text format". Gruber and Swartz[8][9] created the Markdown
language in 2004, with the goal of enabling people "to write using an
easy-to-read and easy-to-write plain text format, optionally convert it
to structurally valid [XHTML](XHTML "wikilink") (or
[HTML](HTML "wikilink"))."[10]

Its key design goal was *readability*, that the language be readable
as-is, without looking like it has been marked up with tags or
formatting instructions, unlike text formatted with 'heavier' [markup
languages](markup_language "wikilink"), such as [Rich Text
Format](Rich_Text_Format "wikilink") (RTF), HTML, or even
[wikitext](wikitext "wikilink") (each of which have obvious in-line tags
and formatting instructions which can make the text more difficult for
humans to read).

Gruber wrote a [Perl](Perl "wikilink") script, , which converts
marked-up text input to valid,
[well-formed](XML#Well-formedness_and_error-handling "wikilink") XHTML
or HTML and replaces angle brackets (, ) and
[ampersands](ampersand "wikilink") () with their corresponding
[character entity references](character_entity_references "wikilink").
It can take the role of a standalone script, a plugin for
[Blosxom](Blosxom "wikilink") or a [Movable
Type](Movable_Type "wikilink"), or of a text filter for
[BBEdit](BBEdit "wikilink").[11]

## Rise and divergence

As Markdown's popularity grew rapidly, many Markdown implementations
appeared, driven mostly by the need for additional features such as
tables, footnotes, definition lists,[12] and Markdown inside HTML
blocks.

The behavior of some of these diverged from the reference
implementation, as Markdown was only characterised by an informal
specification[13] and a Perl implementation for conversion to HTML.

At the same time, a number of ambiguities in the informal specification
had attracted attention.[14] These issues spurred the creation of tools
such as Babelmark[15][16] to compare the output of various
implementations,[17] and an effort by some developers of Markdown
parsers for standardisation. However, Gruber has argued that complete
standardization would be a mistake: "Different sites (and people) have
different needs. No one syntax would make all happy."[18]

Gruber avoided using curly braces in Markdown to unofficially reserve
them for implementation-specific extensions.[19]

## Standardization

From 2012, a group of people, including [Jeff
Atwood](Jeff_Atwood "wikilink") and [John
MacFarlane](John_MacFarlane_(philosopher) "wikilink"), launched what
Atwood characterised as a standardisation effort.[20] A community
website now aims to "document various tools and resources available to
document authors and developers, as well as implementors of the various
Markdown implementations".[21] In September 2014, Gruber objected to the
usage of "Markdown" in the name of this effort and it was rebranded as
CommonMark.[22][23] CommonMark.org published several versions of a
specification, reference implementation, test suite, and "\[plans\] to
announce a finalized 1.0 spec and test suite in 2019."[24] No 1.0 spec
has since been released as major issues still remain unsolved.[25]
Nonetheless, the following websites and projects have adopted
CommonMark: [Discourse](Discourse_(software) "wikilink"),
[GitHub](GitHub "wikilink"), [GitLab](GitLab "wikilink"),
[Reddit](Reddit "wikilink"), [Qt](Qt_(software) "wikilink"), [Stack
Exchange](Stack_Exchange "wikilink") ([Stack
Overflow](Stack_Overflow "wikilink")), and
[Swift](Swift_(programming_language) "wikilink").

In March 2016 two relevant informational Internet
[RFCs](Request_for_Comments "wikilink") were published:

-   introduced [MIME](MIME "wikilink") type <small></small>.

-   discussed and registered the variants
    [MultiMarkdown](MultiMarkdown "wikilink"), GitHub Flavored Markdown
    (GFM), [Pandoc](Pandoc "wikilink"), and Markdown Extra among
    others.[26]

## Variants

Websites like [Bitbucket](Bitbucket "wikilink"),
[Diaspora](Diaspora_(social_network) "wikilink"),
[GitHub](GitHub "wikilink"),[27]
[OpenStreetMap](OpenStreetMap "wikilink"),
[Reddit](Reddit "wikilink"),[28]
[SourceForge](SourceForge "wikilink"),[29] and [Stack
Exchange](Stack_Exchange "wikilink")[30] use variants of Markdown to
make discussions between users easier.

Depending on implementation, basic inline [HTML
tags](HTML_tag "wikilink") may be supported.[31] Italic text may be
implemented by `_underscores_` or `*single-asterisks*`.[32]

### GitHub Flavored Markdown

GitHub had been using its own variant of Markdown since as early as
2009,[33] which added support for additional formatting such as tables
and nesting [block content](HTML_element#Block_elements "wikilink")
inside list elements, as well as GitHub-specific features such as
auto-linking references to commits, issues, usernames, etc. In 2017,
GitHub released a formal specification of its GitHub Flavored Markdown
(GFM) that is based on CommonMark.[34] It is a [strict
superset](Superset "wikilink") of CommonMark, following its
specification exactly except for *tables, strikethrough, autolinks and
task lists,* which GFM adds as extensions.[35] Accordingly, GitHub also
changed the parser used on their sites, which required that some
documents be changed. For instance, GFM now requires that the [hash
symbol](number_sign "wikilink") that creates a heading be separated from
the heading text by a space character.

### Markdown Extra

Markdown Extra is a [lightweight markup
language](lightweight_markup_language "wikilink") based on Markdown
implemented in [PHP](PHP "wikilink") (originally),
[Python](Python_(programming_language) "wikilink") and
[Ruby](Ruby_(programming_language) "wikilink").[36] It adds the
following features that are not available with regular Markdown:

-   Markdown markup inside [HTML](HTML "wikilink") blocks
-   Elements with id/class attribute
-   "Fenced code blocks" that span multiple lines of code
-   Tables[37]
-   Definition lists
-   Footnotes
-   Abbreviations

Markdown Extra is supported in some [content management
systems](content_management_system "wikilink") such as
[Drupal](Drupal "wikilink"),[38] [Grav (CMS)](Grav_(CMS) "wikilink") and
[TYPO3](TYPO3 "wikilink").[39]

### LiaScript

LiaScript[40] is a Markdown dialect that was designed to create
interactive educational content. It is implemented in
[Elm](Elm_(programming_language) "wikilink") and
[TypeScript](TypeScript "wikilink") and adds additional syntax elements
to define features like:

-   Animations
-   Automatic speech output
-   Mathematical formulas (using [KaTeX](KaTeX "wikilink"))
-   [ASCII art](ASCII_art "wikilink") diagrams
-   Various types of quizzes and surveys
-   [JavaScript](JavaScript "wikilink") is natively supported and can be
    attached to various elements, this way code fragments can be made
    executable and editable

## Examples

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 34%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th width="33%"><p>Text using Markdown syntax</p></th>
<th width="34%"><p>Corresponding HTML produced by a Markdown
processor</p></th>
<th width="33%"><p>Text viewed in a browser</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><pre class="md"><code>Heading
=======
&#10;Sub-heading
-----------
&#10;# Alternative heading
&#10;## Alternative sub-heading
&#10;Paragraphs are separated 
by a blank line.
&#10;Two spaces at the end of a line  
produce a line break.</code></pre></td>
<td><pre class="html"><code>&lt;h1&gt;Heading&lt;/h1&gt;
&#10;&lt;h2&gt;Sub-heading&lt;/h2&gt;
&#10;&lt;h1&gt;Alternative heading&lt;/h1&gt;
&#10;&lt;h2&gt;Alternative sub-heading&lt;/h2&gt;
&#10;&lt;p&gt;Paragraphs are separated
by a blank line.&lt;/p&gt;
&#10;&lt;p&gt;Two spaces at the end of a line&lt;br /&gt;
produce a line break.&lt;/p&gt;</code></pre></td>
<td><p>&lt;div style="color: #000000; background: none; overflow:
hidden; page-break-after: avoid; font-size: 1.8em; font-family:
Georgia,Times,serif; margin-top: 1em; margin-bottom: 0.25em;
line-height: 1.3; padding: 0; border-bottom: 1px solid
#AAAAAA;&gt;Heading</p>
</div>
<p>&lt;div style="color: #000000; background: none; overflow: hidden;
page-break-after: avoid; font-size: 1.5em; font-family:
Georgia,Times,serif; margin-top: 1em; margin-bottom: 0.25em;
line-height: 1.3; padding: 0; border-bottom: 1px solid
#AAAAAA;&gt;Sub-heading</p>
</div>
<p>&lt;div style="color: #000000; background: none; overflow: hidden;
page-break-after: avoid; font-size: 1.8em; font-family:
Georgia,Times,serif; margin-top: 1em; margin-bottom: 0.25em;
line-height: 1.3; padding: 0; border-bottom: 1px solid
#AAAAAA;&gt;Alternative heading</p>
</div>
<p>&lt;div style="color: #000000; background: none; overflow: hidden;
page-break-after: avoid; font-size: 1.5em; font-family:
Georgia,Times,serif; margin-top: 1em; margin-bottom: 0.25em;
line-height: 1.3; padding: 0; border-bottom: 1px solid
#AAAAAA;&gt;Alternative sub-heading</p>
</div>
<p>Paragraphs are separated by a blank line.</p>
<p>Two spaces at the end of a line<br />
produce a line break.</p></td>
</tr>
<tr class="even">
<td><pre class="md"><code>Text attributes _italic_, **bold**, `monospace`.
&#10;Horizontal rule:
&#10;---</code></pre></td>
<td><pre class="html"><code>&lt;p&gt;Text attributes &lt;em&gt;italic&lt;/em&gt;, &lt;strong&gt;bold&lt;/strong&gt;, &lt;code&gt;monospace&lt;/code&gt;.&lt;/p&gt;
&#10;&lt;p&gt;Horizontal rule:&lt;/p&gt;
&#10;&lt;hr /&gt;</code></pre></td>
<td><p>Text attributes <em>italic</em>, <strong>bold</strong>,
<code>monospace</code>.</p>
<p>Horizontal rule:</p>
<hr /></td>
</tr>
<tr class="odd">
<td><pre class="md"><code>Bullet lists nested within numbered list:
&#10;  1. fruits
     * apple
     * banana
  2. vegetables
     - carrot
     - broccoli
  </code></pre></td>
<td><pre class="html"><code>&lt;p&gt;Bullet lists nested within numbered list:&lt;/p&gt;
&#10;&lt;ol&gt;
  &lt;li&gt;fruits &lt;ul&gt;
      &lt;li&gt;apple&lt;/li&gt;
      &lt;li&gt;banana&lt;/li&gt;
  &lt;/ul&gt;&lt;/li&gt;
  &lt;li&gt;vegetables &lt;ul&gt;
      &lt;li&gt;carrot&lt;/li&gt;
      &lt;li&gt;broccoli&lt;/li&gt;
  &lt;/ul&gt;&lt;/li&gt;
&lt;/ol&gt;</code></pre></td>
<td><p>Bullet lists nested within numbered list:</p>
<ol>
<li>fruits
<ul>
<li>apple</li>
<li>banana</li>
</ul></li>
<li>vegetables
<ul>
<li>carrot</li>
<li>broccoli</li>
</ul></li>
</ol></td>
</tr>
<tr class="even">
<td></td>
<td><p>[Image](Icon-pictures.png "icon")</p>
<p>&gt; Markdown uses email-style characters for blockquoting. &gt; &gt;
Multiple paragraphs need to be prepended individually.</p>
<p>Most inline <abbr title="Hypertext Markup Language">HTML</abbr> tags
are supported.</p>
</syntaxhighlight></td>
<td><pre class="html"><code>&lt;p&gt;A &lt;a href=&quot;http://example.com&quot;&gt;link&lt;/a&gt;.&lt;/p&gt;
&#10;&lt;p&gt;&lt;img alt=&quot;Image&quot; title=&quot;icon&quot; src=&quot;Icon-pictures.png&quot; /&gt;&lt;/p&gt;
&#10;&lt;blockquote&gt;
&lt;p&gt;Markdown uses email-style characters for blockquoting.&lt;/p&gt;
&lt;p&gt;Multiple paragraphs need to be prepended individually.&lt;/p&gt;
&lt;/blockquote&gt;
&#10;&lt;p&gt;Most inline &lt;abbr title=&quot;Hypertext Markup Language&quot;&gt;HTML&lt;/abbr&gt; tags are supported.&lt;/p&gt;</code></pre></td>
</tr>
<tr class="odd">
<td><pre class="md"><code>m</code></pre></td>
<td><pre class="html"><code>h</code></pre></td>
<td><p>end</p>
<p><code>--&gt;</code></p></td>
</tr>
</tbody>
</table>

## Implementations

Implementations of Markdown are available for over a dozen [programming
languages](programming_language "wikilink"); in addition, many
applications, platforms and [frameworks](Software_framework "wikilink")
support Markdown.[41] For example, Markdown
[plugins](Plug-in_(computing) "wikilink") exist for every major
[blogging](blog "wikilink") platform.[42]

While Markdown is a minimal markup language and is read and edited with
a normal [text editor](text_editor "wikilink"), there are specially
designed editors that preview the files with styles, which are available
for all major platforms. Many general-purpose text and [code
editors](Source-code_editor "wikilink") have [syntax
highlighting](syntax_highlighting "wikilink") plugins for Markdown built
into them or available as optional download. Editors may feature a
side-by-side preview window or render the code directly in a
[WYSIWYG](WYSIWYG "wikilink") fashion.

Some apps, services and editors support Markdown as an editing format,
including:

-   [Bugzilla](Bugzilla "wikilink") uses a customized version of
    Markdown.[43]
-   [ChatGPT](ChatGPT "wikilink"): Output from the AI model formatted in
    Markdown will be rendered in LaTeX and HTML by the ChatGPT client,
    and the model is encouraged to use Markdown to format its output.
    Markdown provided by the user will not be formatted by the client,
    but will still be passed to the AI model unaltered.
-   [Discord](Discord_(software) "wikilink"): chat messages[44]
-   [Discourse](Discourse_(software) "wikilink") uses the CommonMark
    flavor of Markdown in the forum post composer.
-   [Doxygen](Doxygen "wikilink"): a source code documentation generator
    which supports Markdown with extra features[45]
-   [GitHub](GitHub "wikilink") Flavored Markdown (GFM) ignores
    underscores in words, and adds [syntax
    highlighting](syntax_highlighting "wikilink"), [task
    lists](task_list "wikilink"),[46] and tables[47]
-   The [GNOME Evolution](GNOME_Evolution "wikilink") email client
    supports composing messages in Markdown format,[48] with the ability
    to send and render emails in pure Markdown format
    (`Content-Type: text/markdown;`) or to convert Markdown to
    [plaintext](plaintext "wikilink") or [HTML
    email](HTML_email "wikilink") when sending.
-   [Joplin](Joplin_(software) "wikilink"): a note-taking application
    that supports markdown formatting[49]
-   [JotterPad](JotterPad "wikilink"): an online WYSIWYG editor that
    supports Markdown and Fountain[50]
-   [Kanboard](Kanboard "wikilink") uses the standard Markdown syntax as
    its only formatting syntax for task descriptions.[51]
-   [Microsoft Azure DevOps](Microsoft_Azure_DevOps "wikilink")' wiki
    feature has its own implementation[52]
-   [Microsoft Teams](Microsoft_Teams "wikilink"): chat messages[53]
-   [Misskey](Misskey "wikilink"), its numerous forks and other
    [Fediverse](Fediverse "wikilink") platforms such as
    [Akkoma](Akkoma "wikilink")[54] use a custom text format
    misleadingly called "Misskey-Flavored Markdown (MFM)", with support
    for standard nestable block quotes `>` and inline emphasis `` _*` ``
    as well as extensions seen elsewhere for `@` mentions, `#` tags,
    custom [emoji](emoji "wikilink") `:foo:`, automatic URL detection
    and toggleable link target preview, but no support for headings,
    lists, reference links and other standard Markdown features. It
    supports a handful of HTML-like tags (`<small> <center; <plain>`)
    and a special notation with English keywords or key-value pairs
    `$[`*`key=value`*` `*`content`*`]` for spans with stylistic effects
    applied, e.g. fonts, blurs, borders and transformations such as
    flipping, shifting, rotating, scaling and animation, but also for
    [furigana](furigana "wikilink") and search boxes.[55] The message
    format of such [ActivityPub](ActivityPub "wikilink") objects that
    can be consumed as messages is `text/x.misskeymarkdown`.
-   The [Mozilla Thunderbird](Mozilla_Thunderbird "wikilink") email
    client supports Markdown through the "[Markdown here
    Revival](https://addons.thunderbird.net/en-US/thunderbird/addon/markdown-here-revival/)"
    add-on.
-   [Nextcloud Notes](Nextcloud "wikilink"): the default app for taking
    notes on the Nextcloud platform supports formatting using
    Markdown[56]
-   [Obsidian](Obsidian_(software) "wikilink") is note-taking software
    based on Markdown files.[57]
-   [RMarkdown](RMarkdown "wikilink")[58]
-   [RStudio](RStudio "wikilink"): an
    [IDE](Integrated_development_environment "wikilink") for
    [R](R_(programming_language) "wikilink"). It provides a
    [C++](C++ "wikilink") [wrapper
    function](wrapper_function "wikilink") for a markdown variant called
    sundown[59]
-   [Simplenote](Simplenote "wikilink")[60]

## See also

-   [Comparison of document markup
    languages](Comparison_of_document_markup_languages "wikilink")
-   [Comparison of documentation
    generators](Comparison_of_documentation_generators "wikilink")
-   [Lightweight markup
    language](Lightweight_markup_language "wikilink")
-   [Wiki markup](Wiki_markup "wikilink")

## Explanatory notes

## References

## External links

-   for original John Gruber markup

[Category:Computer-related introductions in
2004](Category:Computer-related_introductions_in_2004 "wikilink")
[Category:Lightweight markup
languages](Category:Lightweight_markup_languages "wikilink")
[Category:Open formats](Category:Open_formats "wikilink")

[1]

[2]

[3]

[4]

[5]

[6]

[7]

[8]

[9]

[10] Markdown 1.0.1 readme source code

[11]

[12] Technically HTML description lists

[13]

[14]

[15]

[16]

[17]

[18]

[19]

[20]

[21]

[22]

[23]

[24]

[25]

[26]

[27]

[28]

[29]

[30]

[31]

[32]

[33]

[34]

[35]

[36]

[37]

[38]

[39]

[40]

[41]

[42]

[43]

[44]

[45]

[46]

[47]

[48]

[49]

[50]

[51]

[52] <https://learn.microsoft.com/en-us/azure/devops/project/wiki/markdown-guidance?view=azure-devops>

[53]

[54]

[55]

[56]

[57]

[58]

[59]

[60]
