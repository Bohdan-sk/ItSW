from bs4 import BeautifulSoup
import requests as req


def parser():
    resp = req.get("https://stopgame.ru/review/new/izumitelno")
    soup = BeautifulSoup(resp.content, 'html.parser')

    title = []
    brief = []
    date = []
    views = []
    comments = []

    for el in soup.select('.lent-block'):
        title.append(el.select('.lent-title')[0].text)
        brief.append(el.select('.brief')[0].text)
        date.append(el.select('.lent-date')[0].text)
        views.append(el.select('.lent-views')[0].text)
        comments.append(el.select('.lent-comments')[0].text)

    xml = soup_xml(title, brief, date, views, comments)

    with open("blogs.xml", 'w') as file:
        file.write(xml.prettify())

def soup_xml(title, brief, date, views, comments):
    soup = BeautifulSoup(features="xml")
    blogs = soup.new_tag("blogs")

    for i in range(len(title)):

        blog = soup.new_tag("blog", attrs={"id": i})

        title_tag = soup.new_tag("title")
        title_tag.string = title[i]
        blog.append(title_tag)

        brief_tag = soup.new_tag("brief")
        brief_tag.string = brief[i]
        blog.append(brief_tag)

        date_tag = soup.new_tag("date")
        date_tag.string = date[i]
        blog.append(date_tag)

        views_tag = soup.new_tag("views")
        views_tag.string = views[i]
        blog.append(views_tag)

        comments_tag = soup.new_tag("comments")
        comments_tag.string = comments[i]
        blog.append(comments_tag)

        blogs.append(blog)

    soup.append(blogs)

    return soup

parser()
