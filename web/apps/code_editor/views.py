from django.shortcuts import render
from bs4 import BeautifulSoup
import bleach

SAFE_TAGS = [
    "p", "br", "hr",
    "b", "strong",
    "i", "em",
    "u", "s", "small",
    "mark", "sub", "sup",
    "h1", "h2", "h3", "h4", "h5", "h6",
    "div", "span",
    "ul", "ol", "li",
    "dl", "dt", "dd",
    "table", "thead", "tbody", "tfoot",
    "tr", "td", "th",
    "caption",
    "blockquote",
    "pre", "code", "kbd", "samp",
    "a",
    "img",
    "article", "section",
    "header", "footer",
    "main", "aside",
    "nav",
    "abbr", "cite",
    "q", "time",
    "details", "summary"
]

SAFE_ATTRIBUTES = {
    "*": ["class"],

    "a": ["href", "title", "target", "rel"],

    "img": ["src", "alt", "width", "height"],

    "td": ["colspan", "rowspan"],
    "th": ["colspan", "rowspan"],
}

DANGEROUS_TAGS = [
    "script",
    "style",
    "iframe",
    "object",
    "embed",
    "svg",
    "math",
    "canvas",
    "form",
    "input",
    "textarea",
    "select",
    "option",
    "button",
    "link",
    "meta",
    "base"
]

def remove_tags(html):
    goal = BeautifulSoup(html, "html.parser")

    for tag in DANGEROUS_TAGS:
        for element in goal.find_all(tag):
            element.decompose()

    return str(goal)

def editor(request):
    code = ""

    if request.method == "POST":
        raw_code = request.POST.get("code", "")
        raw_code = remove_tags(raw_code)
        code = bleach.clean(
            raw_code,
            tags=SAFE_TAGS,
            attributes=SAFE_ATTRIBUTES,
            strip=True,
            protocols=["http", "https"]
        )

    return render(request, "code_editor/code.html", {
        "rcode": code
    })
